all:
	docker-compose build

start:
	docker-compose up

stop:
	docker-compose stop

runserver:
	docker-compose up app

test:
	docker-compose run --rm shell py.test --create-db -vvv -x --pdb

shell:
	docker-compose run --rm app /bin/bash
