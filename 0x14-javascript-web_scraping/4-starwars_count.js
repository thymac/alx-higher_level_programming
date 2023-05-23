#!/usr/bin/node
/*
A script that prints the number of movies where the character "Wedge Antilles" is present.
The first argument is the API URL of the Star wars API: https://swapi-api.alx-tools.com/api/films/
Wedge Antilles is character ID 18 - your script must use this ID for filtering the result of the API
You must use the module request
*/

const request = require('request');

const URL = process.argv[2];

request(URL, (error, response, body) => {
  if (error) {
    console.log(error);
  } else if (body) {
    const json = JSON.parse(body);
    const charFilms = json.results.filter(
      x => x.characters.find(y => y.match(/\/people\/18\/?$/))
    );
    console.log(charFilms.length);
  }
});
