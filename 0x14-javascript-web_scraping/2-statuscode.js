#!/usr/bin/node
/*
A script that display the status code of a GET request.
The first argument is the URL to request (GET)
The status code must be printed like this: code: <status code>
You must use the module request
*/

const request = require('request');
const process = require('process');
const url = process.argv[2];

request.get(url, function (err, response) => {
  if (err == null) {
    console.log(`code: ${response.statusCode}`);
  }
});

