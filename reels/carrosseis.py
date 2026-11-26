"""Carrosséis de fotos para intercalar com os Reels no feed (1080 x 1350, formato 4:5).

Uso: SAIDA=/caminho/saida python3 reels/carrosseis.py
"""
import json
import os
import subprocess
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
PASTA = RAIZ / 'reels'
A = RAIZ / 'src' / 'assets'
FONTES = RAIZ / 'node_modules' / '@fontsource-variable'
SAIDA = Path(os.environ['SAIDA']) / 'carrosseis'
LOGO_CLARO = (A / 'marca/pitua-logo-escuro.png').as_uri()


def u(c):
    return (A / c).as_uri()


def capa(foto, eyebrow, titulo):
    return (f'<div class="sl capa"><img class="cheia" src="{u(foto)}" alt=""><div class="bloco">'
            f'<p class="eyebrow">{eyebrow}</p><h1 class="titulo">{titulo}</h1></div></div>')


def foto(c, nome):
    return f'<div class="sl"><img class="cheia" src="{u(c)}" alt=""><span class="tag">{nome}</span></div>'


def quad(c, nome, linha):
    return (f'<div class="sl quad creme"><div class="moldura"><img src="{u(c)}" alt=""></div>'
            f'<h2>{nome}</h2><p>{linha}</p></div>')


def cta(titulo, texto, chamada='Link na bio'):
    return (f'<div class="sl cta"><img class="logo" src="{LOGO_CLARO}" alt=""><h1 class="titulo">{titulo}</h1>'
            f'<p class="texto">{texto}</p><p class="link">{chamada}</p></div>')


def frase(titulo, texto):
    return (f'<div class="sl cta claro"><p class="eyebrow">Como funciona</p><h1 class="titulo">{titulo}</h1>'
            f'<p class="texto">{texto}</p></div>')


P = 'personalizar/'
CARROSSEIS = {
    'presentes-de-fim-de-ano': [
        capa('pecas/potiche-tulipa/01.jpg', 'Presentes pintados à mão', 'Um presente que<br><em>ninguém mais tem.</em>'),
        frase('Você escolhe a peça.<br><em>Eu pinto do seu jeito.</em>',
              'Um nome, uma frase, um bichinho, as cores da casa. Cada peça é pintada à mão e só existe uma vez.'),
        quad(P + 'caneca-afeto.webp', 'Caneca Afeto', 'Com o nome, a frase ou o desenho que você escolher.'),
        quad(P + 'porta-joias-do-dia.webp', 'Porta-joias', 'Para guardar o que é precioso.'),
        quad(P + 'moringa-faixa.webp', 'Moringa com Copo', 'Para a cabeceira, nas cores da casa.'),
        quad(P + 'vela-copo-porcelana.webp', 'Vela em Copo de Porcelana', 'Depois que a vela acaba, o copo fica.'),
        quad(P + 'potes-multiuso-mel.webp', 'Potes Multiuso', 'Para a cozinha, o banheiro ou a penteadeira.'),
        quad(P + 'caneca-com-tampa.webp', 'Caneca com Tampa', 'O chá de todo dia, mais bonito.'),
        cta('Encomende o seu<br><em>presente de fim de ano.</em>', 'Cada peça é pintada à mão, só para quem vai receber.'),
    ],
    'chanuka': [
        capa('pecas/casticais-shabat-shalom/01.jpg', 'Judaica pintada à mão', 'Luz que passa<br><em>de geração em geração.</em>'),
        frase('Peças de Judaica<br><em>com a sua história.</em>',
              'Você escolhe a peça e me conta a sua ideia. Eu crio o desenho e pinto à mão, com as cores que você quiser.'),
        quad(P + 'chanukia.webp', 'Chanukiá', 'Pintada à mão, com as cores e o desenho que você escolher.'),
        quad(P + 'par-de-casticais.webp', 'Par de Castiçais', 'Para acender as velas do Shabat.'),
        quad(P + 'copinhos-shabat.webp', 'Par de Copinhos', 'Para o kidush, com o nome da família.'),
        foto('pecas/taca-de-kidush/01.jpg', 'Kos de Kidush · acervo'),
        foto('pecas/prato-de-shabat/01.jpg', 'Prato de Shabat Paz · Salam · Shalom · acervo'),
        cta('Chag <em>Chanucá Sameach!</em>', 'Peças de Judaica pintadas à mão, sob encomenda.'),
    ],
    'vasos-do-acervo': [
        capa('pecas/vaso-peixes/01.jpg', 'Acervo Pituá', 'Vasos que são<br><em>obras de arte.</em>'),
        foto('pecas/anfora-cisnes/01.jpg', 'Ânfora Cisnes'),
        foto('pecas/vaso-pavao-persa/01.jpg', 'Vaso Pavão Persa'),
        foto('pecas/potiche-tulipa/01.jpg', 'Potiche Tulipa'),
        foto('pecas/vaso-rouen/01.jpg', 'Vaso Rouen'),
        foto('pecas/vaso-conchas/01.jpg', 'Vaso Conchas'),
        cta('Gostou?<br><em>Ela pode inspirar a sua.</em>', 'Peças únicas do acervo, para inspirar uma nova, pintada só para você.'),
    ],
    'quarto-do-bebe': [
        capa('pecas/conjunto-quarto-do-bebe-menino-rafa/01.jpg', 'Quarto do bebê', 'Lembranças que<br><em>crescem junto.</em>'),
        foto('pecas/abajur-menino-rafa/01.jpg', 'Abajur Menino Rafa'),
        foto('pecas/conjunto-quarto-do-bebe-menino-rafa/02.jpg', 'Conjunto Quarto do Bebê Menino Rafa'),
        foto('pecas/moringa-abelha-mel/01.jpg', 'Moringa Abelha Mel'),
        foto('pecas/conjunto-quarto-do-bebe-abelha-mel/01.jpg', 'Conjunto Quarto do Bebê Abelha Mel'),
        cta('Com o nome<br><em>e a história do bebê.</em>', 'Conjuntos pintados à mão, sob encomenda.'),
    ],
}


