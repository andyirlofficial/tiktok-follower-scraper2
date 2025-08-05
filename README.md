# TikTok Follower Scraper (Playwright Version)

Scrapes the TikTok follower count for `@andyirlofficial` using a headless browser and serves it at `/followers.json`, updated every 5 seconds.

## Setup

### 1. Install dependencies
```bash
pip install -r requirements.txt
playwright install
```

### 2. Run the app
```bash
python main.py
```

## Endpoint
http://localhost:5000/followers.json

## Deployment
Use Railway.app or a VPS that supports headless Chromium.