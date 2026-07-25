from datetime import datetime


def get_current_time():
    """Return the current local time."""

    return datetime.now().strftime("%I:%M:%S %p")