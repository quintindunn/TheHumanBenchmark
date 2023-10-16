# Author: Quintin Dunn
# Description: General utils for the modules.
# Date: 10/15/23

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

import config


def return_to_homepage(driver: Chrome):
    """
    Gets the results from the Reaction Time game.
    :param driver: Chromedriver initialized from main.py
    :return: None
    """
    driver.find_element(By.XPATH, config.HOME_PAGE_BTN_XPATH).click()
