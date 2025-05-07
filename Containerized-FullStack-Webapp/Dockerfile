FROM python:alpine3.10
LABEL "NAME"="Backend"
WORKDIR /app
COPY requirements.txt /app 
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ADD . /app
EXPOSE 9000
CMD ["python", "main.py"]
