install:
	pip install -r requirements.txt

start: stop
	@gunicorn app:app -p run/gunicorn.pid 2>/dev/null &
	@echo "Server started"

stop:
	@if [ -a run/gunicorn.pid ] ; \
	then \
	kill `cat run/gunicorn.pid` ; \
	fi;

test: stop
	@if [ -a db/teste.db ] ; \
        then \
        rm db/teste.db ; \
        fi;
	@sed -i.bu 's/desafio/teste/' models.py
	@gunicorn app:app -p run/gunicorn.pid 2>/dev/null &
	@sed -i.bu 's/desafio/teste/' models.py
	@python -m unittest discover
	@sed -i.bu 's/teste/desafio/' models.py
	@rm db/teste.db models.py.bu
