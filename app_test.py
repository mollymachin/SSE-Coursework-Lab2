from app import process_query

var = "What is 21 plus 67?"
square_var = "Which of the following numbers is both "
cube_var = "a square and a cube: 64, 81, 100, 121?"


def test_query_about_dinosaurs_returns_historical_fact():
    input = "Which of the following numbers is the largest: 31, 48, 7?"
    assert process_query(input) == "48"


def test_query_about_anything_that_isnt_dinosaurs_returns_empty_string():
    assert process_query("What is 21 plus 67?") == "88"
