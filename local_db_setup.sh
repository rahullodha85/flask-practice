#!/bin/bash

# ASSUMING database is up and running

ENV=dev FLASK_APP=run.py flask db init
ENV=dev FLASK_APP=run.py flask db migrate
ENV=dev FLASK_APP=run.py flask db upgrade