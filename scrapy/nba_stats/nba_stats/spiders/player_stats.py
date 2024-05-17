import scrapy
import json
import os

class PlayerStatsSpider(scrapy.Spider):
    name = "player_stats"
    allowed_domains = ["basketball-reference.com"]

    name = "player_stats"
    allowed_domains = ["basketball-reference.com"]
    
    # List of player URLs to scrape
    start_urls = [
        "https://www.basketball-reference.com/players/j/jamesle01.html",
        "https://www.basketball-reference.com/players/e/edwaran01.html"
        # Add more player URLs as needed
    ]


    # # Path to the JSON file containing player URLs
    # json_file_path = os.path.join(os.path.dirname(__file__), 'active_players.json')
    
    # def __init__(self, *args, **kwargs):
    #     super(PlayerStatsSpider, self).__init__(*args, **kwargs)
        
    #     # Read the JSON file and extract the URLs
    #     with open(self.json_file_path, 'r') as file:
    #         players = json.load(file)
        
    #     self.start_urls = [player['url'] for player in players]

    def parse(self, response):
        self.logger.info("Parsing the page: %s", response.url)
        
        # Extract the player name from the page
        player_name = response.xpath('//div[@id="meta"]/div/h1/span/text()').get()
        
        if not player_name:
            self.logger.error("Player name not found on page: %s", response.url)
            return
        
        # Extract the stats table
        table = response.xpath('//table[@id="last5"]')
        
        if not table:
            self.logger.error("Stats table not found for player: %s", player_name)
            return
        
        self.logger.info("Stats table found for player: %s", player_name)
        
        # Extract the rows for the last 5 games
        rows = table.xpath('.//tbody/tr')
        
        if not rows:
            self.logger.error("No rows found in the stats table for player: %s", player_name)
            return
        
        self.logger.info("Found %d rows for player: %s", len(rows), player_name)

        for row in rows:
            date = row.xpath('.//th[@data-stat="date"]/a/text()').get()
            team = row.xpath('.//td[@data-stat="team_name_abbr"]/a/text()').get()
            opponent = row.xpath('.//td[@data-stat="opp_name_abbr"]/a/text()').get()
            result = row.xpath('.//td[@data-stat="game_result"]/text()').get()
            minutes_played = row.xpath('.//td[@data-stat="mp"]/text()').get()
            field_goals = row.xpath('.//td[@data-stat="fg"]/text()').get()
            field_goal_attempts = row.xpath('.//td[@data-stat="fga"]/text()').get()
            field_goal_percentage = row.xpath('.//td[@data-stat="fg_pct"]/text()').get()
            three_point_field_goals = row.xpath('.//td[@data-stat="fg3"]/text()').get()
            three_point_field_goal_attempts = row.xpath('.//td[@data-stat="fg3a"]/text()').get()
            three_point_field_goal_percentage = row.xpath('.//td[@data-stat="fg3_pct"]/text()').get()
            free_throws = row.xpath('.//td[@data-stat="ft"]/text()').get()
            free_throw_attempts = row.xpath('.//td[@data-stat="fta"]/text()').get()
            free_throw_percentage = row.xpath('.//td[@data-stat="ft_pct"]/text()').get()
            offensive_rebounds = row.xpath('.//td[@data-stat="orb"]/text()').get()
            defensive_rebounds = row.xpath('.//td[@data-stat="drb"]/text()').get()
            total_rebounds = row.xpath('.//td[@data-stat="trb"]/text()').get()
            assists = row.xpath('.//td[@data-stat="ast"]/text()').get()
            steals = row.xpath('.//td[@data-stat="stl"]/text()').get()
            blocks = row.xpath('.//td[@data-stat="blk"]/text()').get()
            turnovers = row.xpath('.//td[@data-stat="tov"]/text()').get()
            personal_fouls = row.xpath('.//td[@data-stat="pf"]/text()').get()
            points = row.xpath('.//td[@data-stat="pts"]/text()').get()
            game_score = row.xpath('.//td[@data-stat="game_score"]/text()').get()
            plus_minus = row.xpath('.//td[@data-stat="plus_minus"]/text()').get()

            self.logger.info("Extracted stats for %s: date=%s, team=%s, opponent=%s, result=%s, minutes_played=%s, field_goals=%s, field_goal_attempts=%s, field_goal_percentage=%s, three_point_field_goals=%s, three_point_field_goal_attempts=%s, three_point_field_goal_percentage=%s, free_throws=%s, free_throw_attempts=%s, free_throw_percentage=%s, offensive_rebounds=%s, defensive_rebounds=%s, total_rebounds=%s, assists=%s, steals=%s, blocks=%s, turnovers=%s, personal_fouls=%s, points=%s, game_score=%s, plus_minus=%s",
                             player_name, date, team, opponent, result, minutes_played, field_goals, field_goal_attempts, field_goal_percentage, three_point_field_goals, three_point_field_goal_attempts, three_point_field_goal_percentage, free_throws, free_throw_attempts, free_throw_percentage, offensive_rebounds, defensive_rebounds, total_rebounds, assists, steals, blocks, turnovers, personal_fouls, points, game_score, plus_minus)

            yield {
                'player_name': player_name,
                'date': date,
                'team': team,
                'opponent': opponent,
                'result': result,
                'minutes_played': minutes_played,
                'field_goals': field_goals,
                'field_goal_attempts': field_goal_attempts,
                'field_goal_percentage': field_goal_percentage,
                'three_point_field_goals': three_point_field_goals,
                'three_point_field_goal_attempts': three_point_field_goal_attempts,
                'three_point_field_goal_percentage': three_point_field_goal_percentage,
                'free_throws': free_throws,
                'free_throw_attempts': free_throw_attempts,
                'free_throw_percentage': free_throw_percentage,
                'offensive_rebounds': offensive_rebounds,
                'defensive_rebounds': defensive_rebounds,
                'total_rebounds': total_rebounds,
                'assists': assists,
                'steals': steals,
                'blocks': blocks,
                'turnovers': turnovers,
                'personal_fouls': personal_fouls,
                'points': points,
                'game_score': game_score,
                'plus_minus': plus_minus,
            }
