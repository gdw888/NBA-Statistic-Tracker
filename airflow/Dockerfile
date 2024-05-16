FROM apache/airflow:2.3.0

# Set the working directory to /opt/airflow
WORKDIR /opt/airflow

# Copy the requirements.txt file from the host to the image
COPY requirements.txt /opt/airflow/requirements.txt

RUN pip install --no-cache-dir -r /opt/airflow/requirements.txt

# Optional: Copy any custom entrypoint script
# COPY entrypoint.sh /entrypoint.sh
# RUN chmod +x /entrypoint.sh

# Default entrypoint script from airflow image
ENTRYPOINT ["/entrypoint"]

# Default command to run
CMD ["webserver"] # This will be overridden by the docker-compose command
