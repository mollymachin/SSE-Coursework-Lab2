from app import process_query

var = "What is 21 plus 67?"
square_var = "Which of the following numbers is both "
cube_var = "a square and a cube: 64, 81, 100, 121?"
prime_q1 = "Which of the following numbers"
prime_q2 = "are primes: 10, 78, 70, 27, 17?"


def test_query_about_dinosaurs_returns_historical_fact():
    input = "Which of the following numbers is the largest: 31, 48, 7?"
    assert process_query(input) == "48"


def test_query_about_anything_that_isnt_dinosaurs_returns_empty_string():
    assert process_query("What is 21 plus 67?") == "88"


def test_about_multiplying():
    assert process_query(var) == "1407"


def test_about_cubes():
    assert process_query(
        square_var + cube_var
        ) == "64"


def test_minus():
    assert process_query("What is 10 minus 5?") == "5"


def prime():
    assert process_query(prime_q1 + prime_q2) == "17"
