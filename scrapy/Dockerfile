FROM python:3.8-slim

WORKDIR /usr/src/app

# Copy the requirements.txt file from the host to the image
COPY requirements.txt /usr/src/app/requirements.txt

# Install the required Python packages
RUN pip install --no-cache-dir -r /usr/src/app/requirements.txt

# Copy the entire directory into the image
COPY nba_stats /usr/src/app/nba_stats

# Change the working directory to where the Scrapy project is located
WORKDIR /usr/src/app/nba_stats

# Make the shell script executable
RUN chmod +x nba_stats/spiders/start-scrapy.sh

# Set entrypoint to run Scrapy
ENTRYPOINT ["nba_stats/spiders/start-scrapy.sh"]