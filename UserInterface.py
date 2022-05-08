from controller.Controller import Controller

"""
Here you can give your input parameters. Run this class to create your solution.
Solution will be added to the 'working_dir_folder' and sent to your email.
"""

# INPUT BEGIN ------------------------------------------------------------------

# #TWO ELEMENTS IN A STRAIGHT LINE
# # Environment
# env_pos = (0, 0, 0)
# env_point_A = (0, 5000, 5000)
# env_point_A_dir = (1,0,0)
# env_point_B = (10000, 5000, 5000)
# env_point_B_dir = (1,0,0)
# env_length = 10000
# env_width = 10000
# env_height = 10000

# # Equipment 1
# equ1_pos = (2500, 4500, 4500)
# equ1_point_in = (2500, 5000, 5000)
# equ1_point_in_dir=(1,0,0)
# equ1_point_out = (3500, 5000, 5000)
# equ1_point_out_dir=(1,0,0)
# equ1_length = 1000
# equ1_width = 1000
# equ1_height = 1000

# # Equipment 2
# equ2_pos = (5500, 4500, 4500)
# equ2_point_in = (5500, 5000, 5000)
# equ2_point_in_dir=(1,0,0)
# equ2_point_out = (6000, 5000, 5000)
# equ2_point_out_dir=(1,0,0)
# equ2_length = 500
# equ2_width = 1000
# equ2_height = 1000

# TWO ELEMENTS IN DIFFERENT X AND Z-COORDS.
# Environment
env_pos = (0, 0, 0)
env_point_A = (500, 5000, 0)
env_point_A_dir = (0,0,1)
env_point_B = (10000, 5000, 3500)
env_point_B_dir = (1,0,0)
env_length = 10000
env_width = 10000
env_height = 10000

# Equipment 1
equ1_pos = (2500, 4500, 5500)
equ1_point_in = (2500, 5000, 6000)
equ1_point_in_dir=(1,0,0)
equ1_point_out = (3000, 5000, 5500)
equ1_point_out_dir=(0,0,-1)
equ1_length = 1000
equ1_width = 1000
equ1_height = 1000

# Equipment 2
equ2_pos = (6000, 4500, 3000)
equ2_point_in = (6000, 5000, 3500)
equ2_point_in_dir=(1,0,0)
equ2_point_out = (7000, 5000, 3500)
equ2_point_out_dir=(1,0,0)
equ2_length = 1000
equ2_width = 1000
equ2_height = 1000

# TWO ELEMENTS IN DIFFERENT X AND Z-COORDS.
# # Environment
# env_pos = (0, 0, 0)
# env_point_A = (0, 5000, 4500)
# env_point_A_dir = (1,0,0)
# env_point_B = (10000, 5000, 8500)
# env_point_B_dir = (1,0,0)
# env_length = 10000
# env_width = 10000
# env_height = 10000

# # Equipment 1
# equ1_pos = (1500, 4500, 4000)
# equ1_point_in = (1500, 5000, 4500)
# equ1_point_in_dir=(1,0,0)
# equ1_point_out = (2500, 5000, 4500)
# equ1_point_out_dir=(1,0,0)
# equ1_length = 1000
# equ1_width = 1000
# equ1_height = 1000

# # Equipment 2
# equ2_pos = (6000, 4500, 8000)
# equ2_point_in = (6500, 5000, 8000)
# equ2_point_in_dir=(0,0,1)
# equ2_point_out = (7000, 5000, 8500)
# equ2_point_out_dir=(1,0,0)
# equ2_length = 1000
# equ2_width = 1000
# equ2_height = 1000

# # THREE ELEMENTS IN DIFFERENT X AND Z-COORDS.
# # Environment
# env_pos = (0, 0, 0)
# env_point_A = (0, 5000, 2500)
# env_point_A_dir = (1,0,0)
# env_point_B = (10000, 5000, 3500)
# env_point_B_dir = (1,0,0)
# env_length = 10000
# env_width = 10000
# env_height = 10000

