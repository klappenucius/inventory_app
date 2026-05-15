FROM registry.access.redhat.com/ubi9/python-311

WORKDIR /inva

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "run.py"]
