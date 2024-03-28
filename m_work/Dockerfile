FROM python:3.11-slim-bookworm
#FROM python:3.8.12-slim

COPY package_folder package_folder
COPY requirements.txt requirements.txt
COPY models models
COPY modelsv5 modelsv5
COPY setup.py setup.py

#RUN pip install requirements.txt
#RUN pip install -e .
RUN pip install --upgrade pip
RUN pip install -e .

# on my disk run it
#CMD uvicorn package_folder.api_file:app --reload

# run Container locally- uncomment this one
#CMD uvicorn package_folder.api_file:app --host 0.0.0.0

# run Container Deployed
CMD uvicorn package_folder.api_file:app --host 0.0.0.0 --port $PORT
