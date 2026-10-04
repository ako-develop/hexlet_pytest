from pathlib import Path

from hexlet_pytest.example import reverse


def get_test_data_path(filename):
    return Path(__file__).parent / "test_data" / filename


def read_file(filename):
    return get_test_data_path(filename).read_text(encoding="utf-8")


def test_reverse_short():
    assert reverse("Hexlet") == "telxeH"


def test_reverse_long_text():
    source = read_file("long_text.txt")
    expected = read_file("reversed_text.txt")
    assert reverse(source) == expected


def test_reverse_twice_returns_source():
    source = read_file("long_text.txt")
    assert reverse(reverse(source)) == source
