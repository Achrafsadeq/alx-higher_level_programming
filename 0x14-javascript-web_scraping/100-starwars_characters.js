#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const characters = JSON.parse(body).characters;
    characters.forEach(characterUrl => {
      request(characterUrl, (charError, charResponse, charBody) => {
        if (charError) {
          console.log(charError);
        } else {
          console.log(JSON.parse(charBody).name);
        }
      });
    });
  }
});
