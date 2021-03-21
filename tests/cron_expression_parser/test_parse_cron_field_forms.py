from cron_expression_parser import parse_cron_field_form_1, parse_cron_field_form_2, parse_cron_field_form_3


def test_parse_cron_field_form_1_simple():
    assert parse_cron_field_form_1(None, [1, 3, 5]) == [1, 3, 5]


def test_parse_cron_field_form_1_empty_list():
    assert parse_cron_field_form_1(None, []) == []


def test_parse_cron_field_form_1_step():
    assert parse_cron_field_form_1(10, [1]) == [1]
    assert parse_cron_field_form_1(10, list(range(1, 20))) == [1, 11]


def test_parse_cron_field_form_2_simple():
    available = list(range(1, 20))
    assert parse_cron_field_form_2(1, 5, None, available) == list(range(1, 6))


def test_parse_cron_field_form_2_simple_out_of_range():
    available = list(range(1, 20))
    assert parse_cron_field_form_2(0, 5, None, available) == list(range(1, 6))


def test_parse_cron_field_form_2_empty_intersection():
    available = list(range(1, 20))
    assert parse_cron_field_form_2(22, 27, None, available) == []


def test_parse_cron_field_form_2_with_step():
    available = list(range(1, 20))
    assert parse_cron_field_form_2(1, 9, 2, available) == [1, 3, 5, 7, 9]


def test_parse_cron_field_form_3_simple():
    available = list(range(1, 20))
    assert parse_cron_field_form_3("1,4,6", available) == [1, 4, 6]


def test_parse_cron_field_form_3_single_value():
    available = list(range(1, 20))
    assert parse_cron_field_form_3("4", available) == [4]


def test_parse_cron_field_form_3_out_of_range():
    available = list(range(1, 20))
    assert parse_cron_field_form_3("1,4,6,22", available) == [1, 4, 6]


def test_parse_cron_field_form_3_empty_intersection():
    available = list(range(1, 20))
    assert parse_cron_field_form_3("22", available) == []
