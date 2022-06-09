# ClickShare Warranty Test with Python
This repository contains the test project for the basic Web UI Testing with Python in collaboration with Automation on June 09, 2022.
Test strategy is described in the /tests/test_plan.md

## Repo
    > git clone https://github.com/EuxineTL/clickshare_warranty.git
    > cd clickshare_warranty

## Setup
This project requires Python 3.

To set up the Python environment and install dependencies, run:
    > pip install pipenv
    > pipenv install
    > pipenv install -r requirements.txt

Download the WebDriver and extract it to a directory in PATH, below use /usr/bin as an example
    > curl https://chromedriver.storage.googleapis.com/102.0.5005.61/chromedriver_linux64.zip -o chromedriver_linux64.zip
    > sudo unzip -o chromedriver_linux64.zip -d /usr/bin

## Run Tests
To run tests, run the following command from the project's root directory:
    > pipenv run python3 -m pytest

## Remove Virtual Env
    > pipenv --rm

## Todo 
- support more browsers
- Automate the WebDriver download
- CrossBrowserTesting
