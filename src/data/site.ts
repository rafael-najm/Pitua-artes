/**
 * Dados de contato e textos gerais do site.
 * Preencha os campos vazios — o site se ajusta sozinho.
 */
export const site = {
  nome: 'Pitua',
  assinatura: 'Arte em porcelana',
  descricao:
    'Porcelana pintada à mão. Peças únicas, encomendas personalizadas e oficinas criativas.',

  /** Número com DDI e DDD, só dígitos. Ex.: '5521999998888'. Vazio = WhatsApp abre para escolher o contato. */
  whatsapp: '',
  /** Usuário do Instagram, sem @. Ex.: 'pitua.artes'. Vazio = não aparece. */
  instagram: '',
  /** E-mail de contato. Vazio = não aparece. */
  email: '',
  /** Nome da artista, como deve aparecer no site. Vazio = o texto se ajusta sem o nome. */
  artista: '',
};

/** Link do WhatsApp com mensagem pronta. */
export function linkWhatsapp(mensagem: string): string {
  const texto = encodeURIComponent(mensagem);
  return site.whatsapp
    ? `https://wa.me/${site.whatsapp}?text=${texto}`
    : `https://wa.me/?text=${texto}`;
}
