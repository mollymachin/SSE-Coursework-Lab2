from app import process_query

def test_query_about_dinosaurs_returns_historical_fact():
	assert process_query("dinosaurs") == "Dinosaurs ruled the Earth 200 million years ago"

def test_query_about_anything_that_isnt_dinosaurs_returns_empty_string():
	assert process_query("imperial college") == "Unknown"


