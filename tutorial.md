Great — here’s a ready‑to‑drop **`docs/tutorials.md`** file in full Markdown format for your repository. It contains multiple real‑world examples of using your SmartPWA Converter:

---

```markdown
# 📚 SmartPWA Converter Tutorials

This guide provides real‑world examples of how to use **SmartPWA Converter** to transform projects into Progressive Web Apps (PWAs), package them, and deploy them to hosting platforms.

---

## 1. Convert a React Project into a PWA
**Scenario:** You have a React app in `D:/Projects/MyReactApp`.

```bash
# Step 1: Convert project into PWA
python smart_pwa_converter.py convert D:/Projects/MyReactApp --model gpt-4 --api-key YOUR_API_KEY

# Step 2: Package project
python smart_pwa_converter.py package D:/Projects/MyReactApp D:/Projects/Output
```

**Result:**  
- `manifest.json` and `service-worker.js` injected into `public/index.html`.  
- Packaged app in `Output/dist/` with a zip archive ready for deployment.

---

## 2. Deploy to GitHub Pages
**Scenario:** You want to host your converted app on GitHub Pages.

```bash
# Step 1: Package project
python smart_pwa_converter.py package D:/Projects/MyReactApp D:/Projects/Output

# Step 2: Deploy dist folder to GitHub Pages
python smart_pwa_converter.py deploy-github https://github.com/username/myreactapp.git D:/Projects/Output/dist
```

**Result:**  
Your app is live at `https://username.github.io/myreactapp`.

---

## 3. Deploy to Google Drive
**Scenario:** You want to share your packaged app quickly with colleagues.

```bash
# Step 1: Package project
python smart_pwa_converter.py package D:/Projects/MyReactApp D:/Projects/Output

# Step 2: Upload zip to Google Drive
python smart_pwa_converter.py deploy-drive YOUR_FOLDER_ID D:/Projects/Output/dist.zip --api-key YOUR_GOOGLE_API_KEY
```

**Result:**  
A shareable Google Drive link to your app’s zip archive.

---

## 4. Static HTML Project Conversion
**Scenario:** You have a simple static site in `D:/Sites/Portfolio`.

```bash
python smart_pwa_converter.py convert D:/Sites/Portfolio
python smart_pwa_converter.py package D:/Sites/Portfolio D:/Sites/Output
```

**Result:**  
Your portfolio site now has offline support and can be installed as a PWA.

---

## 5. AI Fallback Example
**Scenario:** Your Vue project fails to build (blank page after `npm run dev`).

```bash
python smart_pwa_converter.py convert D:/Projects/BrokenVueApp --model gpt-4 --api-key YOUR_API_KEY
```

**Result:**  
The converter scaffolds a minimal working React app as fallback, injects PWA essentials, and ensures you don’t end up with a blank page.

