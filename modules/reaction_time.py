# Author: Quintin Dunn
# Description: Module for the reaction time game.
# Date: 10/15/23

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException

import logging

import config

from ._utils import return_to_homepage

logger = logging.getLogger("reaction_time.py")


def route_to_page(driver: Chrome) -> None:
    """
    Goes to the page for Reaction Time game.
    :param driver: Chromedriver initialized from main.py
    :return: None
    """

    reaction_time_button = driver.find_element(By.XPATH, config.REACTION_TIME_BTN_XPATH)
    reaction_time_button.click()


def start_reaction_time(driver: Chrome) -> None:
    """
    Starts the reaction time game.
    :param driver: Chromedriver initialized from main.py
    :return: None
    """

    start_btn = driver.find_element(By.XPATH, config.START_REACTION_TIME_XPATH)
    start_btn.click()


def wait_and_click_btn(driver: Chrome) -> None:
    """
    Plays the reaction time game.
    :param driver: Chromedriver initialized from main.py
    :return: None
    """

    try:
        click_btn = WebDriverWait(driver=driver,
                                  timeout=config.REACTION_TIME_TIMEOUT_TIME,
                                  poll_frequency=config.REACTION_TIME_POLLING_FREQUENCY
                                  ).until(
            ec.presence_of_element_located((By.CLASS_NAME, "view-go"))
        )
    except TimeoutException:
        raise Exception("Click button not found.")

    click_btn.click()


def get_results(driver: Chrome) -> int:
    """
    Gets the results from the Reaction Time game.
    :param driver: Chromedriver initialized from main.py
    :return: None
    """

    results_elem = driver.find_element(By.XPATH, config.REACTION_TIME_RESULTS_XPATH)
    text = results_elem.get_attribute("innerText")

    reaction_time = int(text.split(" ms")[0])
    return reaction_time


def run(driver: Chrome) -> list[int]:
    """
    Runs the routine to play the game
    :param driver: Chromedriver initialized from main.py
    :return: A list that contains the time to click in ms.
    """

    logger.info("Starting Reaction Time Benchmark!")

    logger.debug("Going to Reaction Time game.")
    route_to_page(driver=driver)

    logger.info("Starting Reaction Time")
    start_reaction_time(driver=driver)

    logger.info("Waiting for green button.")
    wait_and_click_btn(driver=driver)

    results = get_results(driver=driver)
    logger.info(f"Reacted in {results}ms.")

    return_to_homepage(driver=driver)

    return [results]
