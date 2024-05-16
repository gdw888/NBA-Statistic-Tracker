FROM python:3.8-slim

WORKDIR /usr/src/app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Run scrapy when container starts
ENTRYPOINT ["scrapy"]
CMD ["crawl", "myspider"]