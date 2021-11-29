
test:
	PYTHONPATH=src venv/bin/python -m pytest ./tests/

install:

	( \
		rm -r venv; \
		python3 -m venv venv; \
	    venv/bin/pip install -r requirements.txt; \
	   	venv/bin/python -m spacy download en_core_web_md; \
	)

generate:
	PYTHONPATH=src venv/bin/python src/client.py