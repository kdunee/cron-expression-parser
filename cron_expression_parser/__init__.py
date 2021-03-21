from .cron_entry import CronEntry
import re
from typing import List, Optional

cron_string_regexp = r"^(?P<minutes>[^\s]+)\s+(?P<hours>[^\s]+)\s+(?P<days_of_month>[^\s]+)\s+(?P<months>[^\s]+)\s+(?P<days_of_week>[^\s]+)\s+(?P<command>.+)$"

field_form_1_regexp = r"^\*(/(?P<step>\d+))?$"
field_form_2_regexp = r"^(?P<start>\d+)-(?P<stop>\d+)(/(?P<step>\d+))?$"
field_form_3_regexp = r"^\d+(,\d+)*$"


class CronParsingError(Exception):
    pass


class CronFieldParsingError(CronParsingError):
    pass


def parse_cron_field_form_1(step: Optional[str], available: List[int]) -> List[int]:
    """Parse form 1 of cron field, e.g. "*/3"

    Args:
        step (Optional[str]): an integer value of step between requested values
        available (List[int]): a list of available values for this particular field

    Returns:
        List[int]: list of resulting values
    """
    if step is None:
        return available
    step = int(step)
    return available[::step]


def parse_cron_field_form_2(start: str, stop: str, step: Optional[str], available: List[int]) -> List[int]:
    """Parse form 2 of cron field, e.g. "2-7/2"

    Args:
        start (str): start of requested range
        stop (str): end of requested range (inclusive)
        step (Optional[str]): an integer value of step between requested values
        available (List[int]): a list of available values for this particular field

    Returns:
        List[int]: list of resulting values
    """
    start = int(start)
    stop = int(stop)
    if stop < start:
        raise CronFieldParsingError(f"Stop value {stop} is lower than start value {start}")
    if step is not None:
        step = int(step)
        listed = list(range(start, stop + 1, step))
    else:
        listed = list(range(start, stop + 1))
    intersection = set(listed).intersection(set(available))
    return list(intersection)


def parse_cron_field_form_3(expression: str, available: List[int]) -> List[int]:
    """Parse form 3 of cron field, e.g. "1,3,6,7"

    Args:
        expression (str): A comma-separated list of requested values
        available (List[int]): a list of available values for this particular field

    Returns:
        List[int]: list of resulting values
    """
    listed = [int(value) for value in expression.split(',')]
    intersection = set(listed).intersection(set(available))
    return list(intersection)


def parse_cron_field(expression: str, available: List[int]) -> List[int]:
    """Parse a cron field

    Three basic forms of expressions for a field are supported:
    Name     Example   Regexp
    Form 1   */3       ^\*(/\d+)?$
    Form 2   2-7/2     ^\d+-\d+(/\d+)?$
    Form 3   1,3,6,7   ^\d+(,\d+)*$

    Args:
        expression (str): A string representation of a cron field
        available (List[int]): a list of available values for this particular field

    Raises:
        CronFieldParsingError: when the field cannot be matched to any expected form

    Returns:
        List[int]: list of resulting values
    """

    m = re.match(field_form_1_regexp, expression)
    if m:
        return parse_cron_field_form_1(m.group('step'), available)

    m = re.match(field_form_2_regexp, expression)
    if m:
        return parse_cron_field_form_2(m.group('start'), m.group('stop'), m.group('step'), available)

    m = re.match(field_form_3_regexp, expression)
    if m:
        return parse_cron_field_form_3(expression, available)

    raise CronFieldParsingError(
        f"The field {expression} doesn't match any of the expected forms")


def parse_cron_string(cron_string: str) -> CronEntry:
    """Parses the entire cron string

    Args:
        cron_string (str): A cron string

    Raises:
        CronParsingError: when the cron string doesn't match the expected format

    Returns:
        CronEntry: a CronEntry object, representing the cron string
    """
    cron_string = cron_string.strip()
    m = re.match(cron_string_regexp, cron_string)
    if not m:
        raise CronParsingError("Cron string doesn't match the expected format")

    try:
        return CronEntry(
            minutes=parse_cron_field(m.group('minutes'), list(range(0, 60))),
            hours=parse_cron_field(m.group('hours'), list(range(0, 24))),
            days_of_month=parse_cron_field(
                m.group('days_of_month'), list(range(1, 32))),
            months=parse_cron_field(m.group('months'), list(range(1, 13))),
            days_of_week=parse_cron_field(
                m.group('days_of_week'), list(range(0, 8))),
            command=m.group('command')
        )
    except CronFieldParsingError as e:
        raise CronParsingError("Parsing the cron string failed while parsing one of the fields", e)
