install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:
	#format code
	black *.py srs/*.py

test:
	python -m pytest --v

build:
	#build container
	docker build -t deploy-api

run:
	#run docker

deploy:
	docker build -t 

all: install deploy