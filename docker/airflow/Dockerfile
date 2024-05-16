FROM apache/airflow:2.3.0

# Copy requirements if needed
# COPY requirements.txt .
# RUN pip install -r requirements.txt

# Optional: Copy any custom entrypoint script
# COPY entrypoint.sh /entrypoint.sh
# RUN chmod +x /entrypoint.sh

# Default entrypoint script from airflow image
ENTRYPOINT ["/entrypoint"]

# Default command to run
CMD ["webserver"] # This will be overridden by the docker-compose command
