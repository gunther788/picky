#!/bin/bash

curl -X PUT "http://localhost:5000/webservers" -H "accept: */*" -H "Content-Type: application/json" -d "{\"name\":\"webservers\"}"
sleep 2
curl -X PUT "http://localhost:5000/webservers/sample.example.com" -H "accept: */*" -H "Content-Type: application/json" -d "{\"name\":\"sample.example.com\", \"state\":\"DOWN\"}"
sleep 2
curl -X PUT "http://localhost:5000/webservers/sample.example.com" -H "accept: */*" -H "Content-Type: application/json" -d "{\"name\":\"sample.example.com\", \"state\":\"UP\"}"
sleep 2
curl -X PUT "http://localhost:5000/webservers/sample.example.com/https" -H "accept: */*" -H "Content-Type: application/json" -d "{\"name\":\"https\",\"output\":\"some output of the service check\",\"state\":\"WARNING\"}"
sleep 2
curl -X PUT "http://localhost:5000/webservers/sample.example.com/https" -H "accept: */*" -H "Content-Type: application/json" -d "{\"name\":\"https\",\"output\":\"some output of the service check\",\"state\":\"OK\"}"
sleep 2
curl -X PUT "http://localhost:5000/webservers/sample.example.com/https" -H "accept: */*" -H "Content-Type: application/json" -d "{\"name\":\"https\",\"output\":\"some output of the service check\",\"state\":\"WARNING\"}"
sleep 2
curl -X PUT "http://localhost:5000/webservers/sample.example.com/https" -H "accept: */*" -H "Content-Type: application/json" -d "{\"name\":\"https\",\"output\":\"some output of the service check\",\"state\":\"OK\"}"
sleep 2
curl -X PUT "http://localhost:5000/webservers/sample.example.com/https" -H "accept: */*" -H "Content-Type: application/json" -d "{\"name\":\"https\",\"output\":\"some output of the service check\",\"state\":\"WARNING\"}"
sleep 2
curl -X PUT "http://localhost:5000/webservers/sample.example.com/https" -H "accept: */*" -H "Content-Type: application/json" -d "{\"name\":\"https\",\"output\":\"some output of the service check\",\"state\":\"CRITICAL\"}"
sleep 2
curl -X PUT "http://localhost:5000/webservers/sample.example.com/https" -H "accept: */*" -H "Content-Type: application/json" -d "{\"name\":\"https\",\"output\":\"some output of the service check\",\"state\":\"WARNING\"}"
sleep 2
curl -X PUT "http://localhost:5000/webservers/sample.example.com/https" -H "accept: */*" -H "Content-Type: application/json" -d "{\"name\":\"https\",\"output\":\"some output of the service check\",\"state\":\"CRITICAL\"}"
sleep 2
curl -X PUT "http://localhost:5000/webservers/sample.example.com/https" -H "accept: */*" -H "Content-Type: application/json" -d "{\"name\":\"https\",\"output\":\"some output of the service check\",\"state\":\"WARNING\"}"
sleep 2
curl -X PUT "http://localhost:5000/webservers/sample.example.com/https" -H "accept: */*" -H "Content-Type: application/json" -d "{\"name\":\"https\",\"output\":\"some output of the service check\",\"state\":\"OK\"}"
sleep 2
curl -X PUT "http://localhost:5000/webservers/sample.example.com/https" -H "accept: */*" -H "Content-Type: application/json" -d "{\"name\":\"https\",\"output\":\"some output of the service check\",\"state\":\"CRITICAL\"}"
sleep 2
curl -X PUT "http://localhost:5000/webservers/sample.example.com/https" -H "accept: */*" -H "Content-Type: application/json" -d "{\"name\":\"https\",\"output\":\"some output of the service check\",\"state\":\"WARNING\"}"
sleep 2
curl -X PUT "http://localhost:5000/webservers/sample.example.com" -H "accept: */*" -H "Content-Type: application/json" -d "{\"name\":\"sample.example.com\", \"state\":\"UP\"}"

