/**
 * PEÇAS PARA PERSONALIZAR
 * -----------------------
 * Peças em porcelana branca que recebem pintura personalizada sob encomenda.
 * Aparecem na página de Encomendas e cada uma ganha a sua página em /encomendas/<slug>/.
 *
 * Para adicionar uma peça: coloque a foto em `src/assets/personalizar/` e acrescente um item na lista.
 * Peças sem `foto` ficam escondidas do site até a foto ser adicionada.
 */
import type { ImageMetadata } from 'astro';
import moringaFaixa from '../assets/personalizar/moringa-faixa.webp';
import moringaLisa from '../assets/personalizar/moringa-lisa.webp';
import vela from '../assets/personalizar/vela-copo-porcelana.webp';
import chanukia from '../assets/personalizar/chanukia.webp';
import copinhosShabat from '../assets/personalizar/copinhos-shabat.webp';
import potesBolinha from '../assets/personalizar/potes-multiuso-bolinha.webp';
import potesMel from '../assets/personalizar/potes-multiuso-mel.webp';
import parDeCasticais from '../assets/personalizar/par-de-casticais.webp';
import pratoOval from '../assets/personalizar/prato-grande-oval.webp';
import pratoQuadrado from '../assets/personalizar/prato-grande-quadrado.webp';
import portaJoias from '../assets/personalizar/porta-joias-do-dia.webp';
import canecaAfeto from '../assets/personalizar/caneca-afeto.webp';
import canecaComTampa from '../assets/personalizar/caneca-com-tampa.webp';
import copinho from '../assets/personalizar/copinho.webp';

export interface Medidas {
  /** Ex.: "Moringa", "Copo". Vazio quando há um só bloco. */
  titulo?: string;
  itens: [rotulo: string, valor: string][];
}

export interface PecaPersonalizavel {
  slug: string;
  nome: string;
  /** Frase de abertura, aparece abaixo do nome. */
  chamada: string;
  /** Linha curta para o card (capacidade, tamanho…). */
  resumo: string;
  descricao: string[];
  material: string;
  formato?: string;
  composicao?: string;
  medidas: Medidas[];
  /** Valor em reais (sem centavos). */
  aPartirDe: number;
  foto?: ImageMetadata;
  alt: string;
}

