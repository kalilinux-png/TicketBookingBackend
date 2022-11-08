
function scrap_values() {
    alert("hello from data function")
    let movie = document.querySelector("#movies")
    let movie_name = movie.options[movie.selectedIndex].innerHTML
    let place = document.querySelector("#movies1")
    let place_name = place.options[place.selectedIndex].innerHTML
    let theather = document.querySelector("#movies6")
    let theather_name = theather.options[theather.selectedIndex].innerHTML
    let dimension = document.querySelector("#movies7")
    let dimension_name  = dimension.options[dimension.selectedIndex].innerHTML
    let time  = document.querySelector("#movies2")
    let time_value = time.options[time.selectedIndex].innerHTML
    let no_of_seats = document.querySelector("#movies3")
    let no_of_seats_value = no_of_seats.options[no_of_seats.selectedIndex].innerHTML
    let type_of_seat = document.querySelector("#movies4")
    let type_of_seat_name = type_of_seat.options[type_of_seat.selectedIndex].innerHTML
    let type_of_food = document.querySelector("#food")
    let type_of_food_name = type_of_food.options[type_of_food.selectedIndex].innerHTML
    let date = document.querySelector("#moviedate").value
    let json_object = {
        movie_name : movie_name,
        place_name : place_name,
        theather_name:theather_name,
        dimension_name:dimension_name,
        time_value :time_value,
        no_of_seats_value:no_of_seats_value,
        type_of_food_name:type_of_food_name,
        date:date
    }
    console.log(json_object)
    return json_object
   
   }

function call_api(json_data) {
 const options = {method: 'POST', body: JSON.stringify(json_data)};

fetch('http://127.0.0.1:5000/upload/user_data/', options)
  .then(response => response.text())
  .then(response => {document.body.innerHTML = response})
  .catch(err => console.error(err));

}

function main() { 
    alert("Inside main function")
    json_data = scrap_values()
    call_api(json_data)
}
