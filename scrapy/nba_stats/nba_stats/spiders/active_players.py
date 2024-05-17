import scrapy


class ActivePlayersSpider(scrapy.Spider):
    name = "active_players"
    allowed_domains = ["basketball-reference.com"]
    
    # Generate start_urls for all letters from 'a' to 'z'
    #start_urls = [f"https://www.basketball-reference.com/players/{chr(letter)}/" for letter in range(ord('a'), ord('z') + 1)]
    start_urls = [f"https://www.basketball-reference.com/players/{chr(letter)}/" for letter in range(ord('a'), ord('b') + 1)]

    def parse(self, response):
        # Extract active players' links
        for player in response.xpath('//th[@scope="row" and @class="left " and @data-stat="player"]/strong/a'):
            yield {
                'name': player.xpath('text()').get(),
                'url': response.urljoin(player.xpath('@href').get())
            }