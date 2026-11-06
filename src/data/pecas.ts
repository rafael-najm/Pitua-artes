/**
 * ACERVO
 * ------
 * Cada peça tem uma pasta de fotos em `src/assets/pecas/<slug>/`.
 * As fotos são exibidas em ordem alfabética (01.jpg, 02.jpg…); a primeira é a capa.
 *
 * Para adicionar uma peça: crie a pasta com as fotos e acrescente um item nesta lista.
 */

export type Categoria = 'mesa' | 'decoracao' | 'judaica' | 'telas' | 'sob-medida';

export const categorias: Record<Categoria, string> = {
  mesa: 'Mesa posta',
  decoracao: 'Decoração',
  judaica: 'Judaica',
  telas: 'Telas',
  'sob-medida': 'Sob medida',
};

export interface Peca {
  slug: string;
  nome: string;
  categoria: Categoria;
  /** Uma linha, aparece no card e abaixo do título. */
  resumo: string;
  /** Texto da página da peça. Cada item é um parágrafo. */
  descricao: string[];
  /** Vídeo vertical em /public/video (sem extensão). */
  video?: string;
  /** Aparece na vitrine da página inicial. */
  destaque?: boolean;
  /** Mostra o selo "Projeto sob encomenda". */
  encomenda?: boolean;
}

