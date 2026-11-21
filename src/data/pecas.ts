/**
 * ACERVO
 * ------
 * Cada peça tem uma pasta de fotos em `src/assets/pecas/<slug>/`.
 * As fotos são exibidas em ordem alfabética (01.jpg, 02.jpg…); a primeira é a capa.
 *
 * Para adicionar uma peça: crie a pasta com as fotos e acrescente um item nesta lista.
 */

export type Categoria = 'mesa' | 'decoracao' | 'judaica' | 'placas' | 'sob-medida';

export const categorias: Record<Categoria, string> = {
  mesa: 'Mesa posta',
  decoracao: 'Decoração',
  judaica: 'Judaica',
  placas: 'Placas',
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
    slug: 'vasos-orquideas',
    nome: 'Vasos Orquídeas',
    categoria: 'decoracao',
    resumo: 'Par de vasos com orquídeas sobre relevo branco.',
    descricao: [
      'Orquídeas em rosa e amarelo sobem pelo corpo dos vasos, pintadas sobre um relevo branco de arabescos.',
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
    destaque: true,
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
    slug: 'sorveteira-oriental',
    nome: 'Sorveteira Oriental',
    categoria: 'decoracao',
    resumo: 'Florais em coral e azul, alças em ouro.',
    descricao: [
      'Uma sorveteira com tampa e alças em ouro, pintada em rosa-chá com arabescos e flores em coral e azul, inspirada nos padrões orientais.',
    ],
  },
  {
    slug: 'caixa-imari',
    nome: 'Caixa Imari',
    categoria: 'decoracao',
    resumo: 'Ramos em coral e ouro, borda pontilhada.',
    descricao: [
      'Caixa decorativa em vermelho-coral e ouro, com motivos florais que irradiam do centro e borda trabalhada em pontilhado dourado.',
    ],
  },

  {
    slug: 'abajur-menino-rafa',
    nome: 'Abajur Menino Rafa',
    categoria: 'decoracao',
    resumo: 'Céu de nuvens e um menino entre brinquedos.',
    descricao: [
      'Abajur de porcelana com céu azul e nuvens brancas, onde um menino de boné brinca cercado de ursinho, bolas e cubos de letras.',
      'O gargalo listrado em azul e a cúpula de linho completam uma peça feita para o quarto de criança.',
    ],
  },
  {
    slug: 'conjunto-quarto-do-bebe-menino-rafa',
    nome: 'Conjunto Quarto do Bebê Menino Rafa',
    categoria: 'decoracao',
    resumo: 'Potes com tampa e tigela, com brinquedos e nuvens.',
    descricao: [
      'Conjunto para o quarto do bebê com três potes de tampa em céu azul e uma tigela. Cada pote conta uma brincadeira: o menino de boné, a pipa, a bicicleta, o aviãozinho, o ursinho e os cubos de letras.',
      'A tigela traz um ursinho no fundo, cercado de azul.',
    ],
  },
  {
    slug: 'moringa-abelha-mel',
    nome: 'Moringa Abelha Mel',
    categoria: 'mesa',
    resumo: 'Abelhas, borboletas e um laço turquesa.',
    descricao: [
      'Moringa com copo, pintada com abelhas e borboletas em tons suaves, gargalo amarelo e um laço turquesa em relevo.',
      'Delicada para a mesa de cabeceira ou o quarto das crianças.',
    ],
  },
  {
    slug: 'conjunto-quarto-do-bebe-abelha-mel',
    nome: 'Conjunto Quarto do Bebê Abelha Mel',
    categoria: 'decoracao',
    resumo: 'Três potinhos com abelhas, borboletas e corações.',
    descricao: [
      'Trio de potinhos com tampa para o quarto do bebê: abelhas e borboletas nas tampas, corações, bolinhas e florzinhas nas laterais, em rosa, verde e azul.',
      'Para algodão, cotonetes e pequenos tesouros.',
    ],
  },
  {
    slug: 'globo',
    nome: 'Globo',
    categoria: 'decoracao',
    resumo: 'O mundo em azul profundo, com continentes coloridos.',
    descricao: [
      'Globo terrestre de porcelana sobre base dourada: oceanos em azul profundo, linhas de latitude e longitude em ouro e continentes pintados em mosaico de rosa, laranja, amarelo e verde.',
      'Uma peça para escritórios, estantes e para quem gosta de viajar.',
    ],
  },
  {
    slug: 'kit-lavabo',
    nome: 'Kit Lavabo',
    categoria: 'decoracao',
    resumo: 'Saboneteira, porta-escovas e copo com padrões gráficos.',
    descricao: [
      'Kit para lavabo com saboneteira, porta-escovas e copo, cada peça com um padrão gráfico diferente: escamas, xadrez, florzinhas e listras coloridas.',
      'As cores conversam entre si e deixam o banheiro alegre.',
    ],
  },
  {
    slug: 'par-de-vasos-pistache',
    nome: 'Par de Vasos Pistache',
    categoria: 'decoracao',
    resumo: 'Centáureas e flores do campo sobre verde-pistache.',
    descricao: [
      'Par de vasos com borda recortada em ouro, pintados com centáureas azuis, flores do campo e folhagens sobre fundo branco e verde-pistache.',
      'Bonitos juntos ou separados, com ou sem flores.',
    ],
  },
  {
    slug: 'pote-marmore',
    nome: 'Pote Mármore',
    categoria: 'decoracao',
    resumo: 'Efeito de mármore amarelo com filetes azuis.',
    descricao: [
      'Pote com tampa pintado com efeito de mármore em amarelo e veios delicados, emoldurado por faixas em azul-cobalto e ouro.',
      'Uma peça clássica, que combina com ambientes sóbrios e coloridos.',
    ],
  },
  {
    slug: 'potiche-tulipa',
    nome: 'Potiche Tulipa',
    categoria: 'decoracao',
    resumo: 'Uma grande tulipa sobre xadrez laranja e poás verdes.',
    descricao: [
      'Potiche com tampa em que uma grande tulipa em laranja e vermelho se destaca sobre um fundo que mistura xadrez laranja e poás verde-água.',
      'Uma composição ousada, que muda a cada lado da peça.',
    ],
  },
  {
    slug: 'vaso-areia-ninfeia',
    nome: 'Vaso Areia Ninfeia',
    categoria: 'decoracao',
    resumo: 'Ninfeia em rosa e amarelo sobre um céu em aquarela.',
    descricao: [
      'Vaso com acabamento de textura arenosa, pintado em aquarela de azul, lilás e amarelo, com uma ninfeia em rosa e grandes folhas de lago em verde.',
      'Cada lado da peça traz uma parte da cena.',
    ],
  },
  {
    slug: 'vaso-conchas',
    nome: 'Vaso Conchas',
    categoria: 'decoracao',
    resumo: 'Conchas, corais e golfinhos em relevo.',
    descricao: [
      'Vaso com golfinhos em relevo nas laterais, pintado com conchas, cavalos-marinhos, águas-vivas e corais em tons de terracota, sobre uma base que imita palha trançada.',
      'Uma peça que traz o mar para dentro de casa.',
    ],
  },
  {
    slug: 'vaso-cordas',
    nome: 'Vaso Cordas',
    categoria: 'decoracao',
    resumo: 'Peônias e cordas douradas sobre fundo escuro.',
    descricao: [
      'Par de vasos em fundo marrom-escuro, com grandes peônias em rosa e creme e cordões dourados com borlas, que contornam a borda e descem pela lateral.',
      'Elegantes e dramáticos, lado a lado.',
    ],
  },
  {
    slug: 'vaso-pavao-persa',
    nome: 'Vaso Pavão Persa',
    categoria: 'decoracao',
    resumo: 'Arabescos persas e um pavão entre flores.',
    descricao: [
      'Vaso de gargalo longo em degradê de lilás a azul-cobalto, com medalhões de arabescos persas e um pavão entre flores, contornados em ouro.',
      'A borda recortada e a base dourada completam a peça.',
    ],
  },
  {
    slug: 'vaso-peixes',
    nome: 'Vaso Peixes',
    categoria: 'decoracao',
    resumo: 'Peixes tropicais em um mosaico de cores.',
    descricao: [
      'Vaso bojudo pintado como um recife de corais: peixes-palhaço, peixes-anjo e anêmonas em mosaico de cores vivas, com faixas em amarelo, verde e lilás no gargalo.',
      'Uma peça cheia de movimento, para ambientes alegres.',
    ],
  },
  {
    slug: 'vaso-rouen',
    nome: 'Vaso Rouen',
    categoria: 'decoracao',
    resumo: 'Azul-cobalto sobre branco, no estilo da faiança de Rouen.',
    descricao: [
      'Vaso pintado em azul-cobalto sobre branco, com lambrequins, arabescos e flores inspirados na faiança francesa de Rouen.',
      'Um clássico que atravessa estilos e combina com qualquer ambiente.',
    ],
  },
  {
    slug: 'vaso-silhueta-floral',
    nome: 'Vaso Silhueta Floral',
    categoria: 'decoracao',
    resumo: 'Curvas de porcelana com flores e faixas em azul.',
    descricao: [
      'Vaso de silhueta sinuosa, com flores coloridas emolduradas por contornos em ouro e faixas em azul que acompanham as curvas da peça.',
      'Cada ângulo revela uma composição diferente.',
    ],
  },
  {
    slug: 'anfora-cisnes',
    nome: 'Ânfora Cisnes',
    categoria: 'decoracao',
    resumo: 'Cena romântica, azul-cobalto e alças de cisne.',
    descricao: [
      'Ânfora em azul-cobalto com alças em forma de cisne e um medalhão com uma cena romântica em jardim, pintada com riqueza de detalhes e emoldurada em ouro.',
      'O verso traz estrelas douradas sobre o azul, e a base quadrada fecha a peça com um friso grego.',
    ],
  },
  {
    slug: 'anfora-floral-lilas',
    nome: 'Ânfora Floral Lilás',
    categoria: 'decoracao',
    resumo: 'Guirlandas de flores em lilás, branco e ouro.',
    descricao: [
      'Ânfora com tampa e alças douradas, pintada em faixas de lilás e branco, com uma guirlanda de rosas e flores do campo ao redor do corpo.',
      'A base sextavada traz borboletas e flores silvestres, em contraste delicado com o lilás.',
    ],
  },

  // ——— Mesa posta ———
  {
    slug: 'petisqueira-tropical',
    nome: 'Petisqueira Tropical',
    categoria: 'mesa',
    resumo: 'Hibiscos, aves-do-paraíso e folhagens.',
    descricao: [
      'Petisqueira com tigela central e base com alças, pintada com hibiscos em lilás, aves-do-paraíso e grandes folhas tropicais.',
      'A tigela, em verde, fecha a composição.',
    ],
    destaque: true,
  },
  {
    slug: 'aparelho-risoto-horta',
    nome: 'Aparelho para Risoto Horta',
    categoria: 'mesa',
    resumo: 'Uma colheita diferente em cada prato.',
    descricao: [
      'Um aparelho para risoto em que cada prato traz a sua colheita: alcachofras, milho, cogumelos, berinjelas, rabanetes e ervas, contornando a borda em vermelho.',
      'Mesa posta com cara de feira de domingo.',
    ],
  },
  {
    slug: 'pratos-para-massas',
    nome: 'Pratos para Massas',
    categoria: 'mesa',
    resumo: 'Tomates, cogumelos e ervas na aba do prato.',
    descricao: [
      'Pratos fundos para massas, com tomates, cogumelos, azeitonas e ervas pintados na aba, filete vermelho e borda verde.',
      'Cada prato com a sua composição — juntos, contam a história de uma boa macarronada.',
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
    slug: 'petisqueira-geometrica',
    nome: 'Petisqueira Geométrica',
    categoria: 'mesa',
    resumo: 'Triângulos, círculos e azul-royal.',
    descricao: [
      'Uma leitura geométrica e moderna: triângulos em azul, verde e ouro, círculos concêntricos e pontilhados que dançam em volta da tigela central.',
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

  {
    slug: 'balde-de-gelo-rosas',
    nome: 'Balde de Gelo Rosas',
    categoria: 'mesa',
    resumo: 'Rosas em traço preto sobre um degradê de verão.',
    descricao: [
      'Balde de gelo com borda ondulada e alça de metal, pintado em degradê de amarelo, rosa e verde, com rosas desenhadas em traço preto, xadrez e padrões gráficos.',
      'Para levar cor ao bar e à mesa de verão.',
    ],
  },
  {
    slug: 'bule-camelo',
    nome: 'Bule Camelo',
    categoria: 'mesa',
    resumo: 'Um camelo de manta bordada em laranja, turquesa e ouro.',
    descricao: [
      'Bule em forma de camelo deitado, com a manta pintada como um bordado: flores em azul e vermelho sobre fundo laranja, franjas em turquesa e detalhes em ouro.',
      'A tampa turquesa e a alça dourada completam uma peça que é escultura e bule ao mesmo tempo.',
    ],
  },
  {
    slug: 'descansos-de-colher-chefs',
    nome: 'Descansos de Colher Chefs',
    categoria: 'mesa',
    resumo: 'Um casal de chefs para a bancada da cozinha.',
    descricao: [
      'Par de descansos de colher em forma de chefs de cozinha: ela de lenço vermelho e avental xadrez, ele de bigode, lenço amarelo e avental listrado.',
      'Divertidos e úteis, para quem gosta de cozinhar com bom humor.',
    ],
  },
  {
    slug: 'fruteira-borboletas',
    nome: 'Fruteira Borboletas',
    categoria: 'mesa',
    resumo: 'Borboletas coloridas em uma fruteira com pé.',
    descricao: [
      'Fruteira oval com pé, coberta de borboletas em laranja, azul, rosa e amarelo, pousadas entre ramos verde-claros.',
      'O pé listrado e a base com cantos coloridos fazem dela uma peça de centro de mesa.',
    ],
  },
  {
    slug: 'galheteiro-oliva',
    nome: 'Galheteiro Oliva',
    categoria: 'mesa',
    resumo: 'Ramos de oliveira e azeitonas em tons de roxo.',
    descricao: [
      'Galheteiro quadrado com bico dosador, pintado com ramos de oliveira, azeitonas roxas e arabescos em preto, com o gargalo em amarelo.',
      'Para o azeite de todo dia ganhar lugar de destaque na mesa.',
    ],
  },
  {
    slug: 'porta-queijo-ralado',
    nome: 'Porta Queijo Ralado',
    categoria: 'mesa',
    resumo: 'Uma fatia de queijo, com furinhos e tudo.',
    descricao: [
      'Porta-queijo ralado em forma de fatia de queijo, com casca vermelha, tampa furada para servir e alça lateral.',
      'Bem-humorado, para a mesa da macarronada.',
    ],
  },
  {
    slug: 'potinho-listras',
    nome: 'Potinho Listras',
    categoria: 'mesa',
    resumo: 'Listras coloridas em diagonais, com alças amarelas.',
    descricao: [
      'Potinho retangular com alças amarelas, pintado com listras em azul, verde, laranja, vermelho e roxo, em blocos de diagonais.',
      'Para servir petiscos, molhos e sobremesas com alegria.',
    ],
  },
  {
    slug: 'potinhos-coruja',
    nome: 'Potinhos Coruja',
    categoria: 'mesa',
    resumo: 'Coruja, raposa e flores, com interior laranja.',
    descricao: [
      'Par de cumbucas com borda ondulada e interior laranja, pintadas com coruja, raposa, flores vermelhas e folhagens.',
      'Para petiscos e para a mesa de quem gosta de bichos.',
    ],
  },
  {
    slug: 'travessas-animal-print',
    nome: 'Travessas Animal Print',
    categoria: 'mesa',
    resumo: 'Onça, zebra e flores tropicais.',
    descricao: [
      'Par de travessas retangulares que misturam estampa de onça e de zebra com flores tropicais em amarelo e laranja, com bordas em azul-claro e amarelo.',
      'Para uma mesa cheia de personalidade.',
    ],
  },
  {
    slug: 'travessas-folhagem',
    nome: 'Travessas Folhagem',
    categoria: 'mesa',
    resumo: 'Folhagens tropicais em verde, com filete escuro.',
    descricao: [
      'Conjunto de travessas retangulares em três tamanhos, pintadas com costela-de-adão, palmeiras e samambaias em tons de verde, com borda em filete escuro.',
      'Do forno à mesa, com o frescor de um jardim.',
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

  // ——— Placas ———
  {
    slug: 'placas-emolduradas-tropicais',
    nome: 'Placas Emolduradas Tropicais',
    categoria: 'placas',
    resumo: 'Ave-do-paraíso e helicônia, em par.',
    descricao: [
      'Duas placas de porcelana pintadas à mão e emolduradas em madeira: de um lado, a ave-do-paraíso; do outro, a helicônia — flores tropicais em laranja, vermelho e muitos verdes.',
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
  },
];

export function pecaPorSlug(slug: string): Peca | undefined {
  return pecas.find((p) => p.slug === slug);
}
