# Python Selenium Pytest Automation Framework

## Project Overview

This is a Python-based Selenium Automation Framework developed using Pytest. The framework is designed to automate Web UI, REST API, and Database testing by following industry-standard automation practices.

It supports Page Object Model (POM), Data Driven Testing, Cross Browser Execution, Environment Configuration, Logging, HTML Reporting, Screenshot Capture, and Jenkins Integration.


## Tech Stack

- **Programming Language:** Python 3.14
- **Automation Tool:** Selenium WebDriver
- **Testing Framework:** Pytest
- **API Testing:** Requests
- **Database:** MySQL
- **Data Driven Testing:** Excel (OpenPyXL), JSON
- **Reporting:** Pytest HTML Report
- **Logging:** Python Logging
- **CI/CD:** Jenkins
- **IDE:** PyCharm
- **Version Control:** Git & GitHub


## Project Structure

```text
python-selenium-pytest-framework/
│
├── config/
│   ├── config.py
│   ├── qa_config.py
│   ├── uat_config.py
│   └── prod_config.py
│
├── logs/
│   └── framework.log
│
├── pages/
│   ├── __init__.py
│   └── login_page.py
│
├── reports/
│
├── screenshots/
│
├── testdata/
│   ├── login_data.json
│   └── login_data.xlsx
│
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_login.py
│   ├── test_api.py
│   └── db_test_skip.py
│
├── utilities/
│   ├── api_assertions.py
│   ├── api_client.py
│   ├── base_page.py
│   ├── db_utility.py
│   ├── excel_reader.py
│   ├── json_reader.py
│   ├── logger.py
│   ├── screenshot_utils.py
│   └── wait_utils.py
│
├── pytest.ini
├── requirements.txt
├── .gitignore
└── README.md
```


## Features

- Page Object Model (POM)
- Selenium WebDriver Automation
- REST API Automation (GET, POST, PUT, DELETE)
- Data Driven Testing using Excel and JSON
- Cross Browser Testing (Chrome, Edge, Firefox)
- Environment Support (QA, UAT, PROD)
- Explicit Wait Utilities
- Screenshot Capture on Test Failure
- Logging Framework
- HTML Report Generation
- Database Utility (MySQL)
- Jenkins CI Integration
- Browser & Environment Parameterization
- Reusable Utility Classes


## How to Run

### 1. Clone the Repository

```bash
git clone <your-github-repository-url>
cd python-selenium-pytest-framework
```

### 2. Create Virtual Environment

```bash
python -m venv .venv
```

### 3. Activate Virtual Environment

**Windows**

```bash
.venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Execute UI Tests

```bash
pytest tests/test_login.py --browser chrome --env qa
```

### 6. Execute API Tests

```bash
pytest tests/test_api.py
```

### 7. Execute All Tests

```bash
pytest -v -s --browser chrome --env qa --html=reports/report.html
```


## Jenkins Integration

The framework is integrated with Jenkins for Continuous Integration.

Features:
- Execute tests from Jenkins
- Browser Parameterization
- Environment Parameterization
- Automatic HTML Report Generation
- Build History
- Console Logs


## 🚀 Future Enhancements

- Docker Integration
- GitHub Actions CI/CD Pipeline
- Allure Reporting
- Cross Browser Execution using Selenium Grid
- Parallel Test Execution
- Database Validation
- Email Report Integration
- Cloud Execution (BrowserStack / Sauce Labs)

---

## 👨‍💻 Author

**Gowtham S**

QA Automation Engineer | Python | Selenium | Pytest | API Testing | Jenkins | SQL

If you found this project useful, feel free to ⭐ the repository.

