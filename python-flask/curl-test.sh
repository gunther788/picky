#!/bin/bash

curl -X PUT "http://localhost:5000/webservers" -H "accept: */*" -H "Content-Type: application/json" -d "{\"name\":\"webservers\"}"
curl -X PUT "http://localhost:5000/webservers/sample.example.com" -H "accept: */*" -H "Content-Type: application/json" -d "{\"name\":\"sample.example.com\"}"
