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

            time.sleep(2)  # Wait for any potential redirects
            
            # Verify the login was successful by checking for a specific element
            if page.get_by_role("button", name="Logout").is_visible():
                print("✅ Login successful! Profile button is visible.")
                
                # Navigate to the new URL
                compliance_url = site + "/compliance"
                print(f"🚀 Navigating to {compliance_url}...")
                page.goto(compliance_url)
                page.wait_for_load_state('networkidle')
                print("✅ Compliance page loaded successfully!")

                # Type in the search space and click on first result
                try:
                    print("📝 Typing 'John doe' into the search space...")
                    search_input = page.get_by_placeholder("Search Patient Name or Phone Number")
                    search_input.fill("John doe")
                    
                    # Wait for dropdown results to appear
                    time.sleep(2)
                    
                    # Click on the first result in the dropdown
                    print("🖱️ Selecting the first item from dropdown...")
                    first_result = page.get_by_role("tooltip").first
                    first_result.click()
                    print("✅ First search result selected!")
                    
                    # Wait for the page to load after selection
                    page.wait_for_load_state('networkidle')
                    time.sleep(2)

                    try:
                        print("🔎 Looking for 'BP' heading and its 'History' button...")
                        # Locate the "BP" heading (assuming it's an h6, h5, or similar)
                        bp_heading = page.locator("text=BP").first
                        if bp_heading.is_visible():
                            # Find the "History" button within the same section/card as "BP"
                            # This assumes the button is near the heading in the DOM
                            history_button = bp_heading.locator("..").locator("button:has-text('History')").first
                            if not history_button.is_visible():
                                # If not found, try searching a bit higher in the DOM
                                history_button = bp_heading.locator("..").locator("..").locator("button:has-text('History')").first
                            if history_button.is_visible():
                                history_button.click()
                                print("✅ Clicked the 'History' button inside the 'BP' section!")
                            else:
                                print("❌ Could not find the 'History' button near the 'BP' heading.")
                        else:
                            print("❌ Could not find the 'BP' heading.")
                    except Exception as e:
                        print(f"❌ Error while trying to click 'History' button in 'BP' section: {e}")

                    # Find and click the copy button near the "Unchecked Compliances Summary" field
                    try:
                        print("📊 Looking for 'Unchecked Compliances Summary' field...")
                        # Wait to ensure the page is loaded
                        time.sleep(2)
                        
                        # First, try to find a section containing "Unchecked Compliances Summary" text
                        page.wait_for_selector('text="Unchecked Compliances Summary"', timeout=10000)
                        print("✅ Found the Unchecked Compliances Summary section")
                        
                        # Try to find the copy button with the class you provided and click it
                        copy_button = page.locator('.MuiButtonBase-root.MuiIconButton-root.MuiIconButton-colorPrimary.MuiIconButton-sizeMedium.css-175iuzg').first
                        
                        if copy_button.is_visible():
                            print("✅ Found the copy button")
                            copy_button.click()
                            print("✅ Clicked the copy button - text copied to clipboard!")
                            # Note: Text is now in clipboard but we can't access clipboard content directly with Playwright
                            
                            # Try to get the actual text from nearby elements
                            try:
                                # Try to get the text from an element near the button
                                summary_text = page.locator('text="Unchecked Compliances Summary"').locator('..').locator('..').text_content()
                                print(f"📋 Unchecked Compliances Summary content: {summary_text}")
                            except:
                                print("⚠️ Copied to clipboard but couldn't extract text to display in console")
                        else:
                            print("⚠️ Copy button not visible")
                    except Exception as e:
                        print(f"❌ Could not find or interact with the 'Unchecked Compliances Summary' field. Error: {e}")
                except Exception as e:
                    print(f"❌ Could not find the search input with placeholder 'Search Patient Name or Phone Number'. Error: {e}")

            else:
                print("❌ Login verification failed. Could not find profile button.")
            
            # Keep the browser open for a few more seconds
            print("🕒 Keeping browser open for 10 more seconds to observe...")
            time.sleep(10)
            
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
