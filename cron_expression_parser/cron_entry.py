from dataclasses import dataclass
from typing import List, Union

__all__ = ['CronEntry']


def format_field_name(column_name: str) -> str:
    """Format a field name for nice textual output

    Args:
        column_name (str): A field name

    Returns:
        str: A field name padded to 14 characters
    """
    return '{:14}'.format(column_name)


def format_value(value: Union[str, List[int]]) -> str:
    """Format a field value for nice textual output

    Args:
        value (Union[str, List[int]]): either a list of numbers or already a string

    Returns:
        str: Numbers separated with spaces or the unchanged input string
    """
    if isinstance(value, str):
        return value
    return " ".join([str(num) for num in value])


@dataclass
class CronEntry:
    minutes: List[int]
    hours: List[int]
    days_of_month: List[int]
    months: List[int]
    days_of_week: List[int]
    command: str

    def __str__(self) -> str:
        fields = [
            ('minute', self.minutes),
            ('hour', self.hours),
            ('day of month', self.days_of_month),
            ('month', self.months),
            ('day of week', self.days_of_week),
            ('command', self.command)
        ]

        formatted_fields = [(format_field_name(field_name), format_value(
            value)) for field_name, value in fields]
        rows = [f"{field_name}{value}" for field_name,
                value in formatted_fields]
        return "\n".join(rows)
