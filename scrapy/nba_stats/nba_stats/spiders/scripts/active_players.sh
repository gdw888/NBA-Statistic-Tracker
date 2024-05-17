#!/bin/bash

# Move to the parent directory
cd ..

# Check if "outputs" folder exists
OUTPUT_DIR="outputs"
if [ ! -d "$OUTPUT_DIR" ]; then
    # Create the "outputs" folder if it doesn't exist
    mkdir $OUTPUT_DIR
fi

# Set the OUTPUT_FILE with the "outputs" folder path
OUTPUT_FILE="$OUTPUT_DIR/active_players.json"

# Remove the existing output file if it exists
if [ -f $OUTPUT_FILE ]; then
    rm $OUTPUT_FILE
fi

# Run the Scrapy spider
scrapy crawl active_players -o $OUTPUT_FILE