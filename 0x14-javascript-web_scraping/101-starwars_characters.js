#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
const movieApiUrl = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

request(movieApiUrl, (err, res, data) => {
  if (!err) {
    const characterUrls = JSON.parse(data).characters;
    fetchCharacterNames(characterUrls, 0);
  }
});

function fetchCharacterNames(urls, position) {
  request(urls[position], (err, res, characterData) => {
    if (!err) {
      console.log(JSON.parse(characterData).name);
      if (position + 1 < urls.length) {
        fetchCharacterNames(urls, position + 1);
      }
    }
  });
}
