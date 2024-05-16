cd ..

docker-compose run airflow-webserver airflow db init;

docker-compose run airflow-webserver airflow users create \
    --username admin \
    --password admin \
    --firstname Admin \
    --lastname User \
    --role Admin \
    --email uwgdw88@gmail.com;

# docker-compose down
# docker-compose build
# docker-compose up -d