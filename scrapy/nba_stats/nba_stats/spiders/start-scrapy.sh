#!/bin/bash

# Get the directory where the script is located
SCRIPT_DIR="$(dirname "$(realpath "$0")")"


scrapy crawl active_players -o $SCRIPT_DIR/outputs/active_players.json;
scrapy crawl player_info -o $SCRIPT_DIR/outputs/player_info_output.json;
scrapy crawl player_stats -o $SCRIPT_DIR/outputs/player_stats_ouput.json;


sleep 1000;