"""
This module contains shared fixtures.
"""

import pytest
import selenium.webdriver

# ----------------------------------------------------------------------
# Fixture: Create the WebDriver instance
# ----------------------------------------------------------------------

@pytest.fixture
def browser():
    # local chrome driver
    b = selenium.webdriver.Chrome()
    b.implicitly_wait(10)
    yield b
    b.quit()
