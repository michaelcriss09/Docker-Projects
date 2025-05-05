FROM python:alpine3.10
LABEL "NAME"="Backend"
WORKDIR /app
COPY backend-py/requirements.txt /app/requirements.txt
COPY backend-py/server.py /app/server.py 
RUN pip install --upgrade pip
RUN pip install -r /app/requirements.txt
RUN pip install flask flask-cors
EXPOSE 3000
CMD ["python", "/app/server.py"]


