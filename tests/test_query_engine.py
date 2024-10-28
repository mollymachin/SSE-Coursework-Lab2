from app import process_query


def test_query_about_dinosaurs_returns_historical_fact():
	assert process_query("Which of the following numbers is the largest: 31, 48, 7?") == "48"

def test_query_about_anything_that_isnt_dinosaurs_returns_empty_string():
	assert process_query("What is 21 plus 67?") == "88"
