import type { APIRoute } from 'astro';
import { pecas } from '../data/pecas';

export const GET: APIRoute = ({ site }) => {
  const base = import.meta.env.BASE_URL.replace(/\/$/, '');
  const caminhos = ['/', '/acervo/', '/oficinas/', '/encomendas/', ...pecas.map((p) => `/acervo/${p.slug}/`)];
  const urls = caminhos.map((c) => `  <url><loc>${new URL(base + c, site)}</loc></url>`).join('\n');
  return new Response(
    `<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n${urls}\n</urlset>\n`,
    { headers: { 'Content-Type': 'application/xml; charset=utf-8' } },
  );
};
