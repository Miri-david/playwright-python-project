
# 🎯 Playwright Python Automation Project

[![Build Status](https://img.shields.io/github/actions/workflow/status/Miri-david/playwright-python-project/ci.yml?branch=main)](https://github.com/Miri-david/playwright-python-project/actions)
[![Coverage](https://img.shields.io/codecov/c/github/Miri-david/playwright-python-project)](https://codecov.io/gh/Miri-david/playwright-python-project)
[![Allure Report](https://img.shields.io/badge/Allure-Report-blue)](https://Miri-david.github.io/playwright-python-project/)

---

## 📌 Project Overview

This is a robust **end-to-end test automation framework** built with **Playwright** and **Python**, designed to validate modern web applications with high reliability and speed.  
Below you’ll find an illustrative dashboard (generated after test runs) that visualizes success metrics, test statuses, and asset captures — offering a polished sense of test coverage and success.

---

## 🚀 Purpose

The goal of this project is to deliver:
- ⚡ Fast, **cross-browser stable E2E automation**
- 🎥 Useful artifacts: **screenshots, videos, traces**
- 📊 Professional-quality reporting with **Allure** integration
- 📈 Comprehensive coverage and results tracking for CI/CD environments

---

## 🧰 Technologies Used

Based on reviewing your codebase, this project includes:
- **Python 3.8+**, **pytest**
- **pytest-playwright** plugin
- **allure-pytest** for test reporting
- Playwright-supported browsers: **Chromium**, **Firefox**, **WebKit**
- Directory structure with **Page Object Model**
- CI integration (e.g. GitHub Actions) for **build and test pipelines**
- Code coverage reporting via **pytest-cov**/**coverage.py**

---

## 🛠️ Installation & Usage

1. **Clone repository**
   ```sh
   git clone https://github.com/Miri-david/playwright-python-project.git
   cd playwright-python-project
   ```
2. **Create & activate a virtual environment**
   ```sh
   python -m venv .venv
   source .venv/bin/activate  # or .venv\Scripts\activate on Windows
   ```
3. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   playwright install
   ```
4. **Run tests**
   ```sh
   pytest
   ```
5. **Generate Allure report**
   ```sh
   pytest --alluredir=allure-results
   allure serve allure-results
   ```

---

## 📁 Project Structure

```
/
├── tests/                   # pytest test modules
├── pages/                   # Page object models
├── fixtures/                # Pytest fixtures
├── conftest.py
├── requirements.txt
├── pytest.ini
└── ...
```

---

## ✔️ What’s Tested

The test suite covers:
- UI interactions (login, navigation, search, form submission)
- Cross-browser validation across Chromium, Firefox, WebKit
- Visual artifacts: screenshots, videos, Playwright Traces
- Test result analytics via **Allure**, including history charts, duration, flakiness, and failure breakdown

---

## 📊 Allure Report

View my project’s Allure report hosted via GitHub Pages from _Settings → Pages_.  
Here’s a preview screenshot of the report overview:

<img width="1768" height="970" alt="allurereport" src="https://github.com/user-attachments/assets/88f21f3d-ab07-4385-a214-e73d7c81e255" />
eenshot]((https://miri-david.github.io/playwright-python-project/5/index.html))

(Hit “Runs”, “History”, “Test suite” tabs for full insights.)

---

## ✅ Badges

| Badge               | Purpose                                      |
|--------------------|----------------------------------------------|
| **Build Status**    | Current CI pipeline status (passing/failing) |
| **Coverage**        | Code coverage percentage via Codecov         |
| **Allure Report**   | Direct link to live Allure test report       |

---

## 🔍 Examples & Screenshots

- ✅ Example test: `tests/test_example_login.py`
- 📸 Screenshots/videos on failure stored under `artifacts/` example: <img width="1906" height="960" alt="filureallure" src="https://github.com/user-attachments/assets/cf4375ca-9782-49ea-b6a9-458f139cb7a7" />
 
- 🔁 Each run includes a trace file — viewable in the Playwright Trace Viewer

---

## 🙌 Feedback & Contributions

If you find this repository helpful, please:
- ⭐ Give it a star
- 🗣 Share your feedback or suggestions
- 📩 Submit issues or pull requests

Feel free to connect with me on LinkedIn:  
[**Miri David**](https://www.linkedin.com/in/miri-david-profile/)

---

## 🎓 About My Automation Academy

Learn more about the automation methodologies I teach at:  
[https://automation.co.il/](https://automation.co.il/)

---

Thank you for checking out this project! I hope it inspires trust in automation quality and drives your CI/CD confidence. Happy testing! 🚀

