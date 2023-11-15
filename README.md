### Tracking and Tracing API Documentation

## Introduction
The tracking and tracing page allows end-users (recipient of a shipment) to monitor the status of their shipment.
This document documents the Tracking and Tracing API. This API allows end-users (shipment recipient) to monitor the status of their shipment and simultaneously be aware of the current weather conditions in their location.
A CSV file (below) containing sample shipment and article data is provided for seeding data structures.

## Features
- Ability to search for shipment by tracking number and carrier
- Display shipment information including current status, sender and recipient addresses, name and quantity of items, price, and SKU
- Display current weather information in the recipient shipment location

## Architecture
- This API is implemented using the Django framework and based on the Django-Styleguide structure
- PostgreSQL database
- Using the OpenWeatherMap API 

## Usage
To use this API, users must first send a request to the server that includes the following parameters:
- Tracking number (tracking_number)
- Carrier (carrier)
If successful, the API will return a JSON response that includes the following information:
- Tracking number (tracking_number)
- Carrier (carrier)
- Shipment status (status)
- Sender address (sender_address)
- Recipient address (receiver_address)
- Item name and quantity (article_name, article_quantity)
- Item price (article_price)
- SKU (SKU)
- Current weather information in the recipient shipment location (weather_information)
### Example request:
 
### Example response:
 

## Note:
To retrieve weather information, it uses a free third-party weather API. Therefore, there may be limitations on the number of API requests.

## Important design considerations:
- For any project, we can implement different structures based on the needs and goals of the project. Each structure has its own strengths and weaknesses. The Django Style guide structure seems appropriate for this project.
- In the shipment information section, we have tried to provide a good final output with the appropriate Model structure. If it is to be developed, the information can be used for statistical and reporting purposes in a differentiated manner.
- To reduce server costs, only cities that are in the list of undelivered shipments are updated from the API every two hours. Care has been taken to ensure that duplicate cities are not updated again.

## Deployment
- Web server with appropriate configuration for running Django application
- PostgreSQL database for storing shipment information
- Valid weather API for retrieving weather information

## To manage 1000 requests per second:
- Use different databases alongside the main database, such as MongoDB and Redis.
	- One of the advantages of using Redis and similar databases that are placed on Memory can be mentioned the high speed of them and it is very suitable for storing non-essential information such as weather status information that is updated every two hours and in case of loss of information, the whole process does not have a problem. It reduces the traffic of the main bank.
	- One of the weaknesses of these types of banks is the occupation of short-term server memory, which also costs a lot.
- Although one of the great advantages of frameworks like Django is having an ORM, and to prevent duplicate queries, it has functions such as select_related and prefetch_related, but in many projects, it is better for many of the SQL codes to be written by the programmer himself to have better speed and performance.
- Use load balancing techniques to distribute requests between multiple servers.

## Final note:
This project has been implemented in a short time and there is definitely a lot of work to be done to reach an ideal product in terms of project structure, models, clean coding, etc.

## project setup

1- SetUp venv
```
python -m venv venv
source venv/bin/activate
```

2- install Dependencies
```
pip install -r requirements_dev.txt
```

3- create your env
```
cp .env.example .env
```

4- spin off docker compose
```
docker compose -f docker-compose.dev.yml up -d
```

5- Create tables
```
python manage.py migrate
```

6- run the project
```
python manage.py runserver
```

7- Celery and celery beat

```
  python manage.py setup_periodic_tasks
  celery -A tracktrace.tasks worker -l info --without-gossip --without-mingle --without-heartbeat
  celery -A tracktrace.tasks beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler
```
