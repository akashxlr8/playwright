import pytest
from playwright.sync_api import Page, expect

def test_github_login_page(page: Page):
    """Test GitHub login page interaction"""
    # Navigate to GitHub login page
    page.goto('https://github.com/login')
    
    # Wait for the page to load
    page.wait_for_load_state('networkidle')
    
    # Verify we're on the login page
    expect(page).to_have_title("Sign in to GitHub · GitHub")
    
    # Fill in the login form (using placeholder credentials)
    page.get_by_label("Username or email address").fill("test_username")
    page.get_by_label("Password").fill("test_password")
    
    # Add a small delay to see the form being filled
    page.wait_for_timeout(2000)  # 2 seconds
    
    # Note: We're not actually clicking submit to avoid failed login attempts
    # If you want to test actual login, replace with real credentials
    print("Login form filled successfully!")
    
    # Verify the form elements are present
    expect(page.get_by_label("Username or email address")).to_be_visible()
    expect(page.get_by_label("Password")).to_be_visible()
    expect(page.get_by_role("button", name="Sign in")).to_be_visible()