#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const characters = JSON.parse(body).characters;
    characters.forEach(character => {
      request(character, (err, res, bod) => {
        if (err) {
          console.error(err);
        } else {
          console.log(JSON.parse(bod).name);
        }
      });
    });
  }
});
