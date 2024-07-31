#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode === 200) {
    const movieData = JSON.parse(body);
    const characterUrls = movieData.characters;

    characterUrls.forEach((characterUrl, index) => {
      request(characterUrl, (err, res, characterBody) => {
        if (err) {
          console.error('Error:', err);
          return;
        }

        if (res.statusCode === 200) {
          const characterData = JSON.parse(characterBody);
          console.log(characterData.name);
        } else {
          console.error('Error code:', res.statusCode);
        }
      });
    });
  } else {
    console.error('Error code:', response.statusCode);
  }
});