def gerar():
    fontes = f'''
    @font-face {{ font-family: 'Newsreader'; font-style: normal; font-weight: 200 800;
      src: url('{(FONTES / 'newsreader/files/newsreader-latin-wght-normal.woff2').as_uri()}') format('woff2'); }}
    @font-face {{ font-family: 'Newsreader'; font-style: italic; font-weight: 200 800;
      src: url('{(FONTES / 'newsreader/files/newsreader-latin-wght-italic.woff2').as_uri()}') format('woff2'); }}
    @font-face {{ font-family: 'Jost'; font-style: normal; font-weight: 100 900;
      src: url('{(FONTES / 'jost/files/jost-latin-wght-normal.woff2').as_uri()}') format('woff2'); }}'''
    css = (PASTA / 'estilo.css').read_text(encoding='utf-8')
    partes = []
    for nome, slides in CARROSSEIS.items():
        (SAIDA / nome).mkdir(parents=True, exist_ok=True)
        for i, h in enumerate(slides, 1):
            partes.append(h.replace('<div class="sl', f'<div data-saida="{SAIDA / nome / f"{i:02d}.jpg"}" class="sl', 1))
    arq = SAIDA / 'carrosseis.html'
    arq.write_text(f'<!doctype html><html><head><meta charset="utf-8"><style>{fontes}{css}</style></head>'
                   f'<body>{"".join(partes)}</body></html>', encoding='utf-8')
    script = f'''
const {{ chromium }} = require('playwright');
(async () => {{
  const b = await chromium.launch();
  const p = await b.newPage({{ viewport: {{ width: 1080, height: 1350 }}, deviceScaleFactor: 1 }});
  await p.goto({json.dumps(arq.as_uri())}, {{ waitUntil: 'load' }});
  await p.evaluate(() => document.fonts.ready);
  for (const el of await p.$$('[data-saida]')) {{
    await el.evaluate(e => e.scrollIntoView({{ block: 'start' }}));
    await p.waitForTimeout(40);
    await el.screenshot({{ path: await el.getAttribute('data-saida'), type: 'jpeg', quality: 93 }});
  }}
  await b.close();
}})();'''
    env = dict(os.environ, NODE_PATH=subprocess.run(['npm', 'root', '-g'], capture_output=True, text=True).stdout.strip())
    subprocess.run(['node', '-e', script], check=True, env=env)
    print('ok', SAIDA)


if __name__ == '__main__':
    gerar()
