""" Module: date

A date utility module that wraps python-dateutil.

"""

from datetime import datetime
from dateutil import relativedelta

YEAR = "year"
MONTH = "month"
DAY = "day"
HOUR = "hour"
DAY = "day"
MINUTE = "minute"
SECOND = "second"
PLURAL = "s"


def current_ts():
    """ Return the current timestamp. """
    # TODO have this incorporate the User's timezone
    return datetime.now()


def _get_relative_delta(datetime_first, datetime_second):
    """ Return the difference between the two timestamps. """
    return relativedelta.relativedelta(datetime_first, datetime_second)


def get_simple_datetime_ago(ts):
    """ Return the difference between the timestamp and today. """
    rd = _get_relative_delta(current_ts(), datetime.fromtimestamp(ts))

    value = -1
    unit = "epoch"

    if rd.years > 0:
        value = rd.years
        unit = YEAR
    elif rd.months > 0:
        value = rd.months
        unit = MONTH
    elif rd.days > 0:
        value = rd.days
        unit = DAY
    elif rd.hours > 0:
        value = rd.hours
        unit = HOUR
    elif rd.minutes > 0:
        value = rd. minutes
        unit = MINUTE
    elif rd.seconds > 0:
        value = rd.seconds
        unit = SECOND

    plural = ""
    if value > 1:
        plural = PLURAL

    return "{0} {1}{2} ago".format(value, unit, plural)
