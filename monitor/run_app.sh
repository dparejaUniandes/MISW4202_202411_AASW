#!/bin/sh
flask run --host=0.0.0.0 --debug & celery -A tarea worker --loglevel=info