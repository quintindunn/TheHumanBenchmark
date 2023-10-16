# Author: Quintin Dunn
# Description: Main file for the project
# Date: 10/15/23
import time
from importlib import import_module

import sys

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

import logging

import config

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logger = logging.getLogger(__name__)

MODULES = {
    "Reaction Time": import_module("modules.reaction_time"),
    "Sequence Memory": import_module("modules.sequence_memory"),
    "Aim Trainer": import_module("modules.aim_trainer")
}

# Initialize selenium
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get(config.HOME_PAGE)

logger.info(f"Loaded {len(MODULES)} modules.")


def print_results(results: dict):
    for k, v in results.items():
        print(f"{k}: {v}")


if __name__ == '__main__':
    game_results = dict()

    # Run the modules
    for name, module in MODULES.items():
        logger.info(f"Running module {name}")
        game_results[name] = module.run(driver=driver)
        time.sleep(1)  # Let game load

    print_results(game_results)

    # Stop driver from quitting.
    input()
