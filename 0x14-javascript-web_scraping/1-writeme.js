#!/usr/bin/env node
// A script that writes a string to a file.
// The first argument is the file path
// The second argument is the string to write
// The content of the file must be written in utf-8
// If an error occurred during while writing, print the error object

const fs = require('fs');
const process = require('process');
const filePath = process.argv[2];
const content = process.argv[3];

fs.writeFile(filePath, content, 'utf-8', function (err, data) => {
  if (err) {
    console.log(err);
  }
});
