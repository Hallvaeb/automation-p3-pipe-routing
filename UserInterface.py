from inputOutput.ParameterContainer import ParameterContainer
from controller.Controller import Controller

"""
Check input and run this file to get solution sent to your email!
Have you recieved an ID from your engineer? All parameter-IDs are over 3 digits and
will give you the specific solution your engineer created. 

Number of Equs implemented: 2, 3, 4 and 10. The most complex is 10, by far.
"""

number_of_equipments_or_id = 10
email = "your_email_please@gmail.com"

# INPUT END --------------------------------------------------------------------

env_args, equs_args, pipe_args = ParameterContainer.get_parameter_list(number_of_equipments_or_id)
Controller.construct(env_args, equs_args, pipe_args, email)