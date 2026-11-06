// @ts-check
import { defineConfig } from 'astro/config';

// SITE_URL e BASE_PATH são definidos no deploy (ver .github/workflows/deploy.yml).
// Com domínio próprio (ex.: https://pitua.com.br), use BASE_PATH="/".
const site = process.env.SITE_URL || 'https://rafael-najm.github.io';
const base = process.env.BASE_PATH || '/';

export default defineConfig({
  site,
  base,
  trailingSlash: 'always',
  image: {
    // Gera variações .webp em vários tamanhos para cada foto.
    breakpoints: [480, 720, 960, 1280, 1600, 2000],
  },
  build: {
    inlineStylesheets: 'auto',
  },
});
