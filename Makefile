TS_HOST := $(shell tailscale status --json 2>/dev/null | python3 -c "import sys,json; print(json.load(sys.stdin).get('Self',{}).get('DNSName','').rstrip('.'))" 2>/dev/null)
PORT := 3030

.PHONY: dev presenter funnel serve info stop

## Start dev server (local only)
dev:
	pnpm dev

## Start presenter mode with remote sync
presenter:
	pnpm presenter

## Set up Tailscale Funnel
funnel:
	@if [ -z "$(TS_HOST)" ]; then echo "Error: Tailscale not running"; exit 1; fi
	tailscale funnel $(PORT)

## Start presenter + funnel together
serve: info
	@echo ""
	@echo "Run 'make funnel' in another terminal to enable Tailscale Funnel"
	@echo ""
	pnpm presenter

## Show all URLs
info:
	@echo "Port: $(PORT)"
	@echo ""
	@echo "Local:     http://localhost:$(PORT)/"
	@echo "Presenter: http://localhost:$(PORT)/presenter/"
	@if [ -n "$(TS_HOST)" ]; then \
		echo "Funnel:    https://$(TS_HOST)/"; \
	fi

## Stop Tailscale Funnel
stop:
	tailscale funnel --https=443 off
	@echo "Funnel stopped"
