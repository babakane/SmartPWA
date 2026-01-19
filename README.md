# SmartPWA Converter 🚀

SmartPWA Converter is a Python library and CLI tool that automatically transforms web projects into Progressive Web Apps (PWAs).  
It intelligently detects your project type (React, Vue, static HTML, or Node), validates builds, applies AI-powered fallback scaffolding if the project fails, and packages the result for deployment.

With built-in deployment helpers, you can publish directly to **GitHub Pages** or **Google Drive** for instant hosting.

---

## ✨ Features
- 🔍 **Framework Detection**: Identifies React, Vue, Node, or static HTML projects.
- ✅ **Validation**: Runs build checks to confirm the project works before conversion.
- 🤖 **AI Fallback**: If the project fails, scaffolds a minimal working app (React by default).
- 📦 **Packaging**: Creates a `dist/` folder, virtual environment, and zip archive for distribution.
- 🌐 **Deployment**: Pushes directly to GitHub Pages or uploads to Google Drive.
- 🔑 **Secure API Key Handling**: Accept API keys via environment variables or CLI arguments.
- 🧪 **Testing Hooks**: Optional local server checks to confirm service worker registration and manifest loading.

---

## 📦 Installation
Clone the repository:
```bash
git clone https://github.com/username/smartpwa-converter.git
cd smartpwa-converter
