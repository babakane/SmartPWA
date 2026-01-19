#!/usr/bin/env python3
"""
smart_pwa_converter.py

A single-file Python library to:
1. Detect if a project (React, Vue, static HTML, etc.) is valid and runs properly.
2. Convert it into a Progressive Web App (PWA).
3. If the project fails (blank page, broken build), use AI-assisted simulation
   to scaffold or repair the project before conversion.
4. Package the converted project into a distributable format.

Note: AI simulation is a placeholder — you can plug in your preferred model/API.
"""

import os
import subprocess
import json
import shutil
import zipfile
import venv
from pathlib import Path
from typing import Optional, Tuple

# -----------------------------
# Utility Functions
# -----------------------------

def analyze_project(project_path: str) -> Tuple[str, bool]:
    """
    Detect framework and check if project runs properly.
    Returns (framework, status).
    """
    root = Path(project_path).resolve()
    if not root.exists():
        return ("unknown", False)

    # Detect framework
    if (root / "package.json").exists():
        pkg = json.loads((root / "package.json").read_text(encoding="utf-8"))
        deps = pkg.get("dependencies", {})
        if "react" in deps:
            framework = "react"
        elif "vue" in deps:
            framework = "vue"
        else:
            framework = "node"
    elif (root / "index.html").exists():
        framework = "static"
    else:
        framework = "unknown"

    # Try to run build/dev check (simplified)
    try:
        if framework in ("react", "vue", "node"):
            subprocess.run(["npm", "install"], cwd=root, check=True)
            subprocess.run(["npm", "run", "build"], cwd=root, check=True)
        elif framework == "static":
            # Static HTML always "works"
            return (framework, True)
    except Exception:
        return (framework, False)

    return (framework, True)

def simulate_project_with_ai(project_path: str, model: str, api_key: str) -> bool:
    """
    Placeholder for AI-assisted simulation.
    - Could call an external API to scaffold a minimal working project.
    - For now, just creates a dummy index.html if missing.
    """
    root = Path(project_path).resolve()
    index = root / "index.html"
    if not index.exists():
        index.write_text("<!DOCTYPE html><html><head><title>Simulated Project</title></head><body><h1>Hello PWA</h1></body></html>")
    return True

def convert_to_pwa(project_path: str, model: Optional[str] = None, api_key: Optional[str] = None) -> Tuple[bool, str]:
    """
    Convert project into PWA.
    - Detect framework.
    - Validate project runs.
    - If fails, simulate with AI.
    - Add manifest.json, service-worker.js, inject into index.html.
    """
    framework, status = analyze_project(project_path)
    if not status:
        if model and api_key:
            simulate_project_with_ai(project_path, model, api_key)
        else:
            return False, f"Project {framework} failed to run. Provide model+API key for AI simulation."

    root = Path(project_path).resolve()
    manifest = {
        "name": "Smart PWA App",
        "short_name": "SmartPWA",
        "start_url": ".",
        "display": "standalone",
        "background_color": "#ffffff",
        "theme_color": "#1a73e8",
        "description": "Auto-converted Progressive Web App",
        "icons": [
            {"src": "icons/icon-192.png", "sizes": "192x192", "type": "image/png"},
            {"src": "icons/icon-512.png", "sizes": "512x512", "type": "image/png"}
        ]
    }
    (root / "manifest.json").write_text(json.dumps(manifest, indent=2))

    sw = """
    self.addEventListener('install', e => {
      e.waitUntil(caches.open('pwa-cache').then(cache => cache.addAll(['/'])));
    });
    self.addEventListener('fetch', e => {
      e.respondWith(fetch(e.request).catch(() => caches.match(e.request)));
    });
    """
    (root / "service-worker.js").write_text(sw)

    index = root / "index.html"
    if index.exists():
        html = index.read_text()
        if "manifest.json" not in html:
            html = html.replace("<head>", "<head>\n<link rel='manifest' href='/manifest.json'>")
        if "serviceWorker.register" not in html:
            html = html.replace("</body>", "<script>navigator.serviceWorker.register('/service-worker.js');</script></body>")
        index.write_text(html)

    return True, f"PWA conversion complete for {framework} project at {root}"

def package_pwa(project_path: str, output_path: str, create_virtualenv: bool = True, zip_dist: bool = True) -> Tuple[bool, str]:
    """
    Package project into dist folder.
    """
    src = Path(project_path).resolve()
    out = Path(output_path).resolve()
    dist = out / "dist"
    if dist.exists():
        shutil.rmtree(dist)
    shutil.copytree(src, dist, ignore=shutil.ignore_patterns("node_modules", "build", "dist", ".git"))

    if create_virtualenv:
        venv_dir = out / "venv"
        venv.EnvBuilder(with_pip=True).create(venv_dir)

    if zip_dist:
        zip_path = out / "dist.zip"
        with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
            for root_dir, _, files in os.walk(dist):
                for f in files:
                    full = Path(root_dir) / f
                    rel = full.relative_to(dist)
                    zf.write(full, rel.as_posix())

    return True, f"Packaging complete. Dist folder: {dist}, venv: {out / 'venv'}, zip: {out / 'dist.zip'}"
