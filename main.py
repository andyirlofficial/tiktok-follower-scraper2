from flask import Flask, jsonify
from apscheduler.schedulers.background import BackgroundScheduler
from playwright.sync_api import sync_playwright
import re

app = Flask(__name__)

follower_data = {"username": "andyirlofficial", "followers": 0}

def get_follower_count():
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            page.goto("https://www.tiktok.com/@andyirlofficial", timeout=60000)
            page.wait_for_timeout(5000)
            html = page.content()
            browser.close()

            match = re.search(r'"followerCount":(\d+)', html)
            if match:
                return int(match.group(1))
    except Exception as e:
        print("Error scraping follower count:", e)
    return 0

def update_followers():
    try:
        count = get_follower_count()
        if count > 0:
            follower_data["followers"] = count
            print("Updated follower count:", count)
    except Exception as e:
        print("Update failed:", e)

scheduler = BackgroundScheduler()
scheduler.add_job(update_followers, 'interval', seconds=5)
scheduler.start()

@app.route("/followers.json")
def get_followers():
    return jsonify(follower_data)

if __name__ == "__main__":
    update_followers()
    app.run(host="0.0.0.0", port=5000)