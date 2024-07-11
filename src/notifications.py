from datetime import date, datetime, timedelta

import apprise

apobj = apprise.Apprise()
# TODO Add notification endpoints.


def error_notify(error_msg: str):
    """
    Send apprise notification of error
    """
    res = apobj.notify(
        body=(
            f"{error_msg}" f'Datetime: {datetime.now().strftime("%m/%d/%Y %H:%M:%S")}'
        ),
        title="Project Template",
        tag="error",
    )
    if not res:
        print("Error, could not send apprise notification")
