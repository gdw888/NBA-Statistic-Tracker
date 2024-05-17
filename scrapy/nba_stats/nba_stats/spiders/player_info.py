import scrapy
import json
import os

class PlayerInfoSpider(scrapy.Spider):
    name = "player_info"
    allowed_domains = ["basketball-reference.com"]

    # Path to the JSON file containing player URLs
    current_directory = os.path.dirname(__file__)
    json_file_path = os.path.join(current_directory, 'outputs', 'active_players.json')

    def __init__(self, *args, **kwargs):
        super(PlayerInfoSpider, self).__init__(*args, **kwargs)
        
        # Read the JSON file and extract the URLs
        with open(self.json_file_path, 'r') as file:
            players = json.load(file)
        
        self.start_urls = [player['url'] for player in players]

    def parse(self, response):
        self.logger.info("Parsing the page: %s", response.url)
        
        # Extract the player name
        player_name = response.xpath('//div[@id="meta"]/div/h1/span/text()').get()
        
        if not player_name:
            self.logger.error("Player name not found on page: %s", response.url)
            return

        # Extract player birth date and year
        birth_date = response.xpath('//span[@id="necro-birth"]/a[1]/text()').get()
        birth_year = response.xpath('//span[@id="necro-birth"]/a[2]/text()').get()

        # Log extracted information
        self.logger.info("Extracted info for %s", player_name)
        
        player_info = {
            'player_name': player_name,
            'birth_date': birth_date,
            'birth_year': birth_year
        }
        
        # Yield the extracted player information
        yield player_info
