#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const characters = JSON.parse(body).characters;
    const fetchCharacter = (index) => {
      if (index >= characters.length) return;
      request(characters[index], (charError, charResponse, charBody) => {
        if (charError) {
          console.log(charError);
        } else {
          console.log(JSON.parse(charBody).name);
          fetchCharacter(index + 1);
        }
      });
    };
    fetchCharacter(0);
  }
});
