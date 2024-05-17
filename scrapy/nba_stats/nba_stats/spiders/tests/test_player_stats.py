import os
import json
import pytest
import re
import subprocess

# Define the paths to the shell scripts
ACTIVE_PLAYERS_SCRIPT_PATH = '../scripts/active_players.sh'
PLAYER_STATS_SCRIPT_PATH = '../scripts/player_stats.sh'

# Define the path to the generated JSON file
OUTPUT_FILE = '../outputs/player_stats_output.json'

# Define the expected structure of the JSON data
EXPECTED_KEYS = {
    'player_name', 'date', 'team', 'opponent', 'result', 'minutes_played', 'field_goals', 
    'field_goal_attempts', 'field_goal_percentage', 'three_point_field_goals', 
    'three_point_field_goal_attempts', 'three_point_field_goal_percentage', 'free_throws', 
    'free_throw_attempts', 'free_throw_percentage', 'offensive_rebounds', 'defensive_rebounds', 
    'total_rebounds', 'assists', 'steals', 'blocks', 'turnovers', 'personal_fouls', 'points', 
    'game_score', 'plus_minus'
}

# Sample test data to compare against (Optional)
EXPECTED_PLAYERS_STATS = []

@pytest.fixture(scope="module", autouse=True)
def run_shell_scripts():
    # Ensure the active players shell script exists
    assert os.path.exists(ACTIVE_PLAYERS_SCRIPT_PATH), f"{ACTIVE_PLAYERS_SCRIPT_PATH} does not exist"
    
    # Run the active players shell script
    process_active_players = subprocess.Popen(['sh', ACTIVE_PLAYERS_SCRIPT_PATH])
    process_active_players.wait()

    # Ensure the player stats shell script exists
    assert os.path.exists(PLAYER_STATS_SCRIPT_PATH), f"{PLAYER_STATS_SCRIPT_PATH} does not exist"
    
    # Run the player stats shell script
    process_player_stats = subprocess.Popen(['sh', PLAYER_STATS_SCRIPT_PATH])
    process_player_stats.wait()

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
    for player_stat in json_data:
        assert isinstance(player_stat, dict), "Item in JSON data is not a dictionary"
        assert set(player_stat.keys()) == EXPECTED_KEYS, f"JSON item keys do not match expected keys: {player_stat}"

def test_json_content(json_data):
    date_pattern = re.compile(r'^\d{4}-\d{2}-\d{2}$')
    percentage_pattern = re.compile(r'^(\d*\.\d{3}|None)$')
    number_pattern = re.compile(r'^\d+$')
    nullable_number_pattern = re.compile(r'^(\d+|None)$')
    result_pattern = re.compile(r'^[WL] \d{2,3}-\d{2,3}( \(\d*OT\))?$')
    game_score_pattern = re.compile(r'^-?\d+(\.\d+)?$')  # Updated pattern to allow negative numbers

    for player_stat in json_data:
        # Validate player_name
        assert isinstance(player_stat['player_name'], str) and player_stat['player_name'], "Player name is not a non-empty string"
        
        # Validate date
        assert isinstance(player_stat['date'], str) and player_stat['date'], "Date is not a non-empty string"
        assert date_pattern.match(player_stat['date']), "Date does not match the expected format"
        
        # Validate team and opponent
        assert isinstance(player_stat['team'], str) and player_stat['team'], "Team is not a non-empty string"
        assert isinstance(player_stat['opponent'], str) and player_stat['opponent'], "Opponent is not a non-empty string"
        
        # Validate result
        assert isinstance(player_stat['result'], str) and player_stat['result'], "Result is not a non-empty string"
        assert result_pattern.match(player_stat['result']), "Result does not match the expected format"

        # Validate other numeric fields
        assert nullable_number_pattern.match(str(player_stat['minutes_played'])), "Minutes played does not match the expected format"
        assert nullable_number_pattern.match(str(player_stat['field_goals'])), "Field goals does not match the expected format"
        assert nullable_number_pattern.match(str(player_stat['field_goal_attempts'])), "Field goal attempts does not match the expected format"
        assert percentage_pattern.match(str(player_stat['field_goal_percentage'])), "Field goal percentage does not match the expected format"
        assert nullable_number_pattern.match(str(player_stat['three_point_field_goals'])), "Three point field goals does not match the expected format"
        assert nullable_number_pattern.match(str(player_stat['three_point_field_goal_attempts'])), "Three point field goal attempts does not match the expected format"
        assert percentage_pattern.match(str(player_stat['three_point_field_goal_percentage'])), "Three point field goal percentage does not match the expected format"
        assert nullable_number_pattern.match(str(player_stat['free_throws'])), "Free throws does not match the expected format"
        assert nullable_number_pattern.match(str(player_stat['free_throw_attempts'])), "Free throw attempts does not match the expected format"
        assert percentage_pattern.match(str(player_stat['free_throw_percentage'])), "Free throw percentage does not match the expected format"
        assert nullable_number_pattern.match(str(player_stat['offensive_rebounds'])), "Offensive rebounds does not match the expected format"
        assert nullable_number_pattern.match(str(player_stat['defensive_rebounds'])), "Defensive rebounds does not match the expected format"
        assert nullable_number_pattern.match(str(player_stat['total_rebounds'])), "Total rebounds does not match the expected format"
        assert nullable_number_pattern.match(str(player_stat['assists'])), "Assists does not match the expected format"
        assert nullable_number_pattern.match(str(player_stat['steals'])), "Steals does not match the expected format"
        assert nullable_number_pattern.match(str(player_stat['blocks'])), "Blocks does not match the expected format"
        assert nullable_number_pattern.match(str(player_stat['turnovers'])), "Turnovers does not match the expected format"
        assert nullable_number_pattern.match(str(player_stat['personal_fouls'])), "Personal fouls does not match the expected format"
        assert nullable_number_pattern.match(str(player_stat['points'])), "Points does not match the expected format"
        assert game_score_pattern.match(str(player_stat['game_score'])), "Game score does not match the expected format"
        assert re.match(r'^-?\d+(\.\d+)?$', str(player_stat['plus_minus'])), "Plus minus does not match the expected format"

# Run the tests
if __name__ == '__main__':
    pytest.main()
