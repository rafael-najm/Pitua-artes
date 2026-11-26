"""Monta os Reels da Pituá a partir dos clipes do ensaio (versões 1080x1920 em BRUTOS/mezz).

Cada Reel é uma lista de cenas (clipe, início, duração no bruto, velocidade), textos por cima
(com as fontes e cores do site) e uma cartela final. Sem música: a música entra no próprio Instagram.

Uso: BRUTOS=/caminho/brutos SAIDA=/caminho/saida python3 reels/gerar.py [nome ...]
"""
import json
import os
import subprocess
import sys
from pathlib import Path

from roteiro import REELS

RAIZ = Path(__file__).resolve().parent.parent
PASTA = RAIZ / 'reels'
FONTES = RAIZ / 'node_modules' / '@fontsource-variable'
BRUTOS = Path(os.environ['BRUTOS'])
SAIDA = Path(os.environ['SAIDA'])
TMP = SAIDA / '.tmp'
LOGO = (RAIZ / 'src/assets/marca/pitua-logo.png').as_uri()
LOGO_CLARO = (RAIZ / 'src/assets/marca/pitua-logo-escuro.png').as_uri()

FPS = 30
COR = ("eq=contrast=1.1:brightness=0.005:saturation=1.25,"
       "curves=master='0/0 0.25/0.215 0.5/0.515 0.78/0.82 1/1'")


def clipe(nome):
    achados = list((BRUTOS / 'mezz').glob(f'*_{nome}.mp4'))
    assert len(achados) == 1, nome
    return achados[0]


def sh(*args):
    subprocess.run([str(a) for a in args], check=True)


# ——— textos e cartelas (HTML -> PNG transparente)

def texto(t):
    pos = t.get('pos', 'baixo')
    eb = f'<p class="eyebrow">{t["eyebrow"]}</p>' if t.get('eyebrow') else ''
    tx = f'<p class="texto">{t["texto"]}</p>' if t.get('texto') else ''
    return (f'<div class="ov {pos}"><div class="bloco">{eb}'
            f'<h1 class="titulo {t.get("tam", "")}">{t["titulo"]}</h1>{tx}</div></div>')


def fim(f):
    azul = f.get('fundo') == 'azul'
    return (f'<div class="fim {"azul" if azul else ""}"><img class="logo" src="{LOGO_CLARO if azul else LOGO}" alt="">'
            f'<h1 class="titulo">{f["titulo"]}</h1><p class="texto">{f.get("texto", "")}</p>'
            f'<p class="link">{f.get("chamada", "Link na bio")}</p><p class="site">pituaartes.com.br</p></div>')


def renderiza(pecas, nome):
    """pecas: lista de (arquivo_saida, html). Gera PNGs 1080x1920 com fundo transparente."""
    fontes = f'''
    @font-face {{ font-family: 'Newsreader'; font-style: normal; font-weight: 200 800;
      src: url('{(FONTES / 'newsreader/files/newsreader-latin-wght-normal.woff2').as_uri()}') format('woff2'); }}
    @font-face {{ font-family: 'Newsreader'; font-style: italic; font-weight: 200 800;
      src: url('{(FONTES / 'newsreader/files/newsreader-latin-wght-italic.woff2').as_uri()}') format('woff2'); }}
    @font-face {{ font-family: 'Jost'; font-style: normal; font-weight: 100 900;
      src: url('{(FONTES / 'jost/files/jost-latin-wght-normal.woff2').as_uri()}') format('woff2'); }}'''
    css = (PASTA / 'estilo.css').read_text(encoding='utf-8')
    corpo = ''.join(h.replace('<div class="', f'<div data-saida="{s}" class="', 1) for s, h in pecas)
    arq = TMP / f'textos-{nome}.html'
    arq.write_text(f'<!doctype html><html><head><meta charset="utf-8"><style>{fontes}{css}</style></head>'
                   f'<body>{corpo}</body></html>', encoding='utf-8')
    script = f'''
const {{ chromium }} = require('playwright');
(async () => {{
  const b = await chromium.launch();
  const p = await b.newPage({{ viewport: {{ width: 1080, height: 1920 }}, deviceScaleFactor: 1 }});
  await p.goto({json.dumps(arq.as_uri())}, {{ waitUntil: 'load' }});
  await p.evaluate(() => document.fonts.ready);
  for (const el of await p.$$('[data-saida]')) {{
    await el.evaluate(e => e.scrollIntoView({{ block: 'start' }}));
    await p.waitForTimeout(40);
    await el.screenshot({{ path: await el.getAttribute('data-saida'), omitBackground: true }});
  }}
  await b.close();
}})();'''
    env = dict(os.environ, NODE_PATH=subprocess.run(['npm', 'root', '-g'], capture_output=True, text=True).stdout.strip())
    subprocess.run(['node', '-e', script], check=True, env=env, cwd=TMP)


