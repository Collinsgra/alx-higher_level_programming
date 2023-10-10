#!/usr/bin/node
const request = require('request');

function fetchCharacterNames(filmId) {
  const url = `https://swapi-api.hbtn.io/api/films/${filmId}/`;

  request(url, function (error, response, body) {
    if (!error) {
      const filmData = JSON.parse(body);
      const characters = filmData.characters;
      printCharacters(characters, 0);
    }
  });
}

function printCharacters(characters, index) {
  if (index >= characters.length) {
    return; // Exit when all characters have been printed
  }

  request(characters[index], function (error, response, body) {
    if (!error) {
      const characterData = JSON.parse(body);
      console.log(characterData.name);
      printCharacters(characters, index + 1);
    }
  });
}

// Check if a film ID is provided as a command-line argument
const filmId = process.argv[2];
if (!filmId) {
  console.error('Please provide a film ID as a command-line argument.');
} else {
  fetchCharacterNames(filmId);
}
