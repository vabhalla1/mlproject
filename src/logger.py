import logging
import os
from datetime import datetime
import sys

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
log_path=os.path.join(os.getcwd(),"logs", LOG_FILE)
os.makedirs(log_path, exist_ok=True)

LOG_FILE_PATH=os.path.join(log_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s",
   # datefmt="%d/%b/%Y %H:%M:%S",
    #stream=sys.stdout
)

""" if __name__=="__main__":
    logging.info("Logging has started") """