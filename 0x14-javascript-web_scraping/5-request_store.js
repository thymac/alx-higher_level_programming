#!/usr/bin/node
/*
A script that gets the contents of a webpage and stores it in a file.
The first argument is the URL to request
The second argument the file path to store the body response
The file must be UTF-8 encoded
You must use the module request
*/

const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const filePath = process.argv[3];

request.get(url, (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    fs.writeFile(filePath, body, { encoding: 'utf-8' }, (err) => {
      if (err) {
        console.error(err);
      } else {
        console.log(`The contents of the webpage have been stored in the file: ${filePath}`);
      }
    });
  }
});

