#!/usr/bin/node
/*
A script that prints the number of movies where the character "Wedge Antilles" is present.
The first argument is the API URL of the Star wars API: https://swapi-api.alx-tools.com/api/films/
Wedge Antilles is character ID 18 - your script must use this ID for filtering the result of the API
You must use the module request
*/

const request = require('request');

const apiUrl = process.argv[2];
const characterId = 18;

request.get(apiUrl, (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    const films = JSON.parse(body).results;
    const count = films.filter((film) =>
      film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)
    ).length;
    console.log(count);
  }
});

