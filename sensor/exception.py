import sys
import os
from sensor.logger import logging

def error_msg_detail(error,error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    filename = exc_tb.tb_frame.f_code.co_filename

    error_msg="error occured and the filename is [{0}] and the lineno is [{1}] and error is [{2}]".format(
    filename,exc_tb.tb_lineno,str(error))
    return error_msg

    
class SensorException(Exception):
    def __init__(self,error_msg,error_detail:sys):
        super().__init__(error_msg)

        self.error_msg=error_msg_detail(error_msg,error_detail=error_detail)

    def __str__(self):
        return self.error_msg