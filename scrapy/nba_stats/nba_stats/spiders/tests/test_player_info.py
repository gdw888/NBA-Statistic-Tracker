import os
import json
import pytest
import re
import subprocess

# Define the paths to the shell scripts
ACTIVE_PLAYERS_SCRIPT_PATH = '../scripts/active_players.sh'
PLAYER_INFO_SCRIPT_PATH = '../scripts/player_info.sh'

# Define the path to the generated JSON file
OUTPUT_FILE = '../outputs/player_info_output.json'

# Define the expected structure of the JSON data
EXPECTED_KEYS = {'player_name', 'birth_date', 'birth_year'}

# Sample test data to compare against (Optional)
EXPECTED_PLAYERS = []

@pytest.fixture(scope="module", autouse=True)
def run_shell_scripts():
    # Ensure the active players shell script exists
    assert os.path.exists(ACTIVE_PLAYERS_SCRIPT_PATH), f"{ACTIVE_PLAYERS_SCRIPT_PATH} does not exist"
    
    # Run the active players shell script
    process_active_players = subprocess.Popen(['sh', ACTIVE_PLAYERS_SCRIPT_PATH])
    process_active_players.wait()

    # Ensure the player info shell script exists
    assert os.path.exists(PLAYER_INFO_SCRIPT_PATH), f"{PLAYER_INFO_SCRIPT_PATH} does not exist"
    
    # Run the player info shell script
    process_player_info = subprocess.Popen(['sh', PLAYER_INFO_SCRIPT_PATH])
    process_player_info.wait()

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
    date_pattern = re.compile(r'^[A-Z][a-z]+ \d{1,2}$')
    year_pattern = re.compile(r'^\d{4}$')

    for player in json_data:
        # Validate player_name
        assert isinstance(player['player_name'], str) and player['player_name'], "Player name is not a non-empty string"
        
        # Validate birth_date
        assert isinstance(player['birth_date'], str) and player['birth_date'], "Birth date is not a non-empty string"
        assert date_pattern.match(player['birth_date']), "Birth date does not match the expected format"

        # Validate birth_year
        assert isinstance(player['birth_year'], str) and player['birth_year'], "Birth year is not a non-empty string"
        assert year_pattern.match(player['birth_year']), "Birth year does not match the expected format"

# Run the tests
if __name__ == '__main__':
    pytest.main()
