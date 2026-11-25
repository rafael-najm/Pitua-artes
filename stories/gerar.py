"""
Gera os stories dos destaques do Instagram da Pituá (1080 x 1920) e as capas dos destaques (1080 x 1080).

Uso (na pasta do projeto):
    python3 stories/gerar.py

Precisa do Playwright com Chromium. Os textos ficam neste arquivo; as fotos vêm de src/assets.
As imagens saem em stories/saida/<destaque>/NN.jpg e stories/saida/capas/.
"""

import json
import shutil
import subprocess
from html import escape
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
PASTA = RAIZ / 'stories'
SAIDA = PASTA / 'saida'
BUILD = PASTA / '.build'
A = RAIZ / 'src' / 'assets'
FONTES = RAIZ / 'node_modules' / '@fontsource-variable'


def img(caminho):
    return (A / caminho).as_uri()


def peca(slug, n=1):
    return img(f'pecas/{slug}/{n:02d}.jpg')


LOGO = img('marca/pitua-logo.png')
LOGO_CLARO = img('marca/pitua-logo-escuro.png')

SETA = ('<svg viewBox="0 0 54 110" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round">'
        '<path d="M27 4v96M8 80l19 22 19-22"/></svg>')


# ————————————————————————————————————————————————— modelos de tela

def capa(foto, eyebrow, titulo, texto='', pos='50% 50%'):
    return f'''<section class="st capa">
  <img class="foto" src="{foto}" style="object-position:{pos}" alt="">
  <div class="topo"><img class="logo" src="{LOGO_CLARO}" alt="Pituá"></div>
  <div class="base">
    <p class="eyebrow">{eyebrow}</p>
    <h1 class="titulo">{titulo}</h1>
    {f'<p class="texto">{texto}</p>' if texto else ''}
  </div>
</section>'''


def peca_tela(foto, eyebrow, nome, resumo, pos='50% 50%', fundo=''):
    return f'''<section class="st peca {fundo}">
  <p class="eyebrow">{eyebrow}</p>
  <div class="moldura"><img src="{foto}" style="object-position:{pos}" alt=""></div>
  <h2 class="titulo">{nome}</h2>
  <p class="texto">{resumo}</p>
</section>'''


def foto_texto(foto, eyebrow, titulo, texto, chips=(), pos='50% 50%', fundo=''):
    ch = ''.join(f'<span>{escape(c)}</span>' for c in chips)
    return f'''<section class="st ft {fundo}">
  <div class="moldura"><img src="{foto}" style="object-position:{pos}" alt=""></div>
  <p class="eyebrow">{eyebrow}</p>
  <h2 class="titulo">{titulo}</h2>
  <p class="texto">{texto}</p>
  {f'<div class="chips">{ch}</div>' if ch else ''}
</section>'''


def lista(eyebrow, titulo, itens, fundo=''):
    lis = ''.join(f'<li><span class="num">{i + 1:02d}</span><div><h3>{escape(t)}</h3><p>{escape(d)}</p></div></li>'
                  for i, (t, d) in enumerate(itens))
    return f'''<section class="st lista {fundo}">
  <p class="eyebrow">{eyebrow}</p>
  <h2 class="titulo">{titulo}</h2>
  <ol>{lis}</ol>
</section>'''


def frase(texto, assina='', fundo='creme'):
    return f'''<section class="st frase {fundo}">
  <span class="aspas">“</span>
  <blockquote>{texto}</blockquote>
  {f'<p class="eyebrow assina">{assina}</p>' if assina else ''}
</section>'''


def grade(fotos, titulo, texto, fundo=''):
    fs = ''.join(f'<div><img src="{f}" style="object-position:{p}" alt=""><span>{escape(n)}</span></div>' for f, n, p in fotos)
    return f'''<section class="st grade {fundo}">
  <div class="fotos">{fs}</div>
  <h2 class="titulo">{titulo}</h2>
  <p class="texto">{texto}</p>
</section>'''


