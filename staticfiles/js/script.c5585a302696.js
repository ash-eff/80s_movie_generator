const movieData = document.getElementById('movieData');
const getRandomMovieButton = document.getElementById('getRandomMovieButton');

function displayRandomMovie() {
    fetch('/api/v1/get_random_movie/')
        .then(response => response.json())
        .then(data => {
            movieData.innerHTML = `
            <h2>${data.title}</h2>
            <p><strong>Release Year:</strong> ${data.release_year}<br>
            <strong>Rating:</strong> ${data.rating}<br>
            <strong>Runtime:</strong> ${data.runtime}<br>
            <strong>Genre:</strong> ${data.genre}<br>
            <strong>Description:</strong> ${data.description}<br>
            <strong>Director:</strong> ${data.director}<br>
            <strong>Stars:</strong> ${data.stars}<br>
            <strong>IMDb Link: </strong><a href="${data.movie_url}" target="_blank">${data.title}</a><p>
            `;      
        })
        .catch(error => {
            console.error('Error:', error);
        });
    }
getRandomMovieButton.addEventListener('click', displayRandomMovie);