FROM ubuntu:latest
LABEL "PROJECT"="APACHE-WEBSITE"
ENV DEBIAN_FRONTEND=noninteractive
WORKDIR /var/www/html
RUN apt update && apt install -y apache2
RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf
RUN rm -rf /var/www/hmtl/*
COPY ./apache-project-1  /var/www/html
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]
EXPOSE 80
 