def cta(titulo, texto, chamada, infos=(), mini=None, fundo='azul'):
    inf = ''.join(f'<div>{escape(i)}</div>' for i in infos)
    m = f'<div class="peca-mini"><img src="{mini}" alt=""></div>' if mini else f'<img class="logo" src="{LOGO_CLARO if fundo in ("azul", "grafite") else LOGO}" alt="Pituá">'
    return f'''<section class="st cta {fundo}">
  {m}
  <h2 class="titulo">{titulo}</h2>
  <p class="texto">{texto}</p>
  {f'<div class="infos">{inf}</div>' if inf else ''}
  <div class="seta"><span>{chamada}</span>{SETA}</div>
</section>'''


def artista(foto, eyebrow, titulo, pos='50% 25%'):
    return f'''<section class="st capa artista">
  <img class="foto" src="{foto}" style="object-position:{pos}" alt="">
  <div class="base">
    <p class="eyebrow">{eyebrow}</p>
    <h1 class="titulo">{titulo}</h1>
  </div>
</section>'''


# ————————————————————————————————————————————————— conteúdo
# Cada destaque: (pasta, nome do destaque, capa, lista de telas, link sugerido para o adesivo)

DESTAQUES = [
    ('1-oficinas', 'Oficinas', ('editorial/oficina-tematica-prato.jpg', 0.585, 0.56, 0.80), [
        capa(img('editorial/oficina-aulas-travessa.jpg'), 'Oficinas', 'Aprenda a pintar <em>porcelana.</em>',
             'Aulas, workshops e encontros criativos com a orientação da Nathaly.', '50% 60%'),
        foto_texto(img('editorial/oficina-mob-aulas.jpg'), '<span class="n">01</span> · Aulas de pintura em porcelana',
                   'A sua peça, do primeiro traço ao <em>acabamento.</em>',
                   'Você escolhe a peça, o desenho e as cores, e pinta tudo com a orientação da artista.',
                   ['Aulas semanais', '3 horas por aula', 'Turma recorrente'], '40% 50%'),
        foto_texto(peca('bomboniere-arlequim', 1), '<span class="n">02</span> · Oficina criativa',
                   'Um projeto novo a cada <em>encontro.</em>',
                   'Porcelana, vidro, decoupage, dobraduras e muito mais: uma técnica e uma descoberta a cada semana.',
                   ['Aulas semanais', '3 horas por aula'], '50% 45%'),
        foto_texto(peca('petisqueira-geometrica', 1), '<span class="n">03</span> · Workshops',
                   'Do começo ao fim, em 2 a 4 <em>aulas.</em>',
                   'Um projeto escolhido, com o passo a passo guiado pela artista, para terminar com a peça pronta.',
                   ['Projeto definido', '2, 3 ou 4 aulas'], '50% 50%'),
        foto_texto(img('editorial/oficina-tematica-prato.jpg'), '<span class="n">04</span> · Oficinas temáticas',
                   'Para aniversários, grupos e <em>empresas.</em>',
                   'O tema, a peça e o formato são definidos junto com você.',
                   ['Sob medida', 'Grupos e eventos'], '50% 60%'),
        frase('Um aprendizado contínuo, no seu ritmo: a cada peça, mais técnica e mais <em>segurança no pincel.</em>',
              'Oficinas Pituá', 'creme'),
        cta('Quer saber das próximas <em>turmas?</em>', 'Toque no link e fale com a gente. Contamos dias, horários e como funciona.',
            'Toque no link', mini=img('editorial/oficina-mob-workshops.jpg')),
    ], 'https://pituaartes.com.br/oficinas/'),

    ('2-acervo', 'Acervo', ('editorial/hero-araras.jpg', 0.36, 0.48, 0.58), [
        capa(img('editorial/hero-araras.jpg'), 'Acervo', 'Peças únicas, pintadas <em>à mão.</em>',
             'Inspire-se! Cada uma pode virar a ideia para a sua encomenda.', '35% 50%'),
        peca_tela(peca('elefante-real', 1), 'Acervo · <span class="n">01</span>', 'Elefante Real',
                  'Manta em rosa e ouro, pingentes em verde-esmeralda.'),
        peca_tela(peca('bule-camelo', 1), 'Acervo · <span class="n">02</span>', 'Bule Camelo',
                  'Um camelo de manta bordada em laranja, turquesa e ouro.', fundo='creme'),
        peca_tela(peca('vaso-peixes', 1), 'Acervo · <span class="n">03</span>', 'Vaso Peixes',
                  'Peixes tropicais em um mosaico de cores.'),
        peca_tela(peca('anfora-cisnes', 1), 'Acervo · <span class="n">04</span>', 'Ânfora Cisnes',
                  'Cena romântica, azul-cobalto e alças de cisne.', fundo='creme'),
        peca_tela(peca('potiche-tulipa', 1), 'Acervo · <span class="n">05</span>', 'Potiche Tulipa',
                  'Uma grande tulipa sobre xadrez laranja e poás verdes.'),
        grade([(peca('globo', 1), 'Globo', '50% 50%'), (peca('vaso-pavao-persa', 1), 'Vaso Pavão Persa', '50% 50%'),
               (peca('gato-paisley', 1), 'Gato Paisley', '50% 50%'), (peca('jardineira-mata-atlantica', 1), 'Jardineira Mata Atlântica', '50% 50%')],
              'E muito mais no <em>acervo.</em>', '66 peças para inspirar a sua: vasos, mesa posta, Judaica, decoração…'),
        cta('Gostou de alguma <em>peça?</em>', 'Ela pode inspirar a sua. Veja o acervo completo no site.', 'Toque no link',
            mini=peca('vaso-carmim', 1), fundo='grafite'),
    ], 'https://pituaartes.com.br/acervo/'),

    ('3-encomendas', 'Encomendas', ('editorial/faixa-cachepo-elefante.jpg', 0.5, 0.52, 0.80), [
        capa(img('editorial/frente-encomendas-elefante.jpg'), 'Encomendas', 'Arte sob <em>encomenda.</em>',
             'Uma peça criada a partir da sua história.', '50% 45%'),
        lista('Como funciona', 'Do seu jeito, do começo ao <em>fim.</em>', [
            ('Conversa', 'Você conta a ideia, a ocasião e o lugar da peça. Fotos e referências são bem-vindas.'),
            ('Desenho', 'A artista propõe a composição e as cores. A pintura só começa quando estiver do seu jeito.'),
            ('Pintura', 'Tudo é pintado à mão, camada por camada, com o tempo que cada detalhe pede.'),
            ('Entrega', 'A peça é embalada com cuidado e entregue no prazo combinado.'),
        ]),
        grade([(img('personalizar/caneca-afeto.webp'), 'Caneca', '50% 50%'), (img('personalizar/moringa-faixa.webp'), 'Moringa', '50% 50%'),
               (img('personalizar/vela-copo-porcelana.webp'), 'Vela', '50% 50%'), (img('personalizar/porta-joias-do-dia.webp'), 'Porta-joias', '50% 50%')],
              'Escolha a peça. <em>A arte é sua.</em>', 'Peças em porcelana branca que recebem uma pintura criada a partir da sua ideia.',
              fundo='creme'),
        foto_texto(peca('cuba-baloes', 1), 'Projetos sob medida', 'Da mesa de jantar ao <em>lavabo.</em>',
                   'Aparelhos de jantar, travessas, peças de Judaica, cubas de banheiro: criados do zero, para a sua casa.',
                   pos='50% 50%'),
        foto_texto(peca('prato-de-shabat', 1), 'A história por trás da peça', 'Paz, Salam, <em>Shalom.</em>',
                   'O avô da Nathaly deixou uma folha com três palavras. Ela virou o prato de Shabat da família, que recebe as chalot toda sexta-feira.',
                   pos='50% 50%', fundo='creme'),
        cta('Vamos criar a <em>sua?</em>', 'Conte a sua ideia: a gente responde com um desenho feito para você.', 'Toque no link',
            mini=peca('vaso-carmim', 2)),
    ], 'https://pituaartes.com.br/encomendas/'),

    ('4-eventos-e-brindes', 'Eventos & Brindes', ('eventos/hero-pratinhos.webp', 0.52, 0.205, 0.39), [
        capa(img('eventos/hero-pratinhos.webp'), 'Eventos &amp; Brindes', 'Lembranças pintadas <em>à mão.</em>',
             'Para casamentos, eventos pessoais e marcas.', '50% 50%'),
        lista('Para quem', 'Um desenho exclusivo para cada <em>celebração.</em>', [
            ('Casamentos', 'Lembranças para os convidados, padrinhos, madrinhas e as peças especiais dos noivos.'),
            ('Eventos pessoais', 'Bar e bat mitzvá, 15 anos, aniversários, chá de bebê, bodas.'),
            ('Marcas e empresas', 'Brindes de fim de ano, kits de boas-vindas, lançamentos e eventos.'),
        ], fundo='azul'),
        foto_texto(img('eventos/convidados-vela.webp'), 'Para os convidados', 'A lembrança que vai para <em>casa.</em>',
                   'Velas, copinhos, porta-joias e pratinhos com o desenho da sua festa.', pos='50% 50%'),
        foto_texto(img('eventos/bar-brinde-garrafa-tacas.webp'), 'Bar e brinde', 'Taças, copos e garrafas pintados à <em>mão.</em>',
                   'Para o brinde dos noivos, o bar e a mesa de honra.', pos='50% 50%', fundo='creme'),
        foto_texto(img('eventos/mesa-vasinho.webp'), 'Mesa e decoração', 'A decoração que vira <em>presente.</em>',
                   'Vasinhos, porta-velas e marcadores de lugar que enfeitam a festa e vão embora com os convidados.', pos='50% 50%'),
        foto_texto(img('eventos/anfitrioes-aparelho.jpg'), 'Noivos, padrinhos e anfitriões', 'As peças que ficam para a <em>vida.</em>',
                   'Pratos, travessas, kits de Shabat e peças que passam a fazer parte da história da família.', pos='50% 50%', fundo='creme'),
        cta('Vamos criar as lembranças do seu <em>evento?</em>', 'Em porcelana ou vidro, com um desenho criado para a sua festa ou para a sua marca.',
            'Toque no link', infos=['Pedido mínimo: 20 peças', 'Orçamento sem compromisso'], mini=img('eventos/hero-pratinhos.webp')),
    ], 'https://pituaartes.com.br/eventos/'),

    ('5-a-artista', 'A artista', ('editorial/artista-retrato.jpg', 0.36, 0.34, 0.58), [
        artista(img('editorial/artista-retrato.jpg'), 'A artista', 'Prazer, eu sou a <em>Nathaly.</em>'),
        foto_texto(img('editorial/0Q2A5604.jpg'), 'Desde os 11 anos', 'Por trás de cada peça, as mesmas <em>mãos.</em>',
                   'Apaixonada por pintura em porcelana, a Nathaly acompanha cada peça do primeiro desenho à última pincelada.',
                   pos='50% 30%', fundo='creme'),
        frase('Toda peça começa em branco. Depois vêm o desenho, o pincel e as camadas de cor, até a porcelana virar <em>obra.</em>',
              'Nathaly · Pituá', 'azul'),
        foto_texto(img('editorial/hero-tucano.jpg'), 'Um universo de cores', 'As cores do Brasil e padrões do <em>mundo.</em>',
                   'Araras, tucanos, arabescos persas, azulejos, flores de todos os jardins e muitas histórias de família.', pos='50% 40%'),
        cta('Vamos <em>conversar?</em>', 'Oficinas, encomendas e lembranças para eventos: tudo começa com uma conversa.', 'Toque no link',
            mini=img('editorial/artista-retrato.jpg'), fundo='grafite'),
    ], 'https://pituaartes.com.br/'),
]


