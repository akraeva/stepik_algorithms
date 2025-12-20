import pytest
from src.module_2 import m_2_3_1, m_2_3_2, m_2_3_3, m_2_3_4


# === Задача 1 ===
@pytest.mark.parametrize(
    "data, expected",
    [
        ("6\n0 1 2 3 4 5", "0"),
        ("6\n7 6 5 4 3 2", "4\n2 5\n1 4\n0 2\n2 5"),
    ],
    ids=[
        "Sample 1",
        "Sample 2",
    ],
)
def test_2_3_1(data, expected):
    assert m_2_3_1(data) == expected


# === Задача 2 ===
@pytest.mark.parametrize(
    "data, expected",
    [
        ("2 5\n1 2 3 4 5", "0 0\n1 0\n0 1\n1 2\n0 4"),
    ],
    ids=[
        "Sample 1",
    ],
)
def test_2_3_2(data, expected):
    assert m_2_3_2(data) == expected


# === Задача 3 ===
@pytest.mark.parametrize(
    "data, expected",
    [
        ("5 5\n1 1 1 1 1\n3 5\n2 4\n1 4\n5 4\n5 3", "\n".join("22355")),
    ],
    ids=[
        "Sample 1",
    ],
)
def test_2_3_3(data, expected):
    assert m_2_3_3(data) == expected


# === Задача 4 ===
@pytest.mark.parametrize(
    "data, expected",
    [
        ("4 6 0\n1 2\n1 3\n1 4\n2 3\n2 4\n3 4", "1"),
        ("4 6 1\n1 2\n1 3\n1 4\n2 3\n2 4\n3 4\n1 2", "0"),
    ],
    ids=[
        "Sample 1",
        "Sample 2",
    ],
)
def test_2_3_4(data, expected):
    assert m_2_3_4(data) == expected
