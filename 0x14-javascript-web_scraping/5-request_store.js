#!/iusr/bin/node
/*
A script that computes the number of tasks completed by user id.
The first argument is the API URL: https://jsonplaceholder.typicode.com/todos
Only print users with completed task
You must use the module request
*/

const request = require('request');
const fs = require('fs');

const baseURL = process.argv[2];
const bodyResp = process.argv[3];
request(baseURL, (error, response, body) => {
  if (error == null) {
    fs.writeFileSync(bodyResp, body);
  }
});
