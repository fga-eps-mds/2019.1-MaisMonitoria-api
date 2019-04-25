run:
	docker-compose -f docker-compose.yml up

run-d:
	docker-compose -f docker-compose.yml up -d

down:
	docker-compose -f docker-compose.yml down

tests:
	docker exec api_gateway bash -c "bash run-tests.sh"

run-tests:
	docker-compose exec api_gateway coverage run manage.py test

cov-tests:
	docker-compose exec api_gateway coverage report -m

run-dc-tests:
	docker network create api-backend 
	docker-compose -f docker-compose.yml build
	docker-compose -f docker-compose.yml up -d