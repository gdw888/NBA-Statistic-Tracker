# Basketball Player Stats ETL System

## Description
The Basketball Player Stats ETL System is designed to automate the extraction, transformation, and loading (ETL) of basketball player statistics from unstructured web pages, specifically from player profiles on Basketball Reference. The goal is to capture raw data and enrich it with advanced analytics, such as performance trends and head-to-head statistics against specific teams. This system targets basketball analysts and enthusiasts who require detailed and digestible insights into player performances.

## Table of Contents
1. [Installation](#installation)
2. [Usage](#usage)
3. [Features](#features)
4. [Contributing](#contributing)
5. [Authors and Acknowledgments](#authors-and-acknowledgments)
6. [Support](#support)
7. [Roadmap](#roadmap)
8. [Changelog](#changelog)
9. [References](#references)

## Installation
### Prerequisites
- Docker
- PostgreSQL
- Python 3.8+
- Apache Airflow
- PySpark

### Steps
1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/basketball-stats-etl.git
    cd basketball-stats-etl
    ```
2. Set up the Docker containers:
    ```sh
    docker-compose up -d
    ```
3. Install Python dependencies:
    ```sh
    pip install -r requirements.txt
    ```
4. Initialize the PostgreSQL database using the provided schema.

## Usage
### Running the ETL Pipeline
1. Start the Airflow web server:
    ```sh
    airflow webserver
    ```
2. Start the Airflow scheduler in another terminal:
    ```sh
    airflow scheduler
    ```
3. Trigger the ETL workflow via the Airflow UI or CLI.

### Accessing the Data
- The raw and transformed data can be accessed from the PostgreSQL database.
- Use SQL queries or any preferred database management tool to interact with the data.

## Features
- Real-time data extraction from Basketball Reference player profiles.
- Automated daily extraction of basketball player statistics.
- Storage of raw and derived analytics in a structured PostgreSQL database.
- Calculation of basic analytics like average points per game.

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new feature branch.
    ```sh
    git checkout -b feature/YourFeature
    ```
3. Commit your changes.
    ```sh
    git commit -m "Add feature: YourFeature"
    ```
4. Push to the branch.
    ```sh
    git push origin feature/YourFeature
    ```
5. Open a pull request.

## Authors and Acknowledgments
- **Terry Lee** - *Initial work* - [TerryLee](https://github.com/gdw888/)
- Thanks to the contributors of the libraries and tools used in this project.

## Support
For support, please open an issue in the repository or contact me at uwgdw88@gmail.com.

## Roadmap
- [ ] Implement additional advanced analytics.
- [ ] Expand to include additional statistics based on user feedback.
- [ ] Optimize data extraction and transformation processes.

## Changelog
### v1.0.0
- Initial release with core ETL functionalities.

## References
- [Basketball Reference](https://www.basketball-reference.com/) - Source of player statistics.
- [Scrapy Documentation](https://docs.scrapy.org/en/latest/)
- [Apache Airflow Documentation](https://airflow.apache.org/docs/)
- [PySpark Documentation](https://spark.apache.org/docs/latest/api/python/)
