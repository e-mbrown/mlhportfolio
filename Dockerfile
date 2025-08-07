FROM node:lts-alpine

WORKDIR /myportfolio

COPY package*.json .

RUN npm install

CMD ["npm", "run", "build:css"]

EXPOSE 3000
#########################################

FROM python:3.9-slim

WORKDIR /myportfolio

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY . .

CMD ["flask", "run", "--host=0.0.0.0"]

EXPOSE 5000