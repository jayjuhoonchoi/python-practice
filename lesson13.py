import logging

logging.basicConfig(
    filename="sensor.log",
    level=logging.INFO
)

logging.info("Sensor check started")
logging.warning("Temperature is high")