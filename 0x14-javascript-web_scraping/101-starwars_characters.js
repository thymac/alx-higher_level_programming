#!/usr/bin/node
/*
A script that prints all characters of a Star Wars movie:
The first argument is the Movie ID - example: 3 = "Return of the Jedi"
Display one character name by line in the same order of the list "characters" in the /films/ response
You must use the Star wars API
You must use the module request
*/

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(apiUrl, (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    const movie = JSON.parse(body);
    const characters = movie.characters;
    let count = 0;

    characters.forEach((characterUrl, index) => {
      request.get(characterUrl, (err, response, body) => {
        if (err) {
          console.error(err);
        } else {
          const character = JSON.parse(body);
          console.log(character.name);
          count++;

          if (count === characters.length) {
            // All characters have been printed
            process.exit(0);
          }
        }
      });
    });
  }
});

