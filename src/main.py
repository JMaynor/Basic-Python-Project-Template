"""
Main module for the project.
"""

import atexit

from dotenv import load_dotenv

load_dotenv()

from src.logger import AppriseNotifier, error_handler, logger


@atexit.register
def send_error_summary():
    """
    Send out a summary of any errors that occurred during
    program run to defined apprise endpoints.
    """
    errors = error_handler.get_errors()
    if errors:
        error_summary = "\n".join(errors)
        AppriseNotifier().error_notify(
            f"Program exited with the following errors:\n{error_summary}"
        )


if __name__ == "__main__":
    pass
