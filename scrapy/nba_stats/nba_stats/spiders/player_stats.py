import scrapy


class PlayerStatsSpider(scrapy.Spider):
    name = "player_stats"
    allowed_domains = ["basketball-reference.com"]
    start_urls = ["https://basketball-reference.com"]

    def parse(self, response):
        pass
