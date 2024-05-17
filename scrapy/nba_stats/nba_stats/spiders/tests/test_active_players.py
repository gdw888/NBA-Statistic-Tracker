import os
import json
import pytest

# Define the path to the generated JSON file
OUTPUT_FILE = '../outputs/active_players.json'

# Define the expected structure of the JSON data
EXPECTED_KEYS = {'name', 'url'}

# Sample test data to compare against (Optional)
EXPECTED_PLAYERS = []

@pytest.fixture
def json_data():
    # Ensure the output file exists
    assert os.path.exists(OUTPUT_FILE), f"{OUTPUT_FILE} does not exist"
    
    # Read and parse the JSON file
    with open(OUTPUT_FILE, 'r') as file:
        data = json.load(file)
    
    return data

def test_json_structure(json_data):
    # Check that the JSON data is a list
    assert isinstance(json_data, list), "JSON data is not a list"

    # Check that each item in the list is a dictionary with the expected keys
    for player in json_data:
        assert isinstance(player, dict), "Item in JSON data is not a dictionary"
        assert set(player.keys()) == EXPECTED_KEYS, f"JSON item keys do not match expected keys: {player}"

def test_json_content(json_data):
    # Optional: Check the actual content of the JSON data
    # Uncomment and use this if you have a predefined set of expected players
    # assert json_data == EXPECTED_PLAYERS, "JSON data does not match expected players"

    # Alternatively, validate individual elements or conditions if needed
    for player in json_data:
        assert isinstance(player['name'], str), "Player name is not a string"
        assert isinstance(player['url'], str), "Player URL is not a string"
        assert player['url'].startswith('https://'), "Player URL does not start with 'https://'"

# Run the tests
if __name__ == '__main__':
    pytest.main()