export const pecas: Peca[] = [
  // ——— Decoração ———
  {
    slug: 'jardineira-mata-atlantica',
    nome: 'Jardineira Mata Atlântica',
    categoria: 'decoracao',
    resumo: 'Araras-azuis, tucano e papagaios entre folhagens tropicais.',
    descricao: [
      'Uma floresta inteira contornando a porcelana. Araras-azuis, tucano, papagaio e borboletas surgem entre folhagens e cipós, pintados com riqueza de detalhes.',
      'As bordas em ouro emolduram a cena e dão à jardineira a presença de uma peça de coleção.',
    ],
    destaque: true,
  },
  {
    slug: 'elefante-real',
    nome: 'Elefante Real',
    categoria: 'decoracao',
    resumo: 'Manta em rosa e ouro, pingentes em verde-esmeralda.',
    descricao: [
      'Uma escultura em branco vestida para cerimônia: a manta foi pintada em camadas de rosa, lilás e ouro, com relevos realçados à mão e pingentes em verde-esmeralda.',
      'Peça de presença, feita para ser o centro do ambiente.',
    ],
    destaque: true,
  },
  {
    slug: 'banquetas-jardim-oriental',
    nome: 'Banquetas Jardim Oriental',
    categoria: 'decoracao',
    resumo: 'Par de banquetas com florada em todas as faces.',
    descricao: [
      'Inspiradas nos tradicionais assentos de jardim chineses, as banquetas recebem uma florada contínua — flores, ramos de bambu e folhagens — e um medalhão geométrico no tampo.',
      'Funcionam como assento, mesa de apoio ou escultura.',
    ],
    destaque: true,
  },
  {
    slug: 'relogio-imari',
    nome: 'Relógio Imari',
    categoria: 'decoracao',
    resumo: 'Coral, cobalto e ouro, na tradição Imari.',
    descricao: [
      'Um relógio de mesa que dialoga com a porcelana Imari japonesa: padrões em vermelho-coral e azul-cobalto, paisagens em azul e branco nos medalhões.',
      'O acabamento em ouro no pináculo e nos pés completa a peça.',
    ],
    destaque: true,
  },
  {
    slug: 'potiches-orquideas',
    nome: 'Potiches Orquídeas',
    categoria: 'decoracao',
    resumo: 'Par de potiches com orquídeas sobre relevo branco.',
    descricao: [
      'Orquídeas em rosa e amarelo sobem pelo corpo dos potiches, pintadas sobre um relevo branco de arabescos.',
      'Tampa e base em vermelho, com filetes em ouro, fecham o par.',
    ],
    destaque: true,
  },
  {
    slug: 'gato-origami',
    nome: 'Gato Origami',
    categoria: 'decoracao',
    resumo: 'Facetas, padrões e cor em cada dobra.',
    descricao: [
      'Uma escultura facetada como uma dobradura de papel. Cada plano recebe um universo próprio: aquarelas, pontilhados, grafismos em preto e ouro.',
      'No meio de tanta cor, o rosto do gato, sereno, observa tudo.',
    ],
    destaque: true,
  },
  {
    slug: 'cachepo-elefante-indiano',
    nome: 'Cachepô Elefante Indiano',
    categoria: 'decoracao',
    resumo: 'Elefante cerimonial em azul, entre padrões ornamentais.',
    descricao: [
      'Borda recortada, pés delicados e um elefante cerimonial em azul e turquesa, cercado por medalhões e padrões inspirados na arte indiana.',
    ],
  },
  {
    slug: 'vaso-carmim',
    nome: 'Vaso Carmim',
    categoria: 'decoracao',
    resumo: 'Um jardim em flor sobre fundo vermelho-carmim.',
    descricao: [
      'Flores e ramagens em amarelo, azul e lilás sobre fundo carmim, com o gargalo trabalhado em grafismos e acabamento em ouro.',
    ],
  },
  {
    slug: 'cachepo-provence',
    nome: 'Cachepô Provence',
    categoria: 'decoracao',
    resumo: 'Amarelo-sol e azul-francês.',
    descricao: [
      'Cachepô quadrado com medalhões florais em azul sobre fundo amarelo, treliças em ouro e borda em xadrez azul — uma homenagem às faianças do sul da França.',
    ],
  },
  {
    slug: 'trio-de-corujas',
    nome: 'Trio de Corujas',
    categoria: 'decoracao',
    resumo: 'Três corujas, três paletas.',
    descricao: [
      'Turquesa, amarelo, rosa e laranja: cada coruja tem a sua personalidade, com a plumagem pintada pena a pena.',
    ],
  },
  {
    slug: 'vaso-composicao',
    nome: 'Vaso Composição',
    categoria: 'decoracao',
    resumo: 'Planos de cor que se encaixam como um vitral.',
    descricao: [
      'Um exercício de cor livre: campos de azul, verde, laranja, rosa e roxo se encaixam pela superfície do vaso, como um vitral pintado à mão.',
    ],
  },
  {
    slug: 'cachepos-magnolia',
    nome: 'Cachepôs Magnólia',
    categoria: 'decoracao',
    resumo: 'Taças de pé alto, borda vazada e flores em grande escala.',
    descricao: [
      'Dois cachepôs em forma de taça, com a borda vazada em gotas. Em um, uma magnólia ocupa a peça inteira; no outro, grafismos em tons de ouro e terra.',
    ],
  },
  {
    slug: 'casticais-turquesa',
    nome: 'Castiçais Turquesa',
    categoria: 'decoracao',
    resumo: 'Turquesa, verde-pistache e arabescos em ouro.',
    descricao: [
      'Par de castiçais altos com base e boca em turquesa, corpo verde-pistache e arabescos em ouro, separados por anéis dourados.',
    ],
  },
  {
    slug: 'bomboniere-rose',
    nome: 'Bomboniere Rosé',
    categoria: 'decoracao',
    resumo: 'Florais em coral e azul, alças em ouro.',
    descricao: [
      'Uma caixa com tampa e alças em ouro, pintada em rosa-chá com arabescos e flores em coral e azul. Para doces, joias ou pequenos tesouros.',
    ],
  },
  {
    slug: 'prato-imari',
    nome: 'Prato Imari',
    categoria: 'decoracao',
    resumo: 'Ramos em coral e ouro, borda pontilhada.',
    descricao: [
      'Prato decorativo em vermelho-coral e ouro, com motivos florais que irradiam do centro e borda trabalhada em pontilhado dourado.',
    ],
  },

  // ——— Mesa posta ———
  {
    slug: 'consome-tropical',
    nome: 'Consomê Tropical',
    categoria: 'mesa',
    resumo: 'Hibiscos, aves-do-paraíso e folhagens.',
    descricao: [
      'Conjunto de consomê com pires de alças, pintado com hibiscos em lilás, aves-do-paraíso e grandes folhas tropicais.',
      'A xícara, em verde, fecha a composição.',
    ],
    destaque: true,
  },
  {
    slug: 'aparelho-horta',
    nome: 'Aparelho Horta',
    categoria: 'mesa',
    resumo: 'Uma colheita diferente em cada prato.',
    descricao: [
      'Um aparelho de jantar em que cada prato traz a sua colheita: tomates, cogumelos, berinjelas, alcachofras e ervas, com filete vermelho e borda verde.',
      'Mesa posta com cara de feira de domingo.',
    ],
  },
  {
    slug: 'petisqueira-aquarela',
    nome: 'Petisqueira Aquarela',
    categoria: 'mesa',
    resumo: 'Seis divisórias em degradê e um centro florido.',
    descricao: [
      'Petisqueira modular com seis divisórias em degradê de rosa, lilás e água-marinha, contornadas em preto, ao redor de um prato central com flores em laranja e vermelho.',
      'Para queijos, frutas e encontros demorados.',
    ],
    video: 'petisqueira',
  },
  {
    slug: 'manteigueira-borboletas',
    nome: 'Manteigueira Borboletas',
    categoria: 'mesa',
    resumo: 'Borboletas e ramos, com contorno em laranja.',
    descricao: [
      'Manteigueira com tampa, pintada com borboletas em azul, amarelo e laranja pousadas entre ramos e folhas.',
      'O fundo também ganha pintura — a surpresa aparece a cada uso.',
    ],
    video: 'manteigueira',
  },
  {
    slug: 'latinhas-sardinha-e-atum',
    nome: 'Latinhas Sardinha & Atum',
    categoria: 'mesa',
    resumo: 'As latas de conserva clássicas, reinventadas em porcelana.',
    descricao: [
      'Uma brincadeira com as latas de conserva: sardinha e atum ganham versões em porcelana, com abridor e rótulo pintados à mão.',
      'Para servir patês e petiscos com bom humor.',
    ],
    video: 'latinhas',
  },
  {
    slug: 'queijeira-hibisco',
    nome: 'Queijeira Hibisco',
    categoria: 'mesa',
    resumo: 'Trama de vime pintada e flores tropicais na tampa.',
    descricao: [
      'A base imita uma trama de vime, pintada fio a fio; a tampa abre um jardim de hibiscos amarelos e laranja entre folhas tropicais.',
      'Para queijos, manteiga ou pães.',
    ],
  },
  {
    slug: 'travessa-limoes',
    nome: 'Travessa Limões',
    categoria: 'mesa',
    resumo: 'Limões-sicilianos e moldura inspirada em azulejos.',
    descricao: [
      'Travessa retangular com limões e folhas sobre fundo branco, emoldurada por um padrão em azul que lembra a azulejaria portuguesa, e borda em amarelo.',
    ],
  },
  {
    slug: 'travessa-jacobina',
    nome: 'Travessa Jacobina',
    categoria: 'mesa',
    resumo: 'Arabescos florais e paisley em tons de jardim.',
    descricao: [
      'Uma travessa ampla tomada por florais de inspiração jacobina — paisleys, flores estilizadas e ramagens em verde, laranja, azul e lilás.',
    ],
  },
  {
    slug: 'consome-geometrico',
    nome: 'Consomê Geométrico',
    categoria: 'mesa',
    resumo: 'Triângulos, círculos e azul-royal.',
    descricao: [
      'Uma leitura geométrica e moderna: triângulos em azul, verde e ouro, círculos concêntricos e pontilhados que dançam em volta da xícara.',
    ],
  },
  {
    slug: 'jarra-olho-grego',
    nome: 'Jarra Olho Grego',
    categoria: 'mesa',
    resumo: 'Olhos protetores em azul-cobalto e ouro.',
    descricao: [
      'Uma jarra de formas arredondadas, coberta de olhos gregos em azul, turquesa e ouro — o símbolo de proteção em versão contemporânea.',
    ],
  },
  {
    slug: 'boleira-confeitaria',
    nome: 'Boleira Confeitaria',
    categoria: 'mesa',
    resumo: 'Cupcakes, pirulitos e sorvetes em volta do prato.',
    descricao: [
      'Prato de bolo com pé, decorado com doces de confeitaria — cupcakes, pirulitos, sorvetes — e uma borda em listras coloridas.',
      'Até o pé ganha confeitos pintados.',
    ],
  },
  {
    slug: 'copos-pintados',
    nome: 'Copos Pintados',
    categoria: 'mesa',
    resumo: 'Flores, limões, pinceladas e gotas de ouro sobre vidro.',
    descricao: [
      'Uma coleção de copos de vidro pintados à mão: flores em azul e magenta, limões-sicilianos, pinceladas abstratas e gotas em ouro.',
      'Ficam lindos juntos — ou cada um com a sua história.',
    ],
  },
  {
    slug: 'bomboniere-arlequim',
    nome: 'Bomboniere Arlequim',
    categoria: 'mesa',
    resumo: 'Losangos, bolinhas e listras numa taça com tampa.',
    descricao: [
      'Bomboniere de vidro com pé e tampa pintados em verde-limão, vermelho, azul e preto e branco. Guarda doces, cápsulas de café ou o que a imaginação mandar.',
    ],
  },

  // ——— Judaica ———
  {
    slug: 'prato-de-shabat',
    nome: 'Prato de Shabat Paz\u00a0·\u00a0Salam\u00a0·\u00a0Shalom',
    categoria: 'judaica',
    resumo: 'Três palavras de paz, a partir de uma folha deixada pelo avô da artista.',
    descricao: [
      'Entre os desenhos deixados pelo avô da artista — fluente em árabe, hebraico e português — havia uma folha de papel com três palavras: Paz, Salam e Shalom.',
      'A folha virou este prato de Shabat, desenhado com flores pequeninas, num traço quase minimalista. Desde então, ele está presente em todos os jantares de sexta-feira da família.',
    ],
    destaque: true,
  },
  {
    slug: 'taca-de-kidush',
    nome: 'Kos de Kidush',
    categoria: 'judaica',
    resumo: 'Cálice e pires floridos, para o vinho das sextas-feiras.',
    descricao: [
      'O kos — o cálice do kidush das sextas-feiras — com o pé e o pires cobertos de florzinhas mínimas, em todas as cores.',
      'Foi criado para acompanhar o Prato de Shabat Paz\u00a0·\u00a0Salam\u00a0·\u00a0Shalom.',
    ],
  },
  {
    slug: 'casticais-shabat-shalom',
    nome: 'Castiçais Shabat Shalom',
    categoria: 'judaica',
    resumo: 'Shabat e Shalom, em hebraico, sobre pétalas e ouro.',
    descricao: [
      'Um par de castiçais para as velas de Shabat: em um, a palavra שבת (Shabat); no outro, שלום (Shalom).',
      'Pétalas em rosa e lilás na base e taças douradas com rendado de pontos.',
    ],
    video: 'velas-shabat',
  },

  // ——— Telas ———
  {
    slug: 'diptico-tropical',
    nome: 'Díptico Tropical',
    categoria: 'telas',
    resumo: 'Ave-do-paraíso e helicônia, em par.',
    descricao: [
      'Duas pinturas emolduradas em madeira: de um lado, a ave-do-paraíso; do outro, a helicônia — flores tropicais em laranja, vermelho e muitos verdes.',
    ],
  },

  // ——— Sob medida ———
  {
    slug: 'cuba-baloes',
    nome: 'Cuba Balões',
    categoria: 'sob-medida',
    resumo: 'Pintura sob medida para a cuba de um lavabo.',
    descricao: [
      'A borda da cuba foi dividida em faixas de cor e padrão — folhagens, quadriculados, listras em preto e branco — e balões coloridos sobem por um céu lilás.',
      'Prova de que a pintura em porcelana vai muito além da mesa.',
    ],
    encomenda: true,
  },
];

export function pecaPorSlug(slug: string): Peca | undefined {
  return pecas.find((p) => p.slug === slug);
}
