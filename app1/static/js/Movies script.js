let categoriesLis = document.querySelectorAll(".categories li");
let movies = document.querySelectorAll(".movies .movie");

categoriesLis.forEach((li) => {
    li.addEventListener("click", removeActive);
    li.addEventListener("click", manageMovies);
})

function removeActive() {
    categoriesLis.forEach((li) => {
        li.classList.remove("active");
        this.classList.add("active");
    });
}

function manageMovies() {
    movies.forEach((movie) => {
        movie.style.display = "none";
    });
    document.querySelectorAll(this.dataset.cat).forEach((el) => {
        el.style.display = "block";
    });
}