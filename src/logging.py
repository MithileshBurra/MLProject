# src/logger.py
import logging
import os
from datetime import datetime as dt

# 1. Create a timestamped log file name
LOG_FILE = f"{dt.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# 2. Create logs directory if it doesn't exist
logs_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_dir, exist_ok=True)

# 3. Full log file path
LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

# 4. Configure the logger
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# Optional: print log path
print(f"Logging initialized at: {LOG_FILE_PATH}")

# 5. Optional test message
if __name__ == "__main__":
    logging.info("Logger test successful.")
