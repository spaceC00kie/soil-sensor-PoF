const Gpio = require("onoff").Gpio

const sensor = new Gpio(2, "in")

const isWet = () => {
  console.log(sensor.readSync())
}

setInterval(isWet, 5000)
