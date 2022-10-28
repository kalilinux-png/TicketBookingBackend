
function collect_data() {
    let movie = document.querySelector("#movies")
    let movie_name = movie.options[movie.selectedIndex].innerHTML
    alert(movie_name)
}