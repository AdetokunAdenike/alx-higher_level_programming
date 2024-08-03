#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const API_URL = 'https://swapi-api.alx-tools.com/api/films/';

request(`${API_URL}${movieId}/`, (error, response, body) => {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const data = JSON.parse(body);
    console.log(data.title);
  } else {
    console.log('Error code:', response.statusCode);
  }
});
