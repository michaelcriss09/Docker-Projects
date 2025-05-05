
FROM nginx:alpine
LABEL "Name:"="Frontend"
WORKDIR /usr/share/nginx/html
RUN rm -rf /usr/share/nginx/html/*
COPY ./frontend /usr/share/nginx/html
EXPOSE 80
