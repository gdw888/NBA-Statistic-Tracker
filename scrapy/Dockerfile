FROM python:3.8-slim

WORKDIR /usr/src/app

# Copy the requirements.txt file from the host to the image
COPY requirements.txt /usr/src/app/requirements.txt

RUN pip install --no-cache-dir -r /usr/src/app/requirements.txt

# Set entrypoint to run Scrapy
ENTRYPOINT ["scrapy"]
CMD ["crawl", "player_stats"]