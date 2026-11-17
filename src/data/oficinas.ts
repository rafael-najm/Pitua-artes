/**
 * OFICINAS
 * Formatos de oficina, usados na página de Oficinas e na página inicial.
 */
import { foto, editorial } from '../lib/fotos';

export const formatos = [
  {
    id: 'pintura-em-porcelana',
    rotulo: 'Aulas de pintura em porcelana',
    titulo: 'A sua peça, do primeiro traço ao acabamento.',
    resumo: 'Aulas recorrentes: você escolhe a peça e faz tudo.',
    texto: [
      'Você escolhe a sua peça de porcelana e faz tudo, com a orientação da artista: escolhe o desenho, monta a composição, define as cores e produz a peça do início ao fim.',
      'Um aprendizado contínuo, no seu ritmo — a cada peça, mais técnica e mais segurança no pincel.',
    ],
    detalhes: ['Aulas semanais', '3 horas por aula', 'Turma recorrente'],
    cta: 'Quero fazer aulas',
    msg: 'Olá! Tenho interesse nas aulas de pintura em porcelana da Pituá. Como funcionam as turmas?',
    img: editorial('oficina-aulas-travessa'),
    alt: 'Travessa retangular pintada com limões e azulejos azuis, servindo bolo de rolo',
  },
  {
    id: 'criativa',
    rotulo: 'Oficina criativa',
    titulo: 'Um projeto novo a cada encontro.',
    resumo: 'Aulas semanais, cada uma com um projeto diferente.',
    texto: [
      'A cada semana, um projeto diferente: pintura em porcelana, vidro, decoupage, dobraduras e muito mais.',
      'Criatividade solta — um material, uma técnica e uma descoberta nova a cada encontro.',
    ],
    detalhes: ['Aulas semanais', '3 horas por aula', 'Porcelana, vidro, decoupage, dobraduras…'],
    cta: 'Quero participar',
    msg: 'Olá! Tenho interesse na oficina criativa da Pituá. Como funcionam as turmas?',
    img: foto('bomboniere-arlequim', 1),
    alt: 'Bomboniere de vidro pintada à mão, com tampa amarela, pé listrado e bolinhas',
  },
  {
    id: 'workshops',
    rotulo: 'Workshops',
    titulo: 'Um projeto, do começo ao fim, em 2 a 4 aulas.',
    resumo: 'Um projeto escolhido, desenvolvido em 2 a 4 aulas.',
    texto: [
      'A cada workshop, um projeto escolhido — em porcelana, vidro ou outra técnica — desenvolvido ao longo de 2, 3 ou 4 aulas, com o passo a passo guiado pela artista.',
      'Para quem quer se aprofundar numa peça com calma e terminar o workshop com ela pronta.',
    ],
    detalhes: ['Projeto definido', '2, 3 ou 4 aulas', 'Porcelana, vidro e outras técnicas'],
    cta: 'Quero saber dos próximos workshops',
    msg: 'Olá! Tenho interesse nos workshops da Pituá. Quais são os próximos projetos?',
    img: foto('consome-geometrico', 1),
    alt: 'Conjunto de consomê pintado com triângulos e círculos em azul e verde',
  },
  {
    id: 'tematicas',
    rotulo: 'Oficinas temáticas',
    titulo: 'Temáticas, pensadas por projeto.',
    resumo: 'Sob medida para aniversários, grupos e eventos especiais.',
    texto: [
      'Oficinas desenhadas sob medida para uma ocasião: datas comemorativas, aniversários, encontros entre amigas, grupos e empresas.',
      'O tema, a peça e o formato são definidos junto com você.',
    ],
    detalhes: ['Sob medida', 'Grupos e eventos'],
    cta: 'Planejar uma oficina temática',
    msg: 'Olá! Gostaria de planejar uma oficina temática com a Pituá.',
    img: editorial('oficina-tematica-prato'),
    alt: 'Prato fundo pintado com tomates e folhas, sobre jogo americano de palha',
  },
];
