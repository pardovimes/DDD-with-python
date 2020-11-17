run:
	docker-compose up --build

install:
	docker exec -it football-test_football-app_1 pip install -r requirements.txt

shell:
	docker exec -it football-test_football-app_1 bash

flaskshell:
	docker exec -it football-test_football-app_1 flask shell

test:
	docker exec -it football-test_football-app_1 pytest tests
