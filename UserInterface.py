from controller.Controller import Controller

"""
Here you can give your input parameters. Run this class to create your solution.
Solution will be added to the 'working_dir_folder' and sent to your email.
"""

# INPUT BEGIN ------------------------------------------------------------------

# Environment
env_pos = (0, 0, 0)
env_point_A = (0, 5000, 5000)
env_point_B = (10000, 5000, 5000)
env_length = 10000
env_width = 10000
env_height = 10000

# Equipment 1
equ1_pos = (2500, 4500, 4500)
equ1_point_in = (2500, 5000, 5000)
equ1_point_out = (3500, 5000, 5000)
equ1_length = 1000
equ1_width = 1000
equ1_height = 1000

# Equipment 2
equ2_pos = (5500, 4500, 4500)
equ2_point_in = (5500, 5000, 5000)
equ2_point_out = (6000, 5000, 5000)
equ2_length = 500
equ2_width = 1000
equ2_height = 1000

# # Equipment 3
# equ3_pos = ""
# equ3_point_in = ""
# equ3_point_out = ""
# equ3_length = ""
# equ3_width = ""
# equ3_height = ""

# Pipe
pipe_diameter_outer = 300
pipe_diameter_inner = 250
elbow_curve_radius = 90

# Email
email = "email@gmail.com"


# INPUT END --------------------------------------------------------------------

env_args = [env_pos, env_point_A, env_point_B, env_length, env_width, env_height]

equ1_args = [equ1_pos, equ1_point_in, equ1_point_out, equ1_length, equ1_width, equ1_height]
equ2_args = [equ2_pos, equ2_point_in, equ2_point_out, equ2_length, equ2_width, equ2_height]
# equ3_args = [equ3_pos, equ3_point_in, equ3_point_out, equ3_length, equ3_width, equ3_height]
equs_args = [equ1_args, equ2_args]

pipe_args = [pipe_diameter_outer, pipe_diameter_inner, elbow_curve_radius]

Controller.construct(env_args, equs_args, pipe_args, email)