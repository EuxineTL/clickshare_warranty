---
tags: BARCO, SDET, Python, Gherkin, BDD, Pytest, Selenium
---
# test_plan

## Web UI Test
- URL: [ClickShare Warranty Info](https://www.barco.com/en/clickshare/support/warranty-info)
- Scenario: Get ClickShare warranty info
    1. ==Given== `Check your ClickShare warranty` page is displayed
    2. ==When== User input `serial number` to get warranty info
    3. ==Then== Warranty result for `serial number` is displayed
    4. ==And== Verify `Warranty end date` exists in the warranty result
- If Warranty result for `serial number` is not displayed, your input is not meet the basic requirement.
- Test was successed if the warranty info block and warranty end date was found for a valid serial number, else test was failed.
- Manual Test 1
    1. Manually open the URL in browser
    2. Input `1863552437` in serial number textbox below the label, it's a number from image in the description PDF
    3. Verify the `Warranty result for 1863552437` is displayed
    4. Found the warranty end date
    - It's a successed test
- Manual Test 2
    1. Manually open the page in browser
    2. Input `186232437` in textbox below the label, it's supposed to be a valid serial number in the description PDF
    3. Verify the `Warranty result for 186232437` is displayed
    4. Cannot find the warranty end date
    - It's a failed test, due to the condition is showing warranty end date.  And the claimed valid number is actually not valid
- Manual Test 3 for defects
    1. Manually open the page in browser
    2. Input `456` and get `Minimum 6 characters required` error message, no result block was showed
    3. Input `中文字測試中` and get `Please enter a valid serial number` error message, result block was showed with input string and description
    4. Input `how about text` and get no error message, result block was showed with input string and description
    5. Input `!@#$%^` and get `Please enter a valid serial number` error message, result block was showed with input string and description
    6. Input `123` and get `Minimum 6 characters required` error message, however, result block of previous test (step 5) was remaining there which looks incorrect.

## Todo 
- support more browsers
- Automate the WebDriver download (In experiments)
- CrossBrowserTesting