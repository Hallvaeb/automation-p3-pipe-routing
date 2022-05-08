from ParameterHolder import ParameterHolder
from controller.Controller import Controller

"""
Check input and run this file to get solution sent to your email!
"""

specify_number_of_equipments_please = 2
email = "insert_your_email@gmail.com"

# INPUT END --------------------------------------------------------------------

env_args, equs_args, pipe_args = ParameterHolder.get_parameter_list(no_of_equs = 2)
Controller.construct(env_args, equs_args, pipe_args, email)