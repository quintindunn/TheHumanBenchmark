# Author: Quintin Dunn
# Description: Module for the aim trainer game.
# Date: 10/15/23
import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


import logging

import config

from ._utils import return_to_homepage

logger = logging.getLogger("aim_trainer.py")


def route_to_page(driver: Chrome) -> None:
    """
    Goes to the page for Aim Training game.
    :param driver: Chromedriver initialized from main.py
    :return: None
    """

    reaction_time_button = driver.find_element(By.XPATH, config.AIM_TRAINER_BTN_XPATH)
    reaction_time_button.click()


def start_aim_trainer(driver: Chrome) -> None:
    """
    Starts the aim trainer game.
    :param driver: Chromedriver initialized from main.py
    :return: None
    """

    start_btn = driver.find_element(By.XPATH, config.START_AIM_TRAINER_XPATH)
    start_btn.click()


def play(driver: Chrome) -> int:
    """
    Plays aim trainer game
    :param driver: Chromedriver initialized from main.py
    :return int: Average time per target (ms)
    """
    # Find all targets and click as soon as possible.
    for _ in range(config.AIM_TRAINER_TARGET_COUNT):
        target = driver.find_element(By.XPATH, config.AIM_TRAINER_TARGET_XPATH)

        # Cannot directly click element due to it routing clicks through event interrupts, so click using mouse instead.
        ac = ActionChains(driver=driver)
        ac.move_to_element(target).click().perform()

    # Get results and return.
    results_elem = driver.find_element(By.XPATH, config.AIM_TRAINER_RESULTS_XPATH)
    return int(results_elem.get_attribute("innerText").split("ms")[0])


def run(driver: Chrome) -> list[int]:
    """
    Runs the routine to play the game
    :param driver: Chromedriver initialized from main.py
    :return: A list that contains the time to click in ms.
    """

    logger.info("Starting Aim Trainer Game!")

    logger.info("Going to Aim Trainer game.")
    route_to_page(driver=driver)

    logger.info("Starting Aim Trainer.")
    start_aim_trainer(driver=driver)

    logger.info("Playing game.")
    results = play(driver=driver)

    logger.info(f"Average response time: {results}ms")

    return_to_homepage(driver=driver)

    return [results]
