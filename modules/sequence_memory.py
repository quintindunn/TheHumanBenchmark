# Author: Quintin Dunn
# Description: Module for the sequence memory game.
# Date: 10/15/23
import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement

import logging

import config

from ._utils import return_to_homepage

logger = logging.getLogger("reaction_time.py")


def route_to_page(driver: Chrome) -> None:
    """
    Goes to the page for Sequence Memory game.
    :param driver: Chromedriver initialized from main.py
    :return: None
    """

    reaction_time_button = driver.find_element(By.XPATH, config.SEQUENCE_MEMORY_BTN_XPATH)
    reaction_time_button.click()


def start_sequence_memory(driver: Chrome) -> None:
    """
    Starts the sequence memory game.
    :param driver: Chromedriver initialized from main.py
    :return: None
    """

    start_btn = driver.find_element(By.XPATH, config.START_SEQUENCE_MEMORY_XPATH)
    start_btn.click()


def find_current_button(driver: Chrome, level: int) -> WebElement:
    """
    Finds the correct button, returns the element of the next button in sequence.
    :param driver: Chromedriver initialized from main.py.
    :param level: int of what level the bot is currently on.
    :return WebElement: WebElement object of the next button in sequence.
    """

    active_button = None

    # Wait to get to current level, then save the button for the final button in sequence to active_button.
    for _ in range(level):
        try:
            active_button: WebElement | None = WebDriverWait(driver=driver,
                                                             timeout=config.SEQUENCE_MEMORY_TIMEOUT,
                                                             poll_frequency=config.SEQUENCE_MEMORY_POLLING_FREQUENCY
                                                             ).until(
                ec.presence_of_element_located((By.CSS_SELECTOR, config.SEQUENCE_MEMORY_ACTIVE_SELECTOR))
            )
            time.sleep(0.5)
        except TimeoutException:
            raise Exception("Didn't find button, might have been missed due to lag.")

    if active_button is None:
        raise Exception("Didn't find button, might have been missed due to lag.")

    return active_button


def play(driver: Chrome) -> int:
    """
    Plays sequence memory game
    :param driver: Chromedriver initialized from main.py
    :return: None
    """

    button_list = []

    # Play up to level specified in config.
    for level in range(1, config.SEQUENCE_MEMORY_TARGET_MEMORY + 1):
        logger.info(f"Playing level {level}.")

        # Keep track of button sequence, log into button list.
        button_list.append(find_current_button(driver=driver, level=level))

        time.sleep(config.SEQUENCE_MEMORY_BUTTON_DEACTIVATION_TIME)

        # Press buttons in order they were added to button list.
        for button in button_list:
            time.sleep(config.SEQUENCE_MEMORY_BUTTON_DEACTIVATION_TIME)
            button.click()

    # Reached target, kill the game.
    while True:
        try:
            loss_elem: WebElement | None = driver.find_element(By.XPATH, config.SEQUENCE_MEMORY_RESULTS_XPATH)
            results = loss_elem.get_attribute("innerText")
            if results:
                return int(results.split("Level ")[1])
        except (NoSuchElementException, IndexError):
            driver.find_element(By.CLASS_NAME, "square").click()


def run(driver: Chrome) -> list[int]:
    """
    Runs the routine to play the game
    :param driver: Chromedriver initialized from main.py
    :return: A list that contains the time to click in ms.
    """

    logger.info("Starting Sequence Memory Game!")

    logger.info("Going to Sequence Memory game.")
    route_to_page(driver=driver)

    logger.info("Starting Sequence Memory.")
    start_sequence_memory(driver=driver)

    logger.info("Playing game.")
    results = play(driver=driver)

    logger.info(f"Got to level {results}!")

    return_to_homepage(driver=driver)

    return [results]
