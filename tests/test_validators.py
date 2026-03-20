import pytest
from utils.validation import *

@pytest.mark.parametrize(
    "first_name, last_name, student_id, expected",
    [
        ("Ronald", "Ho", "A01180478", None),
        ("", "Ho", "A01180478", "All fields are required."),
        ("Ronald", "", "A01180478", "All fields are required."),
        ("Ronald", "Ho", "", "All fields are required."),
        (" ", "Ho", "A01180478", None),
        ("Ronald", " ", "A01180478", None),
        ("Ronald", "Ho", " ", None),
        (None, "Ho", "A01180478", "All fields are required."),
        ("Ronald", None, "A01180478", "All fields are required."),
        ("Ronald", "Ho", None, "All fields are required."),
        (" ", " ", " ", None),
        ("", "", "", "All fields are required."),
        (None, None, None, "All fields are required.")
    ]
)
def test_validate_profile_data(first_name, last_name, student_id, expected):
    assert validate_profile_data(first_name, last_name, student_id) == expected


@pytest.mark.parametrize(
    "first_name, last_name, student_id, expected",
    [
        ("Ronald", "Ho", "A01180478", {"first_name": "Ronald", "last_name": "Ho", "student_id": "A01180478"}),
        ("Ronald", "Ho", 1180478, {"first_name": "Ronald", "last_name": "Ho", "student_id": "1180478"}),
        (" Ronald ", " Ho ", " A01180478 ", {"first_name": "Ronald", "last_name": "Ho", "student_id": "A01180478"}),
        ("", "Ho", "A01180478", {"first_name": "", "last_name": "Ho", "student_id": "A01180478"}),
        ("Ronald", "", "A01180478", {"first_name": "Ronald", "last_name": "", "student_id": "A01180478"}),
        ("Ronald", "Ho", "", {"first_name": "Ronald", "last_name": "Ho", "student_id": ""}),
        (" ", "Ho", "A01180478", {"first_name": "", "last_name": "Ho", "student_id": "A01180478"}),
        ("Ronald", " ", "A01180478", {"first_name": "Ronald", "last_name": "", "student_id": "A01180478"}),
        ("Ronald", "Ho", " ", {"first_name": "Ronald", "last_name": "Ho", "student_id": ""}),
        (None, "Ho", "A01180478", {"first_name": "", "last_name": "Ho", "student_id": "A01180478"}),
        ("Ronald", None, "A01180478", {"first_name": "Ronald", "last_name": "", "student_id": "A01180478"}),
        ("Ronald", "Ho", None, {"first_name": "Ronald", "last_name": "Ho", "student_id": ""}),
        (" ", " ", " ", {"first_name": "", "last_name": "", "student_id": ""}),
        ("", "", "", {"first_name": "", "last_name": "", "student_id": ""}),
        (None, None, None, {"first_name": "", "last_name": "", "student_id": ""})
    ]
)
def test_normalize_profile_data(first_name, last_name, student_id, expected):
    assert normalize_profile_data(first_name, last_name, student_id) == expected
