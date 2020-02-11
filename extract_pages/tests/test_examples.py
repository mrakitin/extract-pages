from extract_pages import parse_ranges


def test_extract_pages():
    res = parse_ranges('1,3-6')
    assert res == [1, 3, 4, 5, 6]
