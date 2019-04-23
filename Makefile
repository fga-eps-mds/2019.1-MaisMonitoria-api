run:
	docker-compose -f docker-compose.yml up

run-d:
	docker-compose -f docker-compose.yml up -d

down:
	docker-compose -f docker-compose.yml down

tests:
	docker-compose exec api_gateway py.test --cov=.

run-dc-tests:
	docker network create api-backend 
	docker-compose -f docker-compose.yml build
	docker-compose -f docker-compose.yml up -d
	