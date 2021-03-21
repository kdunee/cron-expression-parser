from cron_expression_parser import parse_cron_string, CronParsingError
import pytest

def test_parse_cron_string():
    r = parse_cron_string("*/15 0 1,15 * 1-5 /usr/bin/find")
    assert r.command == "/usr/bin/find"
    assert r.minutes == [0, 15, 30, 45]
    assert r.hours == [0]
    assert r.days_of_month == [1, 15]
    assert r.months == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    assert r.days_of_week == [1, 2, 3, 4, 5]

def test_parse_cron_string_with_long_command():
    r = parse_cron_string("*/15 0 1,15 * 1-5 ls -halt /usr/bin")
    assert r.command == "ls -halt /usr/bin"

def test_parse_cron_string_with_command_with_spaces():
    r = parse_cron_string("*/15 0 1,15 * 1-5 echo \"Hello    world\"")
    assert r.command == "echo \"Hello    world\""

def test_parse_cron_string_with_extra_whitespace():
    r = parse_cron_string("  */15 0 \t 1,15  * 1-5  /usr/bin/find   ")
    assert r.command == "/usr/bin/find"
    assert r.minutes == [0, 15, 30, 45]
    assert r.hours == [0]
    assert r.days_of_month == [1, 15]
    assert r.months == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    assert r.days_of_week == [1, 2, 3, 4, 5]

def test_parse_cron_string_with_malformed_string():
    with pytest.raises(CronParsingError):
        parse_cron_string("*/15 0 * 1-5 /usr/bin/find")
    with pytest.raises(CronParsingError):
        parse_cron_string("*/15 0 1,15 * 1-5")
    with pytest.raises(CronParsingError):
        parse_cron_string("")
    with pytest.raises(CronParsingError):
        parse_cron_string("a b c d e")