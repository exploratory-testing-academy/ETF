## Python Playwright for Exploratory Testing Foundations Course

Install instructions: https://playwright.dev/python/docs/intro

`python -m venv --copies .env`

`pip install playwright`

`playwright install`

`pip install -r requirements.txt`

### Run browser visible

`pytest --headed`

### Run on these browsers

`pytest --browser chromium --browser webkit --browser firefox`

### Run slower to see

`pytest --slowmo 100`

### Capture video

`pytest --video on`

### Capture screenshots on fail

`pytest --screenshot only-on-failure`

### Define base url

`pytest --base-url http://localhost:8080`
