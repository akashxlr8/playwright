import pytest
from playwright.sync_api import Browser

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    """Configure browser context for better debugging"""
    return {
        **browser_context_args,
        "viewport": {"width": 1280, "height": 720},
        "ignore_https_errors": True,
    }

@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args):
    """Configure browser launch arguments for non-headless mode"""
    return {
        **browser_type_launch_args,
        "headless": False,  # Show the browser
        "slow_mo": 500,     # Slow down actions by 500ms
        "args": [
            "--start-maximized",
            "--disable-web-security",
            "--disable-features=VizDisplayCompositor"
        ]
    }
