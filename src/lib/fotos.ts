import type { ImageMetadata } from 'astro';

const arquivos = import.meta.glob<{ default: ImageMetadata }>('/src/assets/pecas/*/*.{jpg,jpeg,png,webp}', {
  eager: true,
});
const editoriais = import.meta.glob<{ default: ImageMetadata }>('/src/assets/editorial/*.{jpg,jpeg,png,webp}', {
  eager: true,
});

const porPeca = new Map<string, ImageMetadata[]>();
for (const caminho of Object.keys(arquivos).sort()) {
  const slug = caminho.split('/').at(-2)!;
  const lista = porPeca.get(slug) ?? [];
  lista.push(arquivos[caminho].default);
  porPeca.set(slug, lista);
}

/** Todas as fotos de uma peça, na ordem dos nomes dos arquivos. */
export function fotosDa(slug: string): ImageMetadata[] {
  const fotos = porPeca.get(slug);
  if (!fotos?.length) throw new Error(`Nenhuma foto encontrada em src/assets/pecas/${slug}/`);
  return fotos;
}

/** Uma foto específica de uma peça (1 = capa). */
export function foto(slug: string, n = 1): ImageMetadata {
  const fotos = fotosDa(slug);
  return fotos[Math.min(n, fotos.length) - 1];
}

/** Fotos editoriais (retratos, ambientes) por nome de arquivo, sem extensão. */
export function editorial(nome: string): ImageMetadata {
  const chave = Object.keys(editoriais).find((c) => c.split('/').at(-1)!.startsWith(nome + '.'));
  if (!chave) throw new Error(`Foto editorial não encontrada: ${nome}`);
  return editoriais[chave].default;
}
