#!/bin/bash

# Script to run server in PyCharm
export PYTHONPATH=$PWD/app
uvicorn app.main:app --host 127.0.0.1 --port 8080 --reload