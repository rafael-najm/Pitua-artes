# Pitua · Arte em porcelana

Site-portfólio da Pitua: acervo de peças pintadas à mão, encomendas personalizadas e oficinas criativas.

Feito com [Astro](https://astro.build) — gera um site estático, rápido e leve, com as fotos otimizadas automaticamente (WebP em vários tamanhos).

## Páginas

| Página | Endereço | O que tem |
| --- | --- | --- |
| Início | `/` | Abertura, "O que acontece por aqui", destaques, vídeos de uso, a história do Prato de Shabat, a artista e chamada para encomendas |
| Acervo | `/acervo/` | Todas as peças, com filtro por categoria |
| Peça | `/acervo/<nome-da-peca>/` | Galeria com zoom, descrição, botão "Consultar disponibilidade" (WhatsApp) e "Encomendar uma peça inspirada" |
| Encomendas | `/encomendas/` | O que dá para encomendar, como funciona, formulário que abre o WhatsApp com a mensagem pronta e perguntas frequentes |
| Oficinas | `/oficinas/` | Oficinas criativas e oficinas especiais |

## ✏️ Antes de publicar: preencha os contatos

Abra `src/data/site.ts` e preencha:

```ts
whatsapp: '5521999998888', // DDI + DDD + número, só dígitos
instagram: 'pitua.artes',  // sem @
email: 'contato@pitua.com.br',
artista: 'Nome da Artista', // opcional — aparece na seção "A artista"
```

Enquanto o WhatsApp estiver vazio, os botões abrem o WhatsApp com a mensagem pronta para a pessoa escolher o contato.
Instagram e e-mail só aparecem quando preenchidos.

**Revise também os textos.** As descrições das peças foram escritas a partir das fotos — confira nomes, técnicas e detalhes em `src/data/pecas.ts`. A história do Prato de Shabat foi transcrita do vídeo em que a artista conta a história.

## Como adicionar ou editar uma peça

1. Crie uma pasta em `src/assets/pecas/<nome-da-peca>/` (minúsculas, com hífens, sem acentos — ex.: `vaso-azul`).
2. Coloque as fotos como `01.jpg`, `02.jpg`… A `01` é a capa; a `02` aparece quando o mouse passa por cima do card.
   Fotos com até ~2200 px no maior lado são suficientes.
3. Acrescente a peça na lista em `src/data/pecas.ts`:

```ts
{
  slug: 'vaso-azul',            // igual ao nome da pasta
  nome: 'Vaso Azul',
  categoria: 'decoracao',       // mesa | decoracao | judaica | telas | sob-medida
  resumo: 'Uma linha curta que aparece no card.',
  descricao: ['Primeiro parágrafo.', 'Segundo parágrafo (opcional).'],
  destaque: true,               // opcional: aparece na página inicial
  video: 'nome-do-video',       // opcional: arquivo em public/video/nome-do-video.mp4 (+ .jpg de capa)
},
```

## Rodar no computador

Precisa do [Node.js](https://nodejs.org) 22 (versão 22.23.4 ou mais nova).

```bash
npm install
```

```bash
npm run dev
```

O site abre em http://localhost:4321. Para gerar a versão final (pasta `dist/`):

```bash
npm run build
```

## Publicar

**GitHub Pages (grátis, já configurado):** o arquivo `.github/workflows/deploy.yml` publica o site a cada push na branch `main`.
Na primeira vez, vá em *Settings → Pages* do repositório e escolha **Source: GitHub Actions**.
O endereço fica `https://<usuario>.github.io/<repositorio>/`.

**Domínio próprio (ex.: pitua.com.br):** em `deploy.yml`, troque `SITE_URL` pelo domínio e `BASE_PATH` por `/`, e configure o domínio em *Settings → Pages*.

**Vercel ou Netlify:** importe o repositório; o Astro é detectado automaticamente (comando `npm run build`, pasta `dist`). Defina a variável `SITE_URL` com o endereço final.

## Estrutura

```
src/
  data/site.ts        contatos e textos gerais
  data/pecas.ts       o acervo (nomes, categorias, descrições)
  assets/pecas/       fotos de cada peça (uma pasta por peça)
  assets/editorial/   retratos e fotos de ambiente
  pages/              as páginas do site
  components/         cabeçalho, rodapé, card de peça
  styles/global.css   cores, tipografia e estilos gerais
public/video/         vídeos (MP4 leves) e imagens de capa dos vídeos
```

Fotos e vídeos: ensaio profissional da Pitua. Tipografia: Newsreader e Jost (licença SIL Open Font).
