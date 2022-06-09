---
tags: BARCO, SDET, Python, Gherkin, BDD, Pytest
---
# python_test_plan

[![hackmd-github-sync-badge](https://hackmd.io/7_s1PVUcSZmWB480MVy85Q/badge)](https://hackmd.io/7_s1PVUcSZmWB480MVy85Q)

## Web UI Test
- URL: [ClickShare Warranty Info](https://www.barco.com/en/clickshare/support/warranty-info)
- Scenario: Get ClickShare warranty info
    1. ==Given== `Check your ClickShare warranty` page is displayed
    2. ==When== User input `serial number` to get warranty info
    3. ==Then== Warranty result for `serial number` is displayed
    4. ==And== Verify `Warranty end date` exists in the warranty result
- Test was successed if the info was found, else test was failed.
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
    - It's a failed case, which means it is not the claimed valid number