const todas: PecaPersonalizavel[] = [
  {
    slug: 'moringa-faixa',
    nome: 'Moringa Faixa com Copo',
    chamada: 'Um clássico que ganha personalidade e exclusividade.',
    resumo: '1,1 litro · 21 cm de altura',
    descricao: [
      'A moringa com copo é uma peça que une beleza, funcionalidade e delicadeza. Ideal para manter água sempre à mão na mesa de cabeceira, no escritório ou em um cantinho especial da casa.',
      'Confeccionada em porcelana branca, recebe pintura artística personalizada, desenvolvida especialmente a partir da sua ideia ou referência. Flores, desenhos, monogramas, ilustrações ou uma composição exclusiva: você escolhe a arte e nós transformamos a peça em algo único.',
    ],
    material: 'Porcelana',
    medidas: [
      {
        titulo: 'Moringa',
        itens: [
          ['Altura', '21 cm'],
          ['Diâmetro', '13 cm'],
          ['Capacidade', '1.100 ml'],
        ],
      },
      {
        titulo: 'Copo',
        itens: [
          ['Altura', '7,5 cm'],
          ['Diâmetro', '7 cm'],
          ['Capacidade', '125 ml'],
        ],
      },
    ],
    aPartirDe: 548,
    foto: moringaFaixa,
    alt: 'Moringa de porcelana branca com faixa em relevo e copo encaixado no gargalo',
  },
  {
    slug: 'moringa-lisa',
    nome: 'Moringa Lisa com Copo',
    chamada: 'Linhas retas e design minimalista.',
    resumo: '800 ml · 17 cm de altura',
    descricao: [
      'Com linhas retas e design minimalista, a moringa é ideal para manter água sempre à mão na mesa de cabeceira, no escritório ou em um cantinho especial da casa.',
      'Confeccionada em porcelana branca, recebe pintura artística personalizada, desenvolvida especialmente a partir da sua ideia ou referência. Flores, desenhos, monogramas, ilustrações ou uma composição exclusiva: você escolhe a arte e nós transformamos a peça em algo único.',
    ],
    material: 'Porcelana',
    medidas: [
      {
        titulo: 'Moringa',
        itens: [
          ['Altura', '17 cm'],
          ['Diâmetro', '11,5 cm'],
          ['Capacidade', '800 ml'],
        ],
      },
      {
        titulo: 'Copo',
        itens: [
          ['Altura', '6,6 cm'],
          ['Diâmetro', '5,5 cm'],
          ['Capacidade', '80 ml'],
        ],
      },
    ],
    aPartirDe: 538,
    foto: moringaLisa,
    alt: 'Moringa de porcelana branca de linhas retas, com copo cilíndrico encaixado',
  },
  {
    slug: 'vela-copo-porcelana',
    nome: 'Vela em Copo de Porcelana',
    chamada: 'Delicadeza, perfume e arte para deixar qualquer ambiente mais acolhedor.',
    resumo: 'Vela perfumada · 160 ml',
    descricao: [
      'Nossa vela perfumada é apresentada em um copo de porcelana branca, que recebe pintura artística personalizada, desenvolvida especialmente a partir da sua ideia ou referência. Flores, desenhos, monogramas ou ilustrações exclusivas transformam a peça em um objeto único.',
      'Além de perfumar o ambiente, é uma peça decorativa que pode continuar sendo apreciada mesmo depois que a vela terminar.',
      'Uma opção especial para presentear, surpreender e demonstrar carinho em ocasiões especiais. Afinal, presentes personalizados carregam um significado a mais.',
    ],
    material: 'Porcelana (recipiente)',
    medidas: [
      {
        itens: [
          ['Altura', '8 cm'],
          ['Diâmetro', '6,8 cm'],
          ['Capacidade da vela', '160 ml'],
        ],
      },
    ],
    aPartirDe: 188,
    foto: vela,
    alt: 'Vela perfumada em copo de porcelana branca',
  },
  {
    slug: 'chanukia',
    nome: 'Chanukiá',
    chamada: 'Uma maneira especial de celebrar Chanucá, unindo tradição, arte e personalidade.',
    resumo: '8 copinhos + shamash',
    descricao: [
      'Composta por 8 copinhos de porcelana e um copinho mais alto para o shamash (vela auxiliar), nossa chanukiá tem uma proposta contemporânea e versátil. As peças recebem pintura artística personalizada, desenvolvida especialmente a partir da sua ideia ou referência.',
      'Um detalhe especial: os copinhos podem ser usados separadamente ao longo do ano, como pequenos castiçais decorativos, prolongando a beleza e a utilidade da peça para além da celebração.',
    ],
    material: 'Porcelana',
    composicao: '8 copinhos para as velas + 1 copinho mais alto para o shamash',
    medidas: [
      {
        itens: [['Capacidade', 'Copinhos de 70 ml e 90 ml']],
      },
    ],
    aPartirDe: 699,
    foto: chanukia,
    alt: 'Chanukiá com oito copinhos de porcelana branca e um copinho mais alto para o shamash, com velas acesas',
  },
  {
    slug: 'copinhos-shabat',
    nome: 'Par de Copinhos — Castiçais de Shabat',
    chamada: 'Delicadeza nos detalhes para criar uma atmosfera especial.',
    resumo: '2 copinhos · 70 ou 90 ml',
    descricao: [
      'O par é composto por dois copinhos de porcelana branca, ideais para acomodar velas e trazer um toque de charme à decoração. Também podem ser usados para as velas de Shabat.',
      'Versáteis e delicados, ficam lindos em mesas de jantar, aparadores ou em composições decorativas pela casa.',
      'Cada peça recebe pintura artística personalizada, desenvolvida especialmente a partir da sua ideia ou referência, tornando o conjunto exclusivo.',
    ],
    material: 'Porcelana',
    composicao: '2 copinhos',
    medidas: [
      {
        itens: [['Capacidade', '70 ou 90 ml cada']],
      },
    ],
    aPartirDe: 268,
    foto: copinhosShabat,
    alt: 'Par de copinhos de porcelana branca com velas acesas',
  },
  {
    slug: 'copinho',
    nome: 'Copinho',
    chamada: 'Uma peça delicada e cheia de possibilidades.',
    resumo: 'Cálice ou castiçal · 70 ou 90 ml',
    descricao: [
      'Com design simples e elegante, este copinho de porcelana pode ser usado como um pequeno cálice para servir vinho ou transformado em um charmoso castiçal para velas.',
      'Versátil e atemporal, fica lindo na composição da mesa, em ocasiões especiais ou na decoração da casa. Também pode receber pintura artística personalizada, criada especialmente para você.',
      'Uma peça, diferentes maneiras de usar e um charme especial em cada detalhe.',
    ],
    material: 'Porcelana',
    medidas: [{ itens: [['Capacidade', '70 ou 90 ml']] }],
    aPartirDe: 138,
    foto: copinho,
    alt: 'Copinho cilíndrico de porcelana branca',
  },
  {
    slug: 'par-de-casticais',
    nome: 'Par de Castiçais',
    chamada: 'Elegância e delicadeza para iluminar momentos especiais.',
    resumo: '2 castiçais · 9,5 cm de altura',
    descricao: [
      'Com design clássico e acabamento em porcelana branca, este par de castiçais é perfeito para compor mesas de jantar, aparadores e cantinhos especiais da casa. Também pode ser usado para as velas de Shabat, trazendo beleza e personalidade à celebração.',
      'Cada peça recebe pintura artística personalizada, desenvolvida especialmente a partir da sua ideia ou referência, tornando o conjunto exclusivo.',
    ],
    material: 'Porcelana',
    composicao: '2 castiçais',
    medidas: [
      {
        titulo: 'Cada peça',
        itens: [
          ['Altura', '9,5 cm'],
          ['Diâmetro da base', '7 cm'],
        ],
      },
    ],
    aPartirDe: 398,
    foto: parDeCasticais,
    alt: 'Par de castiçais clássicos de porcelana branca, com base larga e boca levemente aberta',
  },
  {
    slug: 'potes-multiuso-mel',
    nome: 'Conjunto de 3 Potes Multiuso Mel',
    chamada: 'Beleza, organização e versatilidade em peças que ganham a sua personalidade.',
    resumo: '3 potes com tampa · 5 a 10 cm de altura',
    descricao: [
      'Nosso conjunto de potes de porcelana é perfeito para organizar pequenos objetos e dar um toque especial à decoração. No banheiro, são ideais para guardar algodão, cotonetes e acessórios. Na papelaria, acomodam pequenos materiais de escritório. No quarto do bebê, podem fazer parte do enxoval, organizando itens de higiene e cuidados.',
      'Confeccionados em porcelana branca, os potes recebem pintura artística personalizada, desenvolvida especialmente a partir da sua ideia ou referência. Assim, cada conjunto se transforma em uma criação exclusiva.',
    ],
    material: 'Porcelana',
    composicao: 'Conjunto com 3 potes com tampas',
    medidas: [
      {
        itens: [
          ['Pote 1', 'Altura 5 cm · Diâmetro 9 cm'],
          ['Pote 2', 'Altura 8,5 cm · Diâmetro 9 cm'],
          ['Pote 3', 'Altura 10 cm · Diâmetro 9 cm'],
        ],
      },
    ],
    aPartirDe: 798,
    foto: potesMel,
    alt: 'Três potes cilíndricos de porcelana branca com tampa, em alturas diferentes',
  },
  {
    slug: 'potes-multiuso-bolinha',
    nome: 'Conjunto de 3 Potes Multiuso Bolinha',
    chamada: 'Beleza, organização e versatilidade em peças que ganham a sua personalidade.',
    resumo: '3 potes com tampa · 7,5 a 12 cm de altura',
    descricao: [
      'Nosso conjunto de potes de porcelana é perfeito para organizar pequenos objetos e dar um toque especial à decoração. No banheiro, são ideais para guardar algodão, cotonetes e acessórios. Na papelaria, acomodam pequenos materiais de escritório. No quarto do bebê, podem fazer parte do enxoval, organizando itens de higiene e cuidados.',
      'Confeccionados em porcelana branca, os potes recebem pintura artística personalizada, desenvolvida especialmente a partir da sua ideia ou referência. Assim, cada conjunto se transforma em uma criação exclusiva.',
    ],
    material: 'Porcelana',
    composicao: 'Conjunto com 3 potes com tampas',
    medidas: [
      {
        itens: [
          ['Pote pequeno', 'Altura 7,5 cm · Diâmetro 9,5 cm'],
          ['Pote médio', 'Altura 10 cm · Diâmetro 9 cm'],
          ['Pote grande', 'Altura 12 cm · Diâmetro 9 cm'],
        ],
      },
    ],
    aPartirDe: 848,
    foto: potesBolinha,
    alt: 'Três potes de porcelana branca de tamanhos diferentes, com tampas de pegador em bolinha',
  },
  {
    slug: 'prato-grande-quadrado',
    nome: 'Prato Grande Quadrado',
    chamada: 'Uma peça versátil que une funcionalidade e expressão artística.',
    resumo: 'Quadrado · 26 × 26 cm',
    descricao: [
      'Com formato quadrado e linhas delicadas, este prato é perfeito para servir, apresentar petiscos e sobremesas ou compor uma mesa especial. Também pode ser usado como peça decorativa em aparadores e bandejas ou como prato de matzot para Pessach.',
      'Confeccionado em porcelana branca, recebe pintura artística personalizada, desenvolvida especialmente a partir da sua ideia ou referência. Você escolhe a arte e nós transformamos o prato em uma peça exclusiva.',
    ],
    material: 'Porcelana',
    formato: 'Quadrado',
    medidas: [{ itens: [['Tamanho', '26 × 26 cm']] }],
    aPartirDe: 498,
    foto: pratoQuadrado,
    alt: 'Prato grande quadrado de porcelana branca, com borda baixa',
  },
  {
    slug: 'prato-grande-oval',
    nome: 'Prato Grande Oval',
    chamada: 'Uma peça especial para compor a mesa de Shabat com beleza, tradição e personalidade.',
    resumo: 'Oval · 22 × 17 cm',
    descricao: [
      'Com formato oval e linhas delicadas, este prato é ideal para acomodar as chalot e dar destaque à mesa durante o Shabat e outras celebrações. Também pode ser usado para servir pães e outras preparações em ocasiões especiais.',
      'Confeccionado em porcelana branca, recebe pintura artística personalizada, desenvolvida especialmente a partir da sua ideia ou referência. Você escolhe a arte e nós transformamos a peça em uma criação exclusiva.',
    ],
    material: 'Porcelana',
    formato: 'Oval',
    medidas: [{ itens: [['Tamanho', '22 × 17 cm']] }],
    aPartirDe: 498,
    foto: pratoOval,
    alt: 'Prato grande oval de porcelana branca',
  },
  {
    slug: 'porta-joias-do-dia',
    nome: 'Porta-Joias do Dia',
    chamada: 'Delicadeza para guardar pequenos tesouros e criar lembranças especiais.',
    resumo: 'Redondo · 10 cm de diâmetro',
    descricao: [
      'Com design redondo e acabamento delicado, este porta-joias é ideal para acomodar anéis, brincos, colares e outros pequenos acessórios. Perfeito para deixar na mesa de cabeceira, na penteadeira ou no banheiro, mantendo suas peças favoritas sempre à mão.',
      'Confeccionado em porcelana branca, recebe pintura artística personalizada, desenvolvida especialmente a partir da sua ideia ou referência.',
      'Também é uma opção encantadora para presentear ou oferecer como lembrança em festas e ocasiões especiais, como casamentos, aniversários e eventos. Uma peça que pode receber uma arte exclusiva, tornando cada presente ainda mais significativo.',
    ],
    material: 'Porcelana',
    formato: 'Redondo',
    medidas: [{ itens: [['Diâmetro', '10 cm']] }],
    aPartirDe: 168,
    foto: portaJoias,
    alt: 'Porta-joias redondo de porcelana branca com borda ondulada',
  },
  {
    slug: 'caneca-afeto',
    nome: 'Caneca Afeto',
    chamada: 'Uma peça versátil e atemporal, com design clean e acabamento branco brilhante.',
    resumo: '300 ml · 9 cm de altura',
    descricao: [
      'Ideal para acompanhar o café, o chá ou a sua bebida preferida em qualquer momento do dia.',
      'Produzida em porcelana, pode receber pintura artística personalizada, criada especialmente para você. Uma ótima opção para presentear ou trazer um toque de personalidade à mesa.',
    ],
    material: 'Porcelana',
    medidas: [
      {
        itens: [
          ['Capacidade', '300 ml'],
          ['Altura', '9 cm'],
          ['Largura', '12 cm (com alça)'],
        ],
      },
    ],
    aPartirDe: 268,
    foto: canecaAfeto,
    alt: 'Caneca de porcelana branca com alça, de design clean',
  },
  {
    slug: 'caneca-com-tampa',
    nome: 'Caneca com Tampa',
    chamada: 'Uma peça delicada e versátil, perfeita para tornar os momentos de pausa ainda mais especiais.',
    resumo: '280 ml · acompanha tampa',
    descricao: [
      'A caneca de porcelana acompanha uma tampa que ajuda a conservar a temperatura da bebida e traz um charme extra à composição.',
      'Ideal para café, chá e outras bebidas quentes, também é uma ótima opção para presentear. Pode receber pintura artística personalizada, criada especialmente para você ou para alguém querido.',
    ],
    material: 'Porcelana',
    composicao: 'Caneca + tampa',
    medidas: [
      {
        itens: [
          ['Capacidade', '280 ml'],
          ['Altura', '9 cm'],
          ['Diâmetro', '8 cm'],
        ],
      },
    ],
    aPartirDe: 298,
    foto: canecaComTampa,
    alt: 'Caneca de porcelana branca com tampa',
  },
];

/** Só as peças com foto aparecem no site. */
export const personalizaveis = todas.filter((p): p is PecaPersonalizavel & { foto: ImageMetadata } => !!p.foto);

export const formatarPreco = (valor: number) =>
  new Intl.NumberFormat('pt-BR', { style: 'currency', currency: 'BRL', maximumFractionDigits: 0 }).format(valor);
