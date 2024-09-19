
build:
	sam build

deploy-infra:
	sam build
	sam deploy

test-backend:
	docker-compose up -d --remove-orphans
	powershell -Command "Start-Sleep -Seconds 5"
	powershell -Command "aws dynamodb list-tables --endpoint-url http://localhost:8000"
	pytest

