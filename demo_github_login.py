#!/usr/bin/env python3
"""
Simple script to demonstrate GitHub login automation with visible browser
Run this script to see Playwright in action with a visible browser window
"""

from playwright.sync_api import sync_playwright
import time
from dotenv import load_dotenv
import os
# Load environment variables from .env file
load_dotenv()
def run_github_login_demo():
    with sync_playwright() as p:
        # Launch browser in non-headless mode
        browser = p.chromium.launch(
            headless=False,  # Show the browser
            slow_mo=1000,    # Slow down actions by 1 second
            args=[
                "--start-maximized",
                "--disable-web-security"
            ]
        )
        
        # Create a new browser context
        context = browser.new_context(
            viewport={"width": 1280, "height": 720}
        )
        
        # Create a new page
        page = context.new_page()
        site = os.getenv("site")
        try:
            print("🚀 Opening website login page...")
            page.goto(site + '/login')

            # Wait for the page to load
            page.wait_for_load_state('networkidle')
            print("✅ Page loaded successfully!")
            
            # Wait a bit for visual confirmation
            time.sleep(2)
            
            print("📝 Filling in the username field...")
            page.get_by_label("Username").fill(os.getenv("user"))
            
            time.sleep(1)  # Pause to see the action
            
            print("🔒 Filling in the password field...")
            page.get_by_label("Password").fill(os.getenv("password"))
            
            time.sleep(2)  # Pause to see the filled form
            
            print("👀 Form filled! You can see the browser in action.")
            # print("⚠️  Note: We're not clicking submit to avoid failed login attempts.")

            page.get_by_role("button", name="Login").click()


            
            # Keep the browser open for a few more seconds
            print("🕒 Keeping browser open for 5 more seconds...")
            time.sleep(5)
            
            print("✨ Demo completed!")
            
        except Exception as e:
            print(f"❌ Error occurred: {e}")
        
        finally:
            # Clean up
            browser.close()

if __name__ == "__main__":
    print("🎭 Playwright website Login Demo")
    print("=" * 40)
    run_github_login_demo()