def gerar():
    fontes = f'''
    @font-face {{ font-family: 'Newsreader'; font-style: normal; font-weight: 200 800;
      src: url('{(FONTES / 'newsreader/files/newsreader-latin-wght-normal.woff2').as_uri()}') format('woff2'); }}
    @font-face {{ font-family: 'Newsreader'; font-style: italic; font-weight: 200 800;
      src: url('{(FONTES / 'newsreader/files/newsreader-latin-wght-italic.woff2').as_uri()}') format('woff2'); }}
    @font-face {{ font-family: 'Jost'; font-style: normal; font-weight: 100 900;
      src: url('{(FONTES / 'jost/files/jost-latin-wght-normal.woff2').as_uri()}') format('woff2'); }}
    '''
    css = (PASTA / 'estilo.css').read_text(encoding='utf-8')
    partes, plano = [], []
    BUILD.mkdir(parents=True, exist_ok=True)
    from PIL import Image
    for pasta, nome, (cfoto, cx, cy, tam), telas, link in DESTAQUES:
        # capa do destaque: um detalhe da pintura, recortado em quadrado (o Instagram mostra o centro em círculo)
        im = Image.open(A / cfoto).convert('RGB')
        lado = tam * min(im.size)
        x0 = min(max(cx * im.width - lado / 2, 0), im.width - lado)
        y0 = min(max(cy * im.height - lado / 2, 0), im.height - lado)
        recorte = BUILD / f'capa-{pasta}.jpg'
        im.crop((int(x0), int(y0), int(x0 + lado), int(y0 + lado))).resize((1080, 1080), Image.LANCZOS).save(recorte, quality=95)
        partes.append(f'<div class="capa-destaque" data-saida="capas/{pasta}.jpg">'
                      f'<img src="{recorte.as_uri()}" alt=""></div>')
        for i, t in enumerate(telas, 1):
            partes.append(t.replace('<section class="st', f'<section data-saida="{pasta}/{i:02d}.jpg" class="st', 1))
        plano.append({'pasta': pasta, 'nome': nome, 'telas': len(telas), 'link': link})
    BUILD.mkdir(parents=True, exist_ok=True)
    html = (f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><style>{fontes}{css}</style></head>'
            f'<body>{"".join(partes)}</body></html>')
    arq = BUILD / 'stories.html'
    arq.write_text(html, encoding='utf-8')
    if SAIDA.exists():
        shutil.rmtree(SAIDA)
    SAIDA.mkdir(parents=True)
    script = f'''
const {{ chromium }} = require('playwright');
const path = require('path'); const fs = require('fs');
(async () => {{
  const b = await chromium.launch();
  const p = await b.newPage({{ viewport: {{ width: 1080, height: 1920 }}, deviceScaleFactor: 1 }});
  await p.goto({json.dumps(arq.as_uri())}, {{ waitUntil: 'load' }});
  await p.evaluate(() => document.fonts.ready);
  const els = await p.$$('[data-saida]');
  for (const el of els) {{
    const rel = await el.getAttribute('data-saida');
    const out = path.join({json.dumps(str(SAIDA))}, rel);
    fs.mkdirSync(path.dirname(out), {{ recursive: true }});
    await el.evaluate(e => e.scrollIntoView({{ block: 'start' }}));
    await p.waitForTimeout(60);
    await el.screenshot({{ path: out, type: 'jpeg', quality: 92 }});
  }}
  await b.close();
}})();'''
    subprocess.run(['node', '-e', script], check=True, cwd=BUILD)
    (SAIDA / 'plano.json').write_text(json.dumps(plano, ensure_ascii=False, indent=1), encoding='utf-8')
    print('ok', sum(p['telas'] for p in plano), 'stories e', len(plano), 'capas em', SAIDA)


if __name__ == '__main__':
    gerar()
