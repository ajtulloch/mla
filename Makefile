proto:
	mkdir -p gen
	find . -iname '*.proto' | xargs -J % protoc --proto_path=. --python_out=gen %
	touch gen/protobufs/__init__.py

freeze:
	pip freeze > requirements.txt

requirements:
	pip install -r requirements.txt

test:
	env/bin/nosetests

db:
	cd frontend
	python db_create.py

.PHONY: server test requirements freeze proto
