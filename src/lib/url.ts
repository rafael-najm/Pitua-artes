/** Monta um caminho interno respeitando o `base` do site (necessário no GitHub Pages). */
const base = import.meta.env.BASE_URL.replace(/\/$/, '');

export function u(caminho: string): string {
  if (/^(https?:|mailto:|tel:|#)/.test(caminho)) return caminho;
  return `${base}${caminho.startsWith('/') ? '' : '/'}${caminho}`;
}
