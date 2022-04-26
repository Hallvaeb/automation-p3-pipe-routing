
from controller.Controller import Controller

"""
Here you can give your input parameters. Run this class to create your solution.
Solution will be added to the 'working_dir_folder' and sent to your email.
"""

# Working directory 
working_dir_folder = "C:\Users\Eier\Github\kbe-a3\WorkingDirectory"

# Environment
env_pos = ""
env_point_A = ""
env_point_B = ""
env_length = ""
env_width = ""
env_height = ""

# Equipment 1
equ1_pos = ""
equ1_point_in = ""
equ1_point_out = ""
equ1_length = ""
equ1_width = ""
equ1_height = ""

# Equipment 2
equ2_pos = ""
equ2_point_in = ""
equ2_point_out = ""
equ2_length = ""
equ2_width = ""
equ2_height = ""

# Equipment 3
equ3_pos = ""
equ3_point_in = ""
equ3_point_out = ""
equ3_length = ""
equ3_width = ""
equ3_height = ""

# Pipe
pipe_diameter_outer = ""
pipe_diameter_inner = ""

# Email
email = ""


# ------------------------------------------------------------------------------

env_args = [env_pos, env_point_A, env_point_B, env_length, env_width, env_height]

equ1_args = [equ1_pos, equ1_point_in, equ1_point_out, equ1_length, equ1_width, equ1_height]
equ2_args = [equ2_pos, equ2_point_in, equ2_point_out, equ2_length, equ2_width, equ2_height]
equ3_args = [equ3_pos, equ3_point_in, equ3_point_out, equ3_length, equ3_width, equ3_height]

equs_args = [equ1_args, equ2_args, equ3_args]

pipe_args = [pipe_diameter_outer, pipe_diameter_inner]

Controller.construct(env_args, equs_args, pipe_args)