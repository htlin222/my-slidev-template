import { defineConfig } from 'vite'
import { execSync } from 'node:child_process'

function getTailscaleHost(): string | undefined {
  try {
    const json = execSync('tailscale status --json 2>/dev/null', { encoding: 'utf-8' })
    return JSON.parse(json)?.Self?.DNSName?.replace(/\.$/, '')
  } catch {
    return undefined
  }
}

const tsHost = getTailscaleHost()

export default defineConfig({
  server: {
    allowedHosts: tsHost ? [tsHost] : [],
  },
})
