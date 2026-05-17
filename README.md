# NetClone 🔁

> **Status: Work in Progress** — actively in development.

A local tool for when you switch internet provider and get a new router. You already know your old SSID and password — NetClone automatically detects the new router's IP, opens its admin panel, and applies your credentials. Every device on your network reconnects without any manual reconfiguration.

---

## The Problem

When you switch provider, your new router comes with a different SSID and password. Every device in your home — phones, smart TVs, thermostats, cameras, speakers — loses its connection. You have to reconfigure each one manually.

NetClone eliminates that. You tell it your old SSID and password, it does the rest.

---

## How It Works

1. **Detects your new router's IP** — automatically reads the system routing table, no manual input needed
2. **Opens the admin panel** — uses Playwright to navigate the router's web interface
3. **Applies your credentials** — sets the SSID and password you provide, using a recipe specific to your router model

You stay in control. If you want to change the password while you're at it, just type a new one.

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