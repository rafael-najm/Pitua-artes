"""
Gera o PDF "Pituá · Eventos & Brindes" (apresentação para cerimonialistas e marcas).

Uso (na pasta do projeto):
    python3 catalogo/gerar.py

Precisa de: Pillow e segno (pip install pillow segno) e do Playwright com Chromium.
Os textos ficam neste arquivo; as fotos vêm de src/assets. O PDF sai em
catalogo/Pitua-Eventos-e-Brindes.pdf
"""

import json
import subprocess
import urllib.parse
from html import escape
from pathlib import Path

import segno
from PIL import Image, ImageOps

RAIZ = Path(__file__).resolve().parent.parent
PASTA = RAIZ / 'catalogo'
BUILD = PASTA / '.build'
SAIDA = PASTA / 'Pitua-Eventos-e-Brindes.pdf'
ASSETS = RAIZ / 'src' / 'assets'
FONTES = RAIZ / 'node_modules' / '@fontsource-variable'

WHATSAPP = '5521968843029'
WHATSAPP_TXT = '(21) 96884-3029'
INSTAGRAM = 'pituaartes'
EMAIL = 'contato@pituaartes.com.br'
SITE = 'pituaartes.com.br'


def zap(msg: str) -> str:
    return f'https://wa.me/{WHATSAPP}?text={urllib.parse.quote(msg)}'


# ————————————————————————————————————————————————————————————— fotos

def prepara(origem: Path, nome: str, lado=1600, quadrado=False, foco=(0.5, 0.5)) -> str:
    """Reduz a foto (para o PDF ficar leve) e devolve o caminho file://."""
    BUILD.mkdir(parents=True, exist_ok=True)
    destino = BUILD / f'{nome}.jpg'
    im = ImageOps.exif_transpose(Image.open(origem)).convert('RGB')
    if quadrado:
        im = ImageOps.fit(im, (lado, lado), Image.LANCZOS, centering=foco)
    else:
        im.thumbnail((lado, lado), Image.LANCZOS)
    im.save(destino, quality=82, optimize=True, progressive=True)
    return destino.as_uri()


def peca(slug: str, n=1) -> Path:
    return sorted((ASSETS / 'pecas' / slug).glob(f'{n:02d}.*'))[0]


# ————————————————————————————————————————————————————————————— conteúdo

publicos = [
    ('Casamentos', 'Lembranças para os convidados, presentes para padrinhos e madrinhas e as peças especiais dos noivos, '
                   'com a pintura inspirada na decoração do casamento.'),
    ('Eventos pessoais', 'Bar e bat mitzvá, 15 anos, aniversários, chá de bebê, bodas, com um desenho que conversa com o '
                         'tema e as cores da festa.'),
    ('Marcas e empresas', 'Brindes de fim de ano, kits de boas-vindas, lançamentos e eventos corporativos, com uma pintura '
                          'criada a partir da identidade visual da marca.'),
]

blocos = [
    dict(rotulo='Para os convidados', titulo='A lembrança que vai para casa.',
         texto='Peças pequenas, pintadas uma a uma, com um desenho exclusivo que repete as flores, as cores ou os '
               'elementos da decoração. Cada convidado leva um pedacinho do evento.',
         itens=['Porta-joias do dia', 'Copinho', 'Vela em copo de porcelana', 'Pratinho de doces'],
         img=ASSETS / 'eventos' / 'convidados-vela.webp'),
    dict(rotulo='Bar e brinde', titulo='Taças, copos e garrafas pintados à mão.',
         texto='O vidro aparece no brinde, no bar e nas fotos. Taças dos noivos e dos padrinhos, copos para o open bar '
               'que o convidado leva para casa e garrafas personalizadas para a mesa de honra.',
         itens=['Taças de vinho e espumante', 'Taças de gin e copos long drink', 'Garrafas de espumante personalizadas',
                'Mini espumantes (187 ml)', 'Garrafa de vinho “para abrir no 1º aniversário”'],
         img=ASSETS / 'eventos' / 'bar-brinde-garrafa-tacas.webp'),
    dict(rotulo='Mesa e decoração', titulo='A decoração que vira presente.',
         texto='Centros de mesa, porta-velas e marcadores de lugar pintados à mão no mesmo desenho da festa, que '
               'enfeitam o evento e, no fim, vão embora com os convidados.',
         itens=['Porta-velas e lanternas', 'Vasinhos para flores', 'Marcadores de lugar',
                'Placa ou espelho de boas-vindas', 'Potes com tampa para bem-casados e doces'],
         img=ASSETS / 'eventos' / 'mesa-vasinho.webp'),
    dict(rotulo='Noivos, padrinhos e anfitriões', titulo='As peças que ficam para a vida.',
         texto='Presentes principais, desenhados com calma: pratos com monograma, kits de Shabat, travessas e peças '
               'que passam a fazer parte da história da família.',
         itens=['Prato com monograma dos noivos', 'Kit de Shabat', 'Castiçais para as velas de Shabat',
                'Peça para guardar o copo quebrado no casamento', 'Travessas e aparelhos personalizados'],
         img=ASSETS / 'eventos' / 'anfitrioes-aparelho.jpg', foco=(0.5, 0.5)),
]

