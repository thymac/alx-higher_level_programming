// A JavaScript script that fetches and lists the title for all movies
// by using this URL: https://swapi-api.alx-tools.com/api/films/?format=json

const $ = window.$;
$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function(data) {
  data.results.forEach(function(movie) {
    $('#list_movies').append('<li>' + movie.title + '</li>');
  });
});
