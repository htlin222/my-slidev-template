import { defineConfig } from 'vite'

export default defineConfig({
  base: process.env.SLIDEV_BASE || '/',
  server: {
    allowedHosts: ['hsieh-tingmac-mini.tail33af84.ts.net'],
  },
})
