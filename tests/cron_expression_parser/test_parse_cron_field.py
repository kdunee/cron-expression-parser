from cron_expression_parser import parse_cron_field, CronFieldParsingError
import pytest


def test_parse_cron_field():
    available = list(range(1, 21))
    assert parse_cron_field("*/3", available) == [1, 4, 7, 10, 13, 16, 19]
    assert parse_cron_field("*", available) == available
    assert parse_cron_field("2-6/2", available) == [2, 4, 6]
    assert parse_cron_field("2-6", available) == [2, 3, 4, 5, 6]
    assert parse_cron_field("20-25", available) == [20]
    assert parse_cron_field("7", available) == [7]
    assert parse_cron_field("1,7,25", available) == [1, 7]


def test_parse_cron_field_with_bad_field():
    available = list(range(1, 21))

    # broken form 1 fields
    with pytest.raises(CronFieldParsingError):
        parse_cron_field("x", available)
    with pytest.raises(CronFieldParsingError):
        parse_cron_field("a/3", available)
    with pytest.raises(CronFieldParsingError):
        parse_cron_field("*/", available)
    with pytest.raises(CronFieldParsingError):
        parse_cron_field("/2", available)

    # broken form 2 fields
    with pytest.raises(CronFieldParsingError):
        parse_cron_field("3-0", available)
    with pytest.raises(CronFieldParsingError):
        parse_cron_field("3--", available)
    with pytest.raises(CronFieldParsingError):
        parse_cron_field("3-", available)
    with pytest.raises(CronFieldParsingError):
        parse_cron_field("-4", available)
    with pytest.raises(CronFieldParsingError):
        parse_cron_field("a-b", available)

    # broken form 3 fields
    with pytest.raises(CronFieldParsingError):
        parse_cron_field("1,", available)
    with pytest.raises(CronFieldParsingError):
        parse_cron_field(",7", available)

    with pytest.raises(CronFieldParsingError):
        parse_cron_field("", available)
