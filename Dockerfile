FROM python:3.9
WORKDIR /app
COPY requirments.txt requirments.txt
RUN pip install -r requirments.txt
COPY . .
CMD ["python", "-m", "flask", "run", "--host", "0.0.0.0"]
