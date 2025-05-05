FROM ubuntu:latest
LABEL "PROJECT"="APACHE-WEBSITE"
ENV DEBIAN_FRONTEND=noninteractive
RUN apt update && apt install -y apache2
RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf
WORKDIR /var/www/html
COPY .  /var/www/html
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]
EXPOSE 80
 
