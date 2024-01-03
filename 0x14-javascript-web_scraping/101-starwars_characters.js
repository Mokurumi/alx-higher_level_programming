#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.error('error:', error);
  } else {
    const characters = JSON.parse(body).characters;
    getCharacter(characters, 0);
  }
});

function getCharacter (characters, index) {
  request(characters[index], (error, response, body) => {
    if (error) {
      console.log(error);
    } else {
      console.log(JSON.parse(body).name);
    }
    if (index + 1 < characters.length) {
      getCharacter(characters, index + 1);
    }
  });
}
