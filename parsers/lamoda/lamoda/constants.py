from datetime import datetime

DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'
CURRENT_TIME = datetime.now().strftime(DATETIME_FORMAT)

ALLOWED_DOMAINS = ["lamoda.ru"]
BASE_URL = "https://lamoda.ru"
START_URLS = [{"url": "https://www.lamoda.ru/b/5181/brand-hugo/?page=", "brand": "HUGO BOSS"}]