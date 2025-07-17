
import logging
import os
from datetime import datetime as dt


LOG_FILE = f"{dt.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"


logs_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_dir, exist_ok=True)


LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)


logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

print(f"Logging initialized at: {LOG_FILE_PATH}")


if __name__ == "__main__":
    logging.info("Logger test successful.")
