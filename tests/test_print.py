import pytest

from aochallenge import print_condensed, print_csv, print_arranged


@pytest.mark.parametrize(
    "data, printed",
    (
        ([[12, 34], [56, 78]], "1234\n5678\n"),
        (("##.", ".#.", ".##"), "##.\n.#.\n.##\n"),
    ),
)
def test_print_condensed(data, printed, capsys):
    print_condensed(data)
    captured = capsys.readouterr()
    assert captured.out == printed


@pytest.mark.parametrize(
    "data, printed", (([[1, 34], [True, "xyz"]], "1,34\nTrue,xyz\n"),)
)
def test_print_csv(data, printed, capsys):
    print_csv(data)
    captured = capsys.readouterr()
    assert captured.out == printed


@pytest.mark.parametrize(
    "data, printed", (([[1, 3456], [True, "xyz"]], "   1 3456\nTrue xyz \n"),)
)
def test_print_arranged(data, printed, capsys):
    print_arranged(data)
    captured = capsys.readouterr()
    assert captured.out == printed
