# Playwright Web Automation Learning Journey

This repository documents my learning journey into web automation using Playwright. The initial goal is to master browser automation techniques, with a long-term vision of integrating AI agents to perform complex browser-based tasks.

## Project Overview

This project serves as a hands-on environment for exploring the capabilities of Playwright for automating web interactions. It currently focuses on a simple yet practical use case: automating the login process on GitHub. This allows for experimentation with page navigation, form filling, and element interaction.

The ultimate goal is to build a foundation for more advanced projects involving AI agents that can intelligently navigate and interact with websites to perform tasks autonomously.

## Current Functionality

The repository contains two main Python scripts that demonstrate web automation:

1.  **`test_login.py`**: A test script using the `pytest` framework to automate interactions with the GitHub login page.
    - Navigates to `https://github.com/login`.
    - Fills in the username and password fields with placeholder text.
    - Verifies that the input fields and the "Sign in" button are visible.
    - This script is designed to be run as a test and is configured to run in "headed" mode (non-headless) so you can see the browser actions in real time.

2.  **`demo_github_login.py`**: A standalone demonstration script.
    - Launches a visible browser window.
    - Navigates to the GitHub login page.
    - Fills in the login credentials from a `.env` file (you'll need to create one).
    - Clicks the login button.
    - This script is ideal for showcasing the automation without needing to run the full test suite.

## Dependencies

The project relies on the following Python packages:

-   `playwright`: The core library for browser automation.
-   `pytest`: A testing framework used to structure and run the automation tests.
-   `pytest-playwright`: A `pytest` plugin that provides integration with Playwright.
-   `python-dotenv`: To manage environment variables for credentials.

## Setup and Installation

To get started with this project, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd playwright-learning
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
    ```

3.  **Install the required Python packages:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Install the Playwright browsers:**
    Playwright requires you to download browser binaries.
    ```bash
    playwright install
    ```

5.  **Create a `.env` file:**
    For the `demo_github_login.py` script, you need to provide your credentials. Create a file named `.env` in the root of the project and add the following:
    ```
    site="https://github.com"
    user="your_github_username"
    password="your_github_password"
    ```

## How to Execute the Scripts

There are a few ways to run the automation scripts:

### 1. Running the Pytest Tests

The tests are configured to run in **headed mode**, meaning you will see a browser window open and perform the actions. This is set in the `pytest.ini` and `conftest.py` files.

To run all the tests, simply execute:
```bash
pytest
```
This will discover and run the `test_login.py` script.

### 2. Running the Standalone Demo Script

The `demo_github_login.py` script can be run directly.

-   **Using Python:**
    ```bash
    python demo_github_login.py
    ```

-   **Using the Batch Script (for Windows users):**
    A `run_demo.bat` file is provided for convenience.
    ```bash
    .\run_demo.bat
    ```

## Configuration Files

-   **`pytest.ini`**: This file configures `pytest` to run tests with specific options. Here, it's set to run in `--headed` mode, use the `chromium` browser, and add a `500ms` `slowmo` to make the actions easier to follow.
-   **`conftest.py`**: This is a `pytest` configuration file that allows for more advanced customizations. It's used here to set browser arguments, such as starting maximized and setting the viewport size. This ensures the browser opens in a consistent state for tests.

---

This `README.md` should provide a comprehensive guide to understanding, setting up, and running the project. As I continue to learn and add more features, I will keep this documentation updated.
