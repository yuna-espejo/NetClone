# NetClone 🔁

> **Status: Work in Progress** — actively in development.

A local tool that helps you configure a new router with the same settings (SSID and password) as your old one — so all your connected devices (smart home, phones, laptops) stay connected without manual reconfiguration.

---

## The Problem

When you replace a home router, every device on your network loses its connection. You have to manually reconnect each one — phones, smart TVs, thermostats, cameras, speakers. It's tedious and error-prone, especially with IoT devices that have no screen.

NetClone solves this by reading the configuration from your old router and automatically applying it to the new one.

---

## How It Works

1. **Detects your network** — automatically finds your router's IP address
2. **Reads your old router's config** — logs into the admin panel and extracts SSID, password, and settings
3. **Applies config to the new router** — uses a recipe system (one JSON file per router model) to navigate the new router's admin panel and configure it identically

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python + Flask |
| Browser automation | Playwright (Chromium) |
| Network detection | subprocess (system routing table) |
| Router recipes | JSON |
| Frontend | HTML + CSS + JavaScript |

---

## Project Structure

```
NetClone/
├── app/
│   ├── network.py        # Auto-detects gateway IP
│   ├── routes/           # Flask API endpoints
│   ├── recipes/          # JSON config per router model
│   ├── static/           # CSS, JS, assets
│   └── templates/        # HTML pages
└── README.md
```

---

## Current Progress

- [x] Project structure and virtual environment
- [x] Dependency installation (Flask, Playwright, psutil)
- [x] Network detection module (`network.py`)
- [ ] Flask server setup
- [ ] Router login automation
- [ ] Recipe system (TP-Link, Movistar, Vodafone...)
- [ ] Frontend UI
- [ ] First end-to-end test

---

## Supported Routers (Planned)

Starting with the most common routers in Spain:
- TP-Link Archer series
- Movistar HGU
- Vodafone router
- Orange Livebox

---

## Getting Started

```bash
# Clone the repo
git clone https://github.com/yuna-espejo/NetClone.git
cd NetClone

# Create and activate virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux

# Install dependencies
pip install flask playwright psutil
python -m playwright install chromium
```

---

## Author

**Yuna Espejo** — Junior Consultant @ Timestamp Group  
[yunaespejo.com](https://yunaespejo.com) · [GitHub](https://github.com/yuna-espejo)