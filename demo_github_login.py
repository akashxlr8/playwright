#!/usr/bin/env python3
"""
Simple script to demonstrate GitHub login automation with visible browser
Run this script to see Playwright in action with a visible browser window
"""

from playwright.sync_api import sync_playwright
import time

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
        
        try:
            print("🚀 Opening GitHub login page...")
            page.goto('https://github.com/login')
            
            # Wait for the page to load
            page.wait_for_load_state('networkidle')
            print("✅ Page loaded successfully!")
            
            # Wait a bit for visual confirmation
            time.sleep(2)
            
            print("📝 Filling in the username field...")
            page.get_by_label("Username or email address").fill("demo_username")
            
            time.sleep(1)  # Pause to see the action
            
            print("🔒 Filling in the password field...")
            page.get_by_label("Password").fill("demo_password")
            
            time.sleep(2)  # Pause to see the filled form
            
            print("👀 Form filled! You can see the browser in action.")
            print("⚠️  Note: We're not clicking submit to avoid failed login attempts.")
            
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
    print("🎭 Playwright GitHub Login Demo")
    print("=" * 40)
    run_github_login_demo()
