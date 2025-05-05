FROM node:8.16.1-alpine
LABEL "NAME"="Nodejs-Project"
WORKDIR /app
COPY ./backend-js /app
RUN npm install
EXPOSE 3000
CMD ["node","server.js"]
