// Flask server to pull data from
const HOST = "http://127.0.0.1:5000/";

let temp, humidity, airPressure;

document.addEventListener("DOMContentLoaded", () => {
  temp = document.getElementById("temperature");
  humidity = document.getElementById("humidity");
  airPressure = document.getElementById("air-pressure");
});

async function update() {
  let res = await fetch(`${HOST}data`);
  let json = await res.json();

  if (temp != null) {
    temp.innerHTML = json.temperature + "°F";
    humidity.innerHTML = json.humidity + "%";
    airPressure.innerHTML = json.airPressure + "hPa";
  }
}

// Run update for the first time, then schedule it every 5 minutes
update();
setInterval(update, 5 * 60 * 1000);
