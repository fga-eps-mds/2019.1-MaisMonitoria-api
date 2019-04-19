run:
	docker-compose -f docker-compose.yml up -d

down:
	docker-compose -f docker-compose.yml down

tests:
	docker exec api_gateway bash -c "bash run-tests.sh"

run-dc-tests:
	docker network create api-backend 
	docker-compose -f docker-compose.yml build
	docker-compose -f docker-compose.yml up -d

unit-tests:
	echo "Running Unit Tests"
	docker exec api_gateway bash -c "bash run-tests.sh"
	docker-compose -f docker-compose.yml down
	docker-compose -f docker-compose.yml rm -f -s