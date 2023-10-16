# Reaction Time
TIMEOUT_TIME = 20  # How long to wait for the button to turn green before determining something went wrong.
POLLING_FREQUENCY = 0.01  # How often to check if the button turned green (seconds)

# Don't change these values if you don't know what you're doing.
HOME_PAGE = "https://humanbenchmark.com/"
HOME_PAGE_BTN_XPATH = "//*[@id=\"root\"]/div/div[3]/div/a"

# Reaction Time
REACTION_TIME_BTN_XPATH = r"/html/body/div[1]/div/div[4]/div[2]/div[2]/div[1]/a[1]"
START_REACTION_TIME = r"/html/body/div[1]/div/div[4]/div[1]"
REACTION_TIME_RESULTS = r"/html/body/div[1]/div/div[4]/div[1]/div/div/div/h1/div"
