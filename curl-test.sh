#!/bin/bash

curl -X PUT "http://localhost:5000/webservers" -H "accept: */*" -H "Content-Type: application/json" -d "{\"name\":\"webservers\"}"
sleep 1
curl -X PUT "http://localhost:5000/webservers/sample.example.com" -H "accept: */*" -H "Content-Type: application/json" -d "{\"name\":\"sample.example.com\", \"state\":\"DOWN\"}"
sleep 1
curl -X PUT "http://localhost:5000/webservers/other.example.com" -H "accept: */*" -H "Content-Type: application/json" -d "{\"name\":\"other.example.com\", \"state\":\"DOWN\"}"
sleep 1
curl -X PUT "http://localhost:5000/webservers/sample.example.com/https" -H "accept: */*" -H "Content-Type: application/json" -d "{\"name\":\"https\",\"output\":\"some output of the service check\",\"state\":\"WARNING\"}"
sleep 1
curl -X PUT "http://localhost:5000/webservers/sample.example.com" -H "accept: */*" -H "Content-Type: application/json" -d "{\"name\":\"sample.example.com\", \"state\":\"UP\"}"
sleep 1
curl -X PUT "http://localhost:5000/webservers/sample.example.com/https" -H "accept: */*" -H "Content-Type: application/json" -d "{\"name\":\"https\",\"output\":\"some output of the service check\",\"state\":\"OK\"}"