# ——— montagem

def monta(nome, r):
    d = TMP / nome
    d.mkdir(parents=True, exist_ok=True)
    textos = [(str(d / f'texto{i}.png'), texto(t)) for i, t in enumerate(r['textos'])]
    cartela = (str(d / 'fim.png'), fim(r['fim']))
    renderiza(textos + [cartela], nome)

    # 1. cada cena: corte, câmera lenta (o bruto é 60 fps) e cor
    cenas, durs = [], []
    for i, (c, ss, src, vel) in enumerate(r['cenas']):
        out = d / f'cena{i}.mp4'
        sh('ffmpeg', '-v', 'error', '-y', '-ss', ss, '-t', src, '-i', clipe(c),
           '-vf', f'setpts=PTS/{vel},fps={FPS},{COR},format=yuv420p',
           '-c:v', 'libx264', '-crf', 14, '-preset', 'fast', '-an', out)
        cenas.append(out)
        durs.append(round(src / vel, 3))
    tfim = r['fim'].get('dur', 3.2)
    out = d / 'fim.mp4'
    sh('ffmpeg', '-v', 'error', '-y', '-loop', 1, '-t', tfim, '-i', cartela[0],
       '-vf', f'fps={FPS},format=yuv420p', '-c:v', 'libx264', '-crf', 14, '-preset', 'fast', out)
    cenas.append(out)
    durs.append(tfim)

    # 2. junta com transições suaves e põe os textos por cima
    XF = r.get('xf', 0.4)
    ins, fil = [], []
    for c in cenas:
        ins += ['-i', c]
    atual, total = '[0:v]', durs[0]
    for i in range(1, len(cenas)):
        rot = f'[x{i}]'
        fil.append(f'{atual}[{i}:v]xfade=transition=fade:duration={XF}:offset={total - XF:.3f}{rot}')
        atual, total = rot, total + durs[i] - XF
    n = len(cenas)
    inicio = [sum(durs[:i]) - i * XF for i in range(len(durs))]  # onde cada cena começa no vídeo final
    for k, (t, (png, _)) in enumerate(zip(r['textos'], textos)):
        if 'cena' in t:  # texto preso a uma cena: entra logo depois que ela aparece
            t0 = round(inicio[t['cena']] + t.get('mais', 0.3), 3)
            t1 = round(t0 + t.get('dur', 3.4), 3)
        else:
            t0, t1 = t['de'], t['ate']
        ins += ['-loop', 1, '-t', round(t1 - t0, 3), '-i', png]
        j = n + k
        fil.append(f'[{j}:v]format=rgba,fade=t=in:st=0:d=0.5:alpha=1,fade=t=out:st={t1 - t0 - 0.5:.3f}:d=0.5:alpha=1,'
                   f'setpts=PTS+{t0}/TB[t{k}]')
        fil.append(f'{atual}[t{k}]overlay=eof_action=pass[v{k}]')
        atual = f'[v{k}]'
    fil.append(f'{atual}fade=t=in:st=0:d=0.3,format=yuv420p[vout]')
    final = SAIDA / f'{r["arquivo"]}.mp4'
    sh('ffmpeg', '-v', 'error', '-y', *ins, '-f', 'lavfi', '-t', round(total, 3), '-i', 'anullsrc=r=48000:cl=stereo',
       '-filter_complex', ';'.join(fil), '-map', '[vout]', '-map', f'{n + len(textos)}:a',
       '-c:v', 'libx264', '-crf', 17, '-preset', 'slow', '-profile:v', 'high', '-r', FPS,
       '-c:a', 'aac', '-b:a', '128k', '-shortest', '-movflags', '+faststart', final)

    # 3. capa: um quadro do vídeo, para escolher como capa no Instagram
    if 'capa' in r:
        sh('ffmpeg', '-v', 'error', '-y', '-ss', r['capa'], '-i', final, '-frames:v', 1, '-q:v', 2,
           SAIDA / f'{r["arquivo"]}-capa.jpg')
    print(f'{final.name}: {total:.1f}s')
    return total


if __name__ == '__main__':
    TMP.mkdir(parents=True, exist_ok=True)
    nomes = sys.argv[1:] or list(REELS)
    for nm in nomes:
        monta(nm, REELS[nm])