# # Equipment 1
# equ1_pos = (1500, 4500, 2000)
# equ1_point_in = (1500, 5000, 2500)
# equ1_point_in_dir=(1,0,0)
# equ1_point_out = (2500, 5000, 2500)
# equ1_point_out_dir=(1,0,0)
# equ1_length = 1000
# equ1_width = 1000
# equ1_height = 1000

# # Equipment 2
# equ2_pos = (3500, 4500, 5000)
# equ2_point_in = (4000, 5000, 5000)
# equ2_point_in_dir=(0,0,1)
# equ2_point_out = (4500, 5000, 5500)
# equ2_point_out_dir=(1,0,0)
# equ2_length = 1000
# equ2_width = 1000
# equ2_height = 1000

# # Equipment 3
# equ3_pos = (7000, 4500, 3000)
# equ3_point_in = (7500, 5000, 4000)
# equ3_point_in_dir = (0,0,-1)
# equ3_point_out = (8000,5000,3500)
# equ3_point_out_dir = (1,0,0)
# equ3_length = 1000
# equ3_width = 1000
# equ3_height = 1000


# # FOUR ELEMENTS IN DIFFERENT X AND Z-COORDS.
# # Environment
# env_pos = (0, 0, 0)
# env_point_A = (0, 5000, 2500)
# env_point_A_dir = (1,0,0)
# env_point_B = (12000, 5000, 1500)
# env_point_B_dir = (1,0,0)
# env_length = 12000
# env_width = 10000
# env_height = 10000

# # Equipment 1
# equ1_pos = (1500, 4500, 2000)
# equ1_point_in = (1500, 5000, 2500)
# equ1_point_in_dir=(1,0,0)
# equ1_point_out = (2500, 5000, 2500)
# equ1_point_out_dir=(1,0,0)
# equ1_length = 1000
# equ1_width = 1000
# equ1_height = 1000

# # Equipment 2
# equ2_pos = (3500, 4500, 5000)
# equ2_point_in = (4000, 5000, 5000)
# equ2_point_in_dir=(0,0,1)
# equ2_point_out = (4500, 5000, 5500)
# equ2_point_out_dir=(1,0,0)
# equ2_length = 1000
# equ2_width = 1000
# equ2_height = 1000

# # Equipment 3
# equ3_pos = (7000, 4500, 3000)
# equ3_point_in = (7500, 5000, 4000)
# equ3_point_in_dir = (0,0,-1)
# equ3_point_out = (8000,5000,3500)
# equ3_point_out_dir = (1,0,0)
# equ3_length = 1000
# equ3_width = 1000
# equ3_height = 1000

# # Equipment 4
# equ4_pos = (9000, 4500, 1000)
# equ4_point_in = (9500, 5000, 2000)
# equ4_point_in_dir = (0,0,-1)
# equ4_point_out = (10000, 5000, 1500)
# equ4_point_out_dir = (1,0,0)
# equ4_length = 1000
# equ4_width = 1000
# equ4_height = 1000

# Pipe
pipe_diameter_outer = 200
pipe_diameter_inner = 150
elbow_radius = 90

# Email
email = "email@gmail.com"


# INPUT END --------------------------------------------------------------------

env_args = [env_pos, env_point_A, env_point_A_dir, env_point_B, env_point_B_dir, env_length, env_width, env_height]

equ1_args = [equ1_pos, equ1_point_in, equ1_point_in_dir, equ1_point_out, equ1_point_out_dir, equ1_length, equ1_width, equ1_height]
equ2_args = [equ2_pos, equ2_point_in, equ2_point_in_dir, equ2_point_out, equ2_point_out_dir, equ2_length, equ2_width, equ2_height]
# equ3_args = [equ3_pos, equ3_point_in, equ3_point_in_dir, equ3_point_out, equ3_point_out_dir, equ3_length, equ3_width, equ3_height]
# equ4_args = [equ4_pos, equ4_point_in, equ4_point_in_dir, equ4_point_out, equ4_point_out_dir, equ4_length, equ4_width, equ4_height]
equs_args = [equ1_args, equ2_args] #equ3_args, equ4_args

pipe_args = [pipe_diameter_outer, pipe_diameter_inner, elbow_radius]

Controller.construct(env_args, equs_args, pipe_args, email)