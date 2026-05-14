# Playwright Pytest Framework

Automation testing framework built using:
- Python
- Pytest
- Playwright

## Project Structure

```text
pages/      -> Page Object Model files
tests/      -> Test cases
utils/      -> Utility/helper files
conftest.py -> Pytest fixtures and setup
```

## Setup Instructions

### Clone Repository

```bash
git clone https://github.com/Bogyam/playwright-pytest-framework
```

### Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Install Playwright Browsers

```bash
playwright install
```

### Run Tests

```bash
pytest
```
