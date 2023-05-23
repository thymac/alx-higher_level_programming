#!/usr/bin/node
/*
A script that computes the number of tasks completed by user id.
The first argument is the API URL: https://jsonplaceholder.typicode.com/todos
Only print users with completed task
You must use the module request
*/

const request = require('request');

const baseURL = process.argv[2];
request(baseURL, (error, response, body) => {
  const aggregate = {};
  if (error) {
    console.log(error);
  }
  const json = JSON.parse(body);
  json.forEach(element => {
    if (element.completed) {
      if (!aggregate[element.userId]) {
        aggregate[element.userId] = 0;
      }
      aggregate[element.userId]++;
    }
  });
  console.log(aggregate);
});
