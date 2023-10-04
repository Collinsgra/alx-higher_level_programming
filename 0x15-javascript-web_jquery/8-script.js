$.get('https://swapi-api.alx-tools.com/api/films/?format=json', (response) => {
  for (let i = 0; i < response.results.length; i++) {
    const movieTitle = `<li>${response.results[i].title}</li>`;
    $('ul#list_movies').append(movieTitle);
  }
});
