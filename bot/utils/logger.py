import logging
import os
from logging.handlers import RotatingFileHandler
import datetime

current_year = datetime.datetime.now().year
current_month = datetime.datetime.now().strftime("%B")
log_dir = f"log/{current_year}/{current_month}"
os.makedirs(log_dir, exist_ok=True)

logger = logging.getLogger('logger')
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

log_file = f"{log_dir}/logfile_{datetime.datetime.now().day}.log"
file_handler = RotatingFileHandler(log_file, mode='a', maxBytes=1e6, backupCount=5)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logging.getLogger('apscheduler.scheduler',).propagate = False
logging.getLogger('apscheduler.executors.default' ).propagate = False
