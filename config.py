# Reaction Time
REACTION_TIME_TIMEOUT_TIME = 20  # How long to wait for the button to turn green before raising an error.
REACTION_TIME_POLLING_FREQUENCY = 0.01  # How often to check if the button turned green (seconds).

# Sequence Memory
SEQUENCE_MEMORY_TARGET_MEMORY = 50
SEQUENCE_MEMORY_POLLING_FREQUENCY = 0.1  # seconds
SEQUENCE_MEMORY_TIMEOUT = 2  # seconds
SEQUENCE_MEMORY_BUTTON_DEACTIVATION_TIME = 0.5  # seconds


# Don't change these values if you don't know what you're doing.
HOME_PAGE = "https://humanbenchmark.com/"
HOME_PAGE_BTN_XPATH = "//*[@id=\"root\"]/div/div[3]/div/a"

# Reaction Time
REACTION_TIME_BTN_XPATH = r"/html/body/div[1]/div/div[4]/div[2]/div[2]/div[1]/a[1]"
START_REACTION_TIME_XPATH = r"/html/body/div[1]/div/div[4]/div[1]"
REACTION_TIME_RESULTS_XPATH = r"/html/body/div[1]/div/div[4]/div[1]/div/div/div/h1/div"

# Sequence Memory
SEQUENCE_MEMORY_BTN_XPATH = r"/html/body/div[1]/div/div[4]/div[2]/div[2]/div[1]/a[2]"
SEQUENCE_MEMORY_ACTIVE_SELECTOR = "div.square.active"
START_SEQUENCE_MEMORY_XPATH = r"/html/body/div[1]/div/div[4]/div[1]/div/div/div/div[2]/button"
SEQUENCE_MEMORY_RESULTS_XPATH = r"/html/body/div[1]/div/div[4]/div[1]/div/div/div[2]/h1"

# Aim Trainer
AIM_TRAINER_BTN_XPATH = r"/html/body/div[1]/div/div[4]/div[2]/div[2]/div[1]/a[3]"
START_AIM_TRAINER_XPATH = r"/html/body/div[1]/div/div[4]/div[1]/div/div[1]/div[2]"
AIM_TRAINER_TARGET_XPATH = r"/html/body/div[1]/div/div[4]/div[1]/div/div[1]/div/div"
AIM_TRAINER_RESULTS_XPATH = r"/html/body/div[1]/div/div[4]/div[1]/div/div[1]/div/div[2]/h1"
AIM_TRAINER_TARGET_COUNT = 30
