#!/bin/bash

# Substitute environment variable PROJECT_NAME into the command to start Gunicorn
exec gunicorn ${PROJECT_NAME}.wsgi:application --bind 0.0.0.0:8000
