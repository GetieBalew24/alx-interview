#!/usr/bin/node


const request = require('request');
const Film_Id = process.argv[2];
const Movie_url = {
  url: 'https://swapi-api.alx-tools.com/api/films/' + Film_Id,
  method: 'GET'
};

request(Movie_url, function (error, response, body) {
  if (!error) {
    const chars = JSON.parse(body).characters;
    printCharacters(chars, 0);
  }
});

function printCharacters (chars, index) {
  request(chars[index], function (error, response, body) {
    if (!error) {
      console.log(JSON.parse(body).name);
      if (index + 1 < chars.length) {
        printCharacters(chars, index + 1);
      }
    }
  });
}