passos = [
    ('Conversa', 'Você conta o evento, a quantidade e mostra a decoração: convite, paleta, flores, identidade visual.'),
    ('Desenho e amostra', 'A artista cria um desenho exclusivo, combinando com a festa ou a marca, e pinta uma '
                          'peça-amostra para aprovação.'),
    ('Produção', 'Com tudo aprovado, as peças são pintadas à mão, uma a uma, e finalizadas.'),
    ('Embalagem e entrega', 'Embaladas com cuidado, com caixinha, tag e fita, se quiser, e entregues no prazo '
                            'combinado.'),
]

informacoes = [
    ('Pedido mínimo', '20 peças'),
    ('Materiais', 'Porcelana ou vidro pintado à mão'),
    ('Desenho', 'Exclusivo, criado para cada evento ou marca'),
    ('Orçamento', 'Sob medida e sem compromisso'),
]

vantagens = [
    'Atendimento prioritário para os seus clientes',
    'Catálogo para apresentar aos noivos e anfitriões',
    'Kit de amostras para o seu ateliê',
]

acervo = [
    ('À mesa', 'Peças de servir, vidro pintado e louças com desenhos que vão do clássico ao tropical.', [
        ('copos-pintados', 'Copos Pintados', 'Vidro'),
        ('bomboniere-arlequim', 'Bomboniere Arlequim', 'Vidro'),
        ('jarra-olho-grego', 'Jarra Olho Grego', 'Porcelana'),
        ('manteigueira-borboletas', 'Manteigueira Borboletas', 'Porcelana'),
        ('queijeira-hibisco', 'Queijeira Hibisco', 'Porcelana'),
        ('boleira-confeitaria', 'Boleira Confeitaria', 'Porcelana'),
    ]),
    ('Decoração e peças especiais', 'Vasos, esculturas e peças judaicas com pintura detalhada, feitas para durar '
                                    'gerações.', [
        ('vaso-carmim', 'Vaso Carmim', 'Porcelana'),
        ('vasos-orquideas', 'Vasos Orquídeas', 'Porcelana'),
        ('elefante-real', 'Elefante Real', 'Porcelana'),
        ('relogio-imari', 'Relógio Imari', 'Porcelana'),
        ('casticais-shabat-shalom', 'Castiçais Shabat Shalom', 'Porcelana'),
        ('cachepo-elefante-indiano', 'Cachepô Elefante Indiano', 'Porcelana'),
    ]),
]

# Ajuste do recorte quadrado de algumas fotos (0 = topo/esquerda, 1 = base/direita)
FOCO = {'copos-pintados': (0.5, 0.35)}

# ————————————————————————————————————————————————————————————— montagem

def ul(itens):
    return '<ul class="ideias">' + ''.join(f'<li>{escape(i)}</li>' for i in itens) + '</ul>'


def rodape(n):
    return f'<footer class="pg-rodape"><span>Pituá · Eventos &amp; Brindes</span><span>{n:02d}</span></footer>'


