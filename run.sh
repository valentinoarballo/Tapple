#!/bin/bash

gunicorn app:app --bind 0.0.0.0:5055 --reload
