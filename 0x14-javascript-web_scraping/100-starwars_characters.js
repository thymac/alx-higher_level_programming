#!/usr/bin/env node
/*
A script that prints all characters of a Star Wars movie:
The first argument is the Movie ID - example: 3 = “Return of the Jedi”
Display one character name by line
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

    characters.forEach((characterUrl) => {
      request.get(characterUrl, (err, response, body) => {
        if (err) {
          console.error(err);
        } else {
          const character = JSON.parse(body);
          console.log(character.name);
        }
      });
    });
  }
});