def gerar_html():
    logo = (ASSETS / 'marca' / 'pitua-logo.png').as_uri()
    logo_escuro = (ASSETS / 'marca' / 'pitua-logo-escuro.png').as_uri()
    hero = prepara(ASSETS / 'eventos' / 'hero-pratinhos.webp', 'hero', lado=1400, quadrado=True)
    artista = prepara(ASSETS / 'editorial' / 'artista-retrato.jpg', 'artista', lado=1200)

    link_orcamento = zap('Olá! Vi a apresentação de Eventos & Brindes da Pituá e gostaria de um orçamento. (Catálogo PDF)')
    link_cer = zap('Olá! Sou cerimonialista, vi a apresentação de Eventos & Brindes e gostaria de conhecer a parceria. (Catálogo PDF)')
    link_marca = zap('Olá! Vi a apresentação de Eventos & Brindes e gostaria de um orçamento de brindes para a minha empresa. (Catálogo PDF)')
    qr = segno.make(link_orcamento, error='m')
    qr_svg = qr.svg_inline(scale=4, dark='#174b83', light=None, border=0)

    paginas = []
    n = 1

    # 1. capa
    paginas.append(f'''
    <section class="pg capa">
      <div class="capa-txt">
        <img class="logo" src="{logo}" alt="Pituá">
        <div>
          <p class="eyebrow">Eventos &amp; Brindes</p>
          <h1 class="display">Lembranças<br><em>pintadas à mão.</em></h1>
          <p class="lede">Para casamentos, eventos pessoais e marcas: peças em porcelana ou vidro com um desenho
          criado para combinar com a decoração da festa ou com a identidade visual da marca.</p>
        </div>
        <p class="capa-site">{SITE}</p>
      </div>
      <div class="capa-img"><img src="{hero}" alt=""></div>
    </section>''')
    n += 1

    # 2. para quem + material
    cards = ''.join(
        f'<article class="publico"><span class="num">{i + 1:02d}</span><h3>{escape(t)}</h3><p>{escape(d)}</p></article>'
        for i, (t, d) in enumerate(publicos))
    paginas.append(f'''
    <section class="pg pq">
      <header class="pg-head">
        <p class="eyebrow">Para quem</p>
        <h2 class="h2">Um desenho exclusivo <em>para cada celebração.</em></h2>
      </header>
      <div class="publicos">{cards}</div>
      <div class="material">
        <p class="eyebrow">Porcelana ou vidro</p>
        <p>Os brindes podem ser em <strong>porcelana</strong> ou em <strong>vidro pintado à mão</strong>, sempre com
        um <strong>desenho exclusivo</strong>, criado para combinar com a decoração da festa ou com a identidade
        visual da marca.</p>
      </div>
      {rodape(n)}
    </section>''')
    n += 1

    # 3–6. blocos de ideias
    for i, b in enumerate(blocos):
        img = prepara(b['img'], f'bloco{i}', lado=1400, quadrado=True, foco=b.get('foco', (0.5, 0.5)))
        rev = ' rev' if i % 2 else ''
        paginas.append(f'''
    <section class="pg bloco{rev}">
      <div class="bloco-img"><img src="{img}" alt=""></div>
      <div class="bloco-txt">
        <p class="eyebrow"><span class="idx">Ideias {i + 1:02d}/04</span> · {escape(b['rotulo'])}</p>
        <h2 class="h2">{escape(b['titulo'])}</h2>
        <p class="body">{escape(b['texto'])}</p>
        {ul(b['itens'])}
      </div>
      {rodape(n)}
    </section>''')
        n += 1

    # 7. como funciona (escura)
    lis = ''.join(f'<li><span class="num">{i + 1:02d}</span><h3>{escape(t)}</h3><p>{escape(d)}</p></li>'
                  for i, (t, d) in enumerate(passos))
    infos = ''.join(f'<div><dt>{escape(t)}</dt><dd>{escape(d)}</dd></div>' for t, d in informacoes)
    paginas.append(f'''
    <section class="pg escura processo">
      <header class="pg-head">
        <p class="eyebrow">Como funciona</p>
        <h2 class="h2">Do convite à última embalagem.</h2>
      </header>
      <ol class="passos">{lis}</ol>
      <dl class="infos">{infos}</dl>
      {rodape(n)}
    </section>''')
    n += 1

    # 8. cerimonialistas e marcas
    vant = ''.join(f'<li>{escape(v)}</li>' for v in vantagens)
    paginas.append(f'''
    <section class="pg parceria">
      <div class="par-col">
        <p class="eyebrow">Para cerimonialistas</p>
        <h2 class="h2">Uma parceira para os seus eventos.</h2>
        <p class="body">Lembranças exclusivas, pintadas à mão, para encantar os seus clientes, com atendimento próximo
        do primeiro desenho até a entrega.</p>
        <ul class="ideias">{vant}</ul>
        <a class="link" href="{link_cer}">Quero ser parceira <span>→</span></a>
      </div>
      <div class="par-col par-marcas">
        <p class="eyebrow">Para marcas e empresas</p>
        <h2 class="h2">Brindes com a cara da sua marca.</h2>
        <p class="body">Copos, taças, garrafas, canecas e kits de presente com uma pintura criada a partir da
        identidade visual da marca, para clientes, equipes, fim de ano e lançamentos.</p>
        <ul class="ideias">
          <li>Brindes de fim de ano</li><li>Kits de boas-vindas</li><li>Lançamentos e eventos corporativos</li>
        </ul>
        <a class="link" href="{link_marca}">Falar sobre brindes corporativos <span>→</span></a>
      </div>
      {rodape(n)}
    </section>''')
    n += 1

    # 9. a artista
    paginas.append(f'''
    <section class="pg artista">
      <div class="art-img"><img src="{artista}" alt=""></div>
      <div class="art-txt">
        <p class="eyebrow">A artista</p>
        <h2 class="h2">Por trás de cada peça, as mesmas mãos.</h2>
        <p class="body">Nathaly é apaixonada por pintura em porcelana desde os 11 anos e, de lá pra cá, nunca mais
        parou. Na Pituá, cada peça passa pelas mãos dela, do primeiro desenho à última pincelada: um trabalho paciente
        e detalhista, que mistura as cores do Brasil, padrões do mundo inteiro e muitas histórias de família.</p>
        <blockquote>Toda peça começa em branco. Depois vêm o desenho, o pincel e as camadas de cor, até a porcelana
        virar <em>obra</em>.</blockquote>
      </div>
      {rodape(n)}
    </section>''')
    n += 1

    # 10–11. do acervo
    for k, (titulo, sub, pecas) in enumerate(acervo):
        figs = ''
        for slug, nome, mat in pecas:
            src = prepara(peca(slug), f'acervo-{slug}', lado=800, quadrado=True, foco=FOCO.get(slug, (0.5, 0.5)))
            figs += f'<figure><img src="{src}" alt=""><figcaption>{escape(nome)}<span>{mat}</span></figcaption></figure>'
        paginas.append(f'''
    <section class="pg acervo">
      <header class="ac-head">
        <p class="eyebrow">Do acervo · {k + 1:02d}/02</p>
        <h2 class="h2">{escape(titulo)}</h2>
        <p class="body">{escape(sub)}</p>
        <p class="nota">Peças do acervo da Pituá, para dar ideia do que a pintura à mão é capaz de fazer. Mais peças
        em <a href="https://{SITE}/acervo/">{SITE}/acervo</a>.</p>
      </header>
      <div class="grade">{figs}</div>
      {rodape(n)}
    </section>''')
        n += 1

    # 12. contato
    paginas.append(f'''
    <section class="pg escura contato">
      <div class="ct-txt">
        <img class="logo" src="{logo_escuro}" alt="Pituá">
        <h2 class="h2">Vamos criar as lembranças <em>do seu próximo evento?</em></h2>
        <p class="body">Conte a data, a quantidade e mostre a decoração ou a identidade da marca. A gente responde com
        ideias e um orçamento sob medida.</p>
        <dl class="contatos">
          <div><dt>WhatsApp</dt><dd><a href="{link_orcamento}">{WHATSAPP_TXT}</a></dd></div>
          <div><dt>Instagram</dt><dd><a href="https://instagram.com/{INSTAGRAM}">@{INSTAGRAM}</a></dd></div>
          <div><dt>E-mail</dt><dd><a href="mailto:{EMAIL}">{EMAIL}</a></dd></div>
          <div><dt>Site</dt><dd><a href="https://{SITE}/eventos/">{SITE}/eventos</a></dd></div>
        </dl>
      </div>
      <a class="qr" href="{link_orcamento}">
        <div class="qr-box">{qr_svg}</div>
        <p>Aponte a câmera para<br>pedir um orçamento</p>
      </a>
    </section>''')

    fontes = f'''
    @font-face {{ font-family: 'Newsreader'; font-style: normal; font-weight: 200 800;
      src: url('{(FONTES / 'newsreader/files/newsreader-latin-wght-normal.woff2').as_uri()}') format('woff2'); }}
    @font-face {{ font-family: 'Newsreader'; font-style: italic; font-weight: 200 800;
      src: url('{(FONTES / 'newsreader/files/newsreader-latin-wght-italic.woff2').as_uri()}') format('woff2'); }}
    @font-face {{ font-family: 'Jost'; font-style: normal; font-weight: 100 900;
      src: url('{(FONTES / 'jost/files/jost-latin-wght-normal.woff2').as_uri()}') format('woff2'); }}
    '''
    css = (PASTA / 'estilo.css').read_text(encoding='utf-8')
    html = f'''<!doctype html>
<html lang="pt-BR"><head><meta charset="utf-8"><title>Pituá · Eventos &amp; Brindes</title>
<style>{fontes}{css}</style></head>
<body>{''.join(paginas)}</body></html>'''
    arq = BUILD / 'catalogo.html'
    arq.write_text(html, encoding='utf-8')
    return arq


def gerar_pdf(html: Path):
    script = f'''
const {{ chromium }} = require('playwright');
(async () => {{
  const b = await chromium.launch();
  const p = await b.newPage();
  await p.goto({json.dumps(html.as_uri())}, {{ waitUntil: 'load' }});
  await p.evaluate(() => document.fonts.ready);
  await p.pdf({{ path: {json.dumps(str(SAIDA))}, width: '1280px', height: '720px', printBackground: true,
                 margin: {{ top: 0, right: 0, bottom: 0, left: 0 }} }});
  await b.close();
}})();'''
    subprocess.run(['node', '-e', script], check=True, cwd=BUILD)


if __name__ == '__main__':
    gerar_pdf(gerar_html())
    print(SAIDA, f'{SAIDA.stat().st_size / 1e6:.1f} MB')
