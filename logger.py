"""
logger.py

Central logging configuration for the Angel AI Assistant.
"""

import logging

from config import LOGS_DIR

# ---------------------------------------------------------------------
# Create log directory if it doesn't exist
# ---------------------------------------------------------------------

LOGS_DIR.mkdir(exist_ok=True)

LOG_FILE = LOGS_DIR / "angel.log"

# ---------------------------------------------------------------------
# Configure Logging
# ---------------------------------------------------------------------

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

logger = logging.getLogger("Angel")