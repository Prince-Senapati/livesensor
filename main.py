from sensor.exception import SensorException
import sys
from sensor.logger import logging

def test():
    try:
        logging.info("error occured")
        a=1/0
    except Exception as e:
        raise SensorException(e,sys)

if __name__ == "__main__":
    try:
        test()
    except Exception as e:
        print(e)