/**
 * Dados de contato e textos gerais do site.
 * Preencha os campos vazios — o site se ajusta sozinho.
 */
export const site = {
  nome: 'Pituá',
  assinatura: 'Arte sob encomenda',
  descricao:
    'Porcelana pintada à mão. Peças únicas, encomendas personalizadas e oficinas criativas.',

  /** Número com DDI e DDD, só dígitos. Ex.: '5521999998888'. Vazio = WhatsApp abre para escolher o contato. */
  whatsapp: '5521968843029', // +55 21 96884-3029
  /** Usuário do Instagram, sem @. Ex.: 'pitua.artes'. Vazio = não aparece. */
  instagram: 'pituaartes',
  /** E-mail de contato. Vazio = não aparece. */
  email: 'contato@pituaartes.com.br',
  /** Nome da artista, como deve aparecer no site. Vazio = o texto se ajusta sem o nome. */
  artista: 'Nathaly',
};

/** Nome da página, para indicar a origem na mensagem do WhatsApp. */
export function paginaDe(caminho: string): string {
  const c = caminho.replace(import.meta.env.BASE_URL.replace(/\/$/, ''), '');
  if (c.startsWith('/oficinas')) return 'Oficinas';
  if (c.startsWith('/eventos')) return 'Eventos';
  if (c.startsWith('/encomendas/') && c.length > '/encomendas/'.length) return 'Peça para personalizar';
  if (c.startsWith('/encomendas')) return 'Encomendas';
  if (c.startsWith('/acervo/') && c.length > '/acervo/'.length) return 'Peça do acervo';
  if (c.startsWith('/acervo')) return 'Acervo';
  return 'Página inicial';
}

/** Link do WhatsApp com mensagem pronta. */
export function linkWhatsapp(mensagem: string): string {
  const texto = encodeURIComponent(mensagem);
  return site.whatsapp
    ? `https://wa.me/${site.whatsapp}?text=${texto}`
    : `https://wa.me/?text=${texto}`;
}
