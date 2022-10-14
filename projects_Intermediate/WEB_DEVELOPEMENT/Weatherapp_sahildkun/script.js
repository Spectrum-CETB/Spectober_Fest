let weather = {
  apikey : "0440bab35d73c9f2c5ea0f29c25ed388",
  fetchweather: function (city) {

    fetch(
       "https://api.openweathermap.org/data/2.5/weather?q="
       + city 
       +"&units=metric&appid="
       + this.apikey
       ).then((response) => response.json())
       .then((data) => this.displayweather(data))
      
    
  },
  displayweather: function (data) {

    const {name} = data;
    const {icon,description} = data.weather[0];
    const {temp , humidity } = data.main;
    const {speed} = data.wind;
    console.log(name,icon,description,temp,humidity,speed);
    document.querySelector(".city").innerHTML = "Weather in " +  name;
    document.querySelector(".temp").innerHTML = temp + " ℃";
    document.querySelector(".description").innerHTML = description;
    document.querySelector(".humidity").innerHTML = "Humidity : " + humidity + "%";
    document.querySelector(".wind").innerHTML = "Wind speed : "+ speed + "kmph";
    document.querySelector(".weather").classList.remove("loading");
    document.body.style.backgroundImage =
      "url('https://source.unsplash.com/1600x900/?" + name + "')";
  },
  search : function () {
    
    this.fetchweather(document.querySelector(".search-bar").value);
  }
} 


document.querySelector(".search button").addEventListener("click", function () {
  weather.search();
})
document.querySelector(".search-bar").addEventListener("keyup", function (event) {
    if (event.key == "Enter") {
      weather.search();
    }
  });

  weather.fetchWeather("Denver");

  
