# SmartPWA Converter 🚀

<img width="1024" height="1024" alt="image" src="https://github.com/user-attachments/assets/47c9ea13-8575-49cd-b41b-7bb797048653" />


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
```

No pip install required — just run the script directly or import it as a library.

---

## 🚀 Usage

### Convert Project
```bash
python smart_pwa_converter.py convert D:/Experimental_project/ProVisionFocus --model gpt-4 --api-key YOUR_API_KEY
```

### Package Project
```bash
python smart_pwa_converter.py package D:/Experimental_project/ProVisionFocus D:/Experimental_project/Output_projects
```

### Deploy to GitHub Pages
```bash
python smart_pwa_converter.py deploy-github https://github.com/username/provisionfocus.git D:/Experimental_project/Output_projects/dist
```

### Deploy to Google Drive
```bash
python smart_pwa_converter.py deploy-drive YOUR_FOLDER_ID D:/Experimental_project/Output_projects/dist.zip --api-key YOUR_GOOGLE_API_KEY
```

---

## 🔑 API Key Setup
You can pass your API key via `--api-key` or set it as an environment variable:

```bash
export OPENAI_API_KEY=your_key_here   # Linux/Mac
setx OPENAI_API_KEY your_key_here     # Windows
```

---

## 🌍 Why SmartPWA?
Many projects fail to run properly even after `npm install` and `npm run dev`, leaving developers stuck with blank pages. SmartPWA Converter eliminates repetitive debugging tasks by automatically repairing or simulating a working baseline, ensuring your app is always ready to be converted into a PWA and deployed.

---

## 📜 License
MIT License — free to use, modify, and distribute.

---

## 🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.
```

---

This README gives you a **professional GitHub landing page** with installation, usage, and deployment instructions.  

👉 Do you want me to also add **badges** (like build status, license, Python version) at the top so it looks even more polished when published?
