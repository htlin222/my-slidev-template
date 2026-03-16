#!/usr/bin/env python3
"""Image utility server for gallery browsing and interactive cropping."""

import base64
import json
import subprocess
import webbrowser
from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parent.parent
IMAGES_DIR = ROOT / "public" / "images"
SLIDES_FILE = ROOT / "slides.md"
HTML_FILE = Path(__file__).resolve().parent / "imageutil.html"
PORT = 8765


def get_image_info(path: Path) -> dict:
    """Get image metadata using magick identify."""
    info = {"name": path.name, "size": path.stat().st_size}
    try:
        out = subprocess.check_output(
            ["magick", "identify", "-format", "%w %h", str(path)],
            stderr=subprocess.DEVNULL,
            text=True,
        ).strip()
        w, h = out.split()[:2]
        info["width"], info["height"] = int(w), int(h)
    except Exception:
        info["width"], info["height"] = 0, 0
    info["hasBackup"] = path.with_suffix(".original.png").exists()
    return info


def parse_slides_refs() -> list[dict]:
    """Parse slides.md for image references with line numbers."""
    refs = []
    if not SLIDES_FILE.exists():
        return refs
    import re

    pattern = re.compile(r'<img\s+src="/images/([^"]+)"')
    for i, line in enumerate(SLIDES_FILE.read_text().splitlines(), 1):
        m = pattern.search(line)
        if m:
            refs.append({"filename": m.group(1), "line": i, "context": line.strip()})
    return refs


class Handler(SimpleHTTPRequestHandler):
    def do_GET(self):
        path = unquote(self.path.split("?")[0])

        if path == "/":
            self._serve_file(HTML_FILE, "text/html")
        elif path == "/api/images":
            images = sorted(IMAGES_DIR.glob("*.png"))
            # Exclude .original.png backups
            images = [p for p in images if not p.name.endswith(".original.png")]
            data = [get_image_info(p) for p in images]
            self._json_response(data)
        elif path.startswith("/api/image/"):
            fname = path[len("/api/image/") :]
            fpath = IMAGES_DIR / fname
            if fpath.exists() and fpath.parent == IMAGES_DIR:
                self._serve_file(fpath, "image/png")
            else:
                self.send_error(404)
        elif path == "/api/slides":
            self._json_response(parse_slides_refs())
        else:
            self.send_error(404)

    def do_POST(self):
        path = unquote(self.path)
        length = int(self.headers.get("Content-Length", 0))
        body = json.loads(self.rfile.read(length)) if length else {}

        if path == "/api/crop":
            fname = body.get("filename", "")
            image_data = body.get("imageData", "")
            fpath = IMAGES_DIR / fname
            if not fpath.exists() or fpath.parent != IMAGES_DIR:
                self._json_response({"error": "Invalid file"}, 400)
                return
            # Backup original (only first time)
            backup = fpath.with_suffix(".original.png")
            if not backup.exists():
                fpath.rename(backup)
                # We need to write the new file at fpath
            # Decode and write cropped image
            raw = base64.b64decode(image_data.split(",")[-1])
            fpath.write_bytes(raw)
            self._json_response({"ok": True, "backup": backup.name})

        elif path == "/api/restore":
            fname = body.get("filename", "")
            fpath = IMAGES_DIR / fname
            backup = fpath.with_suffix(".original.png")
            if not backup.exists() or fpath.parent != IMAGES_DIR:
                self._json_response({"error": "No backup found"}, 400)
                return
            if fpath.exists():
                fpath.unlink()
            backup.rename(fpath)
            self._json_response({"ok": True})
        else:
            self.send_error(404)

    def _serve_file(self, filepath: Path, content_type: str):
        data = filepath.read_bytes()
        self.send_response(200)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", len(data))
        self.send_header("Cache-Control", "no-cache")
        self.end_headers()
        self.wfile.write(data)

    def _json_response(self, data, code=200):
        body = json.dumps(data).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", len(body))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, fmt, *args):
        print(f"  {args[0]}")


if __name__ == "__main__":
    print(f"Serving at http://localhost:{PORT}")
    webbrowser.open(f"http://localhost:{PORT}")
    HTTPServer(("", PORT), Handler).serve_forever()
