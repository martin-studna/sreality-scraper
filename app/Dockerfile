FROM python:latest

WORKDIR /code
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN playwright install
RUN playwright install-deps
COPY srealityspider.py srealityspider.py
COPY flat_post_repository.py flat_post_repository.py 
COPY main.py main.py
CMD ["python", "main.py"]