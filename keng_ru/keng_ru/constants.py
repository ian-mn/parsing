from datetime import datetime

DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'
CURRENT_TIME = datetime.now().strftime(DATETIME_FORMAT)

ALLOWED_DOMAINS = ["keng.ru"]
BASE_URL = "https://keng.ru"
START_URL = "https://keng.ru/brands/"