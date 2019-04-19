run:
	docker-compose -f docker-compose.yml up -d

down:
	docker-compose -f docker-compose.yml down

tests:
	docker exec api_gateway bash -c "bash run-tests.sh"

run-dc-tests:
	docker-compose -f ./composes/${file} build
	docker-compose -f ./composes/${file} up -d

unit-tests:
	echo "Running Unit Tests"
	docker exec api_gateway bash -c "bash run-tests.sh"
	docker-compose -f ./composes/${file} down
	docker-compose -f ./composes/${file} rm -f -s