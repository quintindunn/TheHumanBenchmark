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
}

# Initialize selenium
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get(config.HOME_PAGE)

logger.info(f"Loaded {len(MODULES)} modules.")
if __name__ == '__main__':
    # Run the modules
    for name, module in MODULES.items():
        logger.info(f"Running module {name}")
        module.run(driver=driver)
