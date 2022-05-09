

from random import randint


class ParameterContainer():
	''' Contains parameters for premade solutions. 
		ARE YOU AN ENGINEER LOOKING TO ADD A SPECIFIC CASE? Look to the bottom of this file.'''

	def get_parameter_list(number_of_equipments_or_id):
		''' Returns all parameters needed to create a solution with the given number of equipments.
			May be random or predefined depending on what's been implemented.'''
		
		if(number_of_equipments_or_id == 2):

			randomizer = randint(0,1)
			if(randomizer == 0):
				'''TWO EQUIPMENT IN A STRAIGHT LINE'''
				## Environment
				env_pos = (0, 0, 0)
				env_point_A = (0, 5000, 5000)
				env_point_A_dir = (1,0,0)
				env_point_B = (10000, 5000, 5000)
				env_point_B_dir = (1,0,0)
				env_length = 10000
				env_width = 10000
				env_height = 10000 + randint(0, 2000)

				# Equipment 1
				equ1_pos = (2500, 4500, 4500)
				equ1_point_in = (2500, 5000, 5000)
				equ1_point_in_dir=(1,0,0)
				equ1_point_out = (3500, 5000, 5000)
				equ1_point_out_dir=(1,0,0)
				equ1_length = 1000
				equ1_width = 1000
				equ1_height = 1000 + randint(0, 2000)

				# Equipment 2
				equ2_pos = (5500, 4500, 4500)
				equ2_point_in = (5500, 5000, 5000)
				equ2_point_in_dir=(1,0,0)
				equ2_point_out = (6000, 5000, 5000)
				equ2_point_out_dir=(1,0,0)
				equ2_length = 500
				equ2_width = 1000
				equ2_height = 1000 + randint(0, 2000)

			elif(randomizer == 1):
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

			elif(randomizer == 2):
				# TWO ELEMENTS IN DIFFERENT X AND Z-COORDS.
				# Environment
				env_pos = (0, 0, 0)
				env_point_A = (0, 5000, 4500)
				env_point_A_dir = (1,0,0)
				env_point_B = (10000, 5000, 8500)
				env_point_B_dir = (1,0,0)
				env_length = 10000
				env_width = 10000
				env_height = 10000

				# Equipment 1
				equ1_pos = (1500, 4500, 4000)
				equ1_point_in = (1500, 5000, 4500)
				equ1_point_in_dir=(1,0,0)
				equ1_point_out = (2500, 5000, 4500)
				equ1_point_out_dir=(1,0,0)
				equ1_length = 1000
				equ1_width = 1000
				equ1_height = 1000

				# Equipment 2
				equ2_pos = (6000, 4500, 8000)
				equ2_point_in = (6500, 5000, 8000)
				equ2_point_in_dir=(0,0,1)
				equ2_point_out = (7000, 5000, 8500)
				equ2_point_out_dir=(1,0,0)
				equ2_length = 1000
				equ2_width = 1000
				equ2_height = 1000

			equ1_args = [equ1_pos, equ1_point_in, equ1_point_in_dir, equ1_point_out, equ1_point_out_dir, equ1_length, equ1_width, equ1_height]

			equ2_args = [equ2_pos, equ2_point_in, equ2_point_in_dir, equ2_point_out, equ2_point_out_dir, equ2_length, equ2_width, equ2_height]

			equs_args = [equ1_args, equ2_args]

		elif(number_of_equipments_or_id == 3):
			# Randomizes which parameters are given.
			randomizer = randint(0,3)

			if(randomizer == 0):
				''' THREE EQUIPMENT IN DIFFERENT X AND Z-COORDS '''
				# Environment
				env_pos = (0, 0, 0)
				env_point_A = (0, 5000, 4500)
				env_point_A_dir = (1,0,0)
				env_point_B = (8000, 5000, 0)
				env_point_B_dir = (0,0,-1)
				env_length = 10000
				env_width = 10000
				env_height = 10000

				# Equipment 1
				equ1_pos = (1500, 4500, 4000)
				equ1_point_in = (1500, 5000, 4500)
				equ1_point_in_dir=(1,0,0)
				equ1_point_out = (2500, 5000, 4500)
				equ1_point_out_dir=(1,0,0)
				equ1_length = 1000
				equ1_width = 1000
				equ1_height = 1000
				
				# Equipment 2
				equ2_pos = (6000, 4500, 8000)
				equ2_point_in = (6500, 5000, 8000)
				equ2_point_in_dir=(0,0,1)
				equ2_point_out = (7000, 5000, 8500)
				equ2_point_out_dir=(1,0,0)
				equ2_length = 1000
				equ2_width = 1000
				equ2_height = 1000

				# Equipment 3
				equ3_pos = (7500, 4500, 5500)
				equ3_point_in = (8000, 5000, 6500)
				equ3_point_in_dir=(0,0,-1)
				equ3_point_out = (8000, 5000, 5500)
				equ3_point_out_dir=(0,0,-1)
				equ3_length = 1000
				equ3_width = 1000
				equ3_height = 1000

			elif(randomizer == 1):
				# THREE ELEMENTS IN DIFFERENT X AND Z-COORDS.
				# Environment
				env_pos = (0, 0, 0)
				env_point_A = (0, 5000, 2500)
				env_point_A_dir = (1,0,0)
				env_point_B = (10000, 5000, 3500)
				env_point_B_dir = (1,0,0)
				env_length = 10000
				env_width = 10000
				env_height = 10000

				# Equipment 1
				equ1_pos = (1500, 4500, 2000)
				equ1_point_in = (1500, 5000, 2500)
				equ1_point_in_dir=(1,0,0)
				equ1_point_out = (2500, 5000, 2500)
				equ1_point_out_dir=(1,0,0)
				equ1_length = 1000
				equ1_width = 1000
				equ1_height = 1000

				# Equipment 2
				equ2_pos = (3500, 4500, 5000)
				equ2_point_in = (4000, 5000, 5000)
				equ2_point_in_dir=(0,0,1)
				equ2_point_out = (4500, 5000, 5500)
				equ2_point_out_dir=(1,0,0)
				equ2_length = 1000
				equ2_width = 1000
				equ2_height = 1000

				# Equipment 3
				equ3_pos = (7000, 4500, 3000)
				equ3_point_in = (7500, 5000, 4000)
				equ3_point_in_dir = (0,0,-1)
				equ3_point_out = (8000,5000,3500)
				equ3_point_out_dir = (1,0,0)
				equ3_length = 1000
				equ3_width = 1000
				equ3_height = 1000

			elif (randomizer==2):
				# THREE ELEMENTS IN DIFFERENT X AND Y-COORDS.
				# Environment
				env_pos = (0, 0, 0)
				env_point_A = (0, 5000, 2000)
				env_point_A_dir = (1,0,0)
				env_point_B = (10000, 5000, 2000)
				env_point_B_dir = (1,0,0)
				env_length = 10000
				env_width = 10000
				env_height = 10000

				# Equipment 1
				equ1_pos = (1500, 4500, 1500)
				equ1_point_in = (1500, 5000, 2000)
				equ1_point_in_dir=(1,0,0)
				equ1_point_out = (2000, 5500, 2000)
				equ1_point_out_dir=(0,-1,0)
				equ1_length = 1000
				equ1_width = 1000
				equ1_height = 1000

				# Equipment 2
				equ2_pos = (4500, 1500, 1500)
				equ2_point_in = (4500, 2000, 2000)
				equ2_point_in_dir=(1,0,0)
				equ2_point_out = (5500, 2000, 2000)
				equ2_point_out_dir=(1,0,0)
				equ2_length = 1000
				equ2_width = 1000
				equ2_height = 1000

				# Equipment 3
				equ3_pos = (6000, 4500, 1500)
				equ3_point_in = (6500, 4500, 2000)
				equ3_point_in_dir=(0,1,0)
				equ3_point_out = (7000, 5000, 2000)
				equ3_point_out_dir=(1,0,0)
				equ3_length = 1000
				equ3_width = 1000
				equ3_height = 1000
			
			elif (randomizer==3):
				# THREE ELEMENTS IN DIFFERENT X AND Y-COORDS.
				# Environment
				env_pos = (0, 0, 0)
				env_point_A = (0, 5000, 2000)
				env_point_A_dir = (1,0,0)
				env_point_B = (10000, 5000, 2000)
				env_point_B_dir = (1,0,0)
				env_length = 10000
				env_width = 10000
				env_height = 10000

				# Equipment 1
				equ1_pos = (1500, 4500, 1500)
				equ1_point_in = (1500, 5000, 2000)
				equ1_point_in_dir=(1,0,0)
				equ1_point_out = (2000, 5500, 2000)
				equ1_point_out_dir=(0,-1,0)
				equ1_length = 1000
				equ1_width = 1000
				equ1_height = 1000

				# Equipment 2
				equ2_pos = (3000, 7500, 1500)
				equ2_point_in = (3000, 8000, 2000)
				equ2_point_in_dir=(1,0,0)
				equ2_point_out = (4000, 8000, 2000)
				equ2_point_out_dir=(1,0,0)
				equ2_length = 1000
				equ2_width = 1000
				equ2_height = 1000

				# Equipment 3
				equ3_pos = (6000, 4500, 1500)
				equ3_point_in = (6500, 4500, 2000)
				equ3_point_in_dir=(0,1,0)
				equ3_point_out = (7000, 5000, 2000)
				equ3_point_out_dir=(1,0,0)
				equ3_length = 1000
				equ3_width = 1000
				equ3_height = 1000
			

			equ1_args = [equ1_pos, equ1_point_in, equ1_point_in_dir, equ1_point_out, equ1_point_out_dir, equ1_length, equ1_width, equ1_height]
			equ2_args = [equ2_pos, equ2_point_in, equ2_point_in_dir, equ2_point_out, equ2_point_out_dir, equ2_length, equ2_width, equ2_height]
			equ3_args = [equ3_pos, equ3_point_in, equ3_point_in_dir, equ3_point_out, equ3_point_out_dir, equ3_length, equ3_width, equ3_height]
			equs_args = [equ1_args, equ2_args, equ3_args]

		elif(number_of_equipments_or_id == 4):
			# FOUR ELEMENTS IN DIFFERENT X AND Z-COORDS.
			# Environment
			env_pos = (0, 0, 0)
			env_point_A = (0, 5000, 2500)
			env_point_A_dir = (1,0,0)
			env_point_B = (12000, 5000, 1500)
			env_point_B_dir = (1,0,0)
			env_length = 12000
			env_width = 10000
			env_height = 10000

			# Equipment 1
			equ1_pos = (1500, 4500, 2000)
			equ1_point_in = (1500, 5000, 2500)
			equ1_point_in_dir=(1,0,0)
			equ1_point_out = (2500, 5000, 2500)
			equ1_point_out_dir=(1,0,0)
			equ1_length = 1000
			equ1_width = 1000
			equ1_height = 1000

			# Equipment 2
			equ2_pos = (3500, 4500, 5000)
			equ2_point_in = (4000, 5000, 5000)
			equ2_point_in_dir=(0,0,1)
			equ2_point_out = (4500, 5000, 5500)
			equ2_point_out_dir=(1,0,0)
			equ2_length = 1000
			equ2_width = 1000
			equ2_height = 1000

			# Equipment 3
			equ3_pos = (7000, 4500, 3000)
			equ3_point_in = (7500, 5000, 4000)
			equ3_point_in_dir = (0,0,-1)
			equ3_point_out = (8000,5000,3500)
			equ3_point_out_dir = (1,0,0)
			equ3_length = 1000
			equ3_width = 1000
			equ3_height = 1000

			# Equipment 4
			equ4_pos = (9000, 4500, 1000)
			equ4_point_in = (9500, 5000, 2000)
			equ4_point_in_dir = (0,0,-1)
			equ4_point_out = (10000, 5000, 1500)
			equ4_point_out_dir = (1,0,0)
			equ4_length = 1000
			equ4_width = 1000
			equ4_height = 1000

			equ1_args = [equ1_pos, equ1_point_in, equ1_point_in_dir, equ1_point_out, equ1_point_out_dir, equ1_length, equ1_width, equ1_height]
			equ2_args = [equ2_pos, equ2_point_in, equ2_point_in_dir, equ2_point_out, equ2_point_out_dir, equ2_length, equ2_width, equ2_height]
			equ3_args = [equ3_pos, equ3_point_in, equ3_point_in_dir, equ3_point_out, equ3_point_out_dir, equ3_length, equ3_width, equ3_height]
			equ4_args = [equ4_pos, equ4_point_in, equ4_point_in_dir, equ4_point_out, equ4_point_out_dir, equ4_length, equ4_width, equ4_height]
			
			equs_args = [equ1_args, equ2_args, equ3_args, equ4_args]

		elif(number_of_equipments_or_id == 10):
			# Environment
			env_pos = (0, 0, 0)
			env_point_A = (0, 1000, 1000)
			env_point_A_dir = (1,0,0)
			env_point_B = (13500, 10000, 3000) 
			env_point_B_dir = (0,1,0)
			env_length = 15000
			env_width = 10000
			env_height = 10000

			# Equipment 1
			equ1_pos = (1000, 500, 500)
			equ1_point_in = (1000, 1000, 1000)
			equ1_point_in_dir=(1,0,0)
			equ1_point_out = (2000, 1000, 1000)
			equ1_point_out_dir=(1,0,0)
			equ1_length = 1000
			equ1_width = 1000
			equ1_height = 1000

			# Equipment 2
			equ2_pos = (3000, 500, 3000)
			equ2_point_in = (3500, 1000, 3000)
			equ2_point_in_dir=(0,0,1)
			equ2_point_out = (4000, 1000, 3500)
			equ2_point_out_dir=(1,0,0)
			equ2_length = 1000
			equ2_width = 1000
			equ2_height = 1000

			# Equipment 3
			equ3_pos = (5000, 500, 4000)
			equ3_point_in = (5500, 1000, 4000)
			equ3_point_in_dir = (0,0,1)
			equ3_point_out = (5500,1500,4500)
			equ3_point_out_dir = (0,1,0)
			equ3_length = 1000
			equ3_width = 1000
			equ3_height = 1000

			# Equipment 4
			equ4_pos = (8000, 2000, 4000)
			equ4_point_in = (8000, 2500, 4500)
			equ4_point_in_dir = (1,0,0)
			equ4_point_out = (8500, 2500, 4000)
			equ4_point_out_dir = (0,0,-1)
			equ4_length = 1000
			equ4_width = 1000
			equ4_height = 1000

			# Equipment 5
			equ5_pos = (8000, 2000, 2500)
			equ5_point_in = (8500, 2500, 3500)
			equ5_point_in_dir = (0,0,-1)
			equ5_point_out = (8500, 3000, 3000)
			equ5_point_out_dir = (0,1,0)
			equ5_length = 1000
			equ5_width = 1000
			equ5_height = 1000

			# Equipment 6
			equ6_pos = (1000, 3000, 2500) 
			equ6_point_in = (2000, 3500, 3000)
			equ6_point_in_dir = (-1,0,0)
			equ6_point_out = (1500, 4000, 3000)
			equ6_point_out_dir = (0,1,0)
			equ6_length = 1000
			equ6_width = 1000
			equ6_height = 1000

			# Equipment 7
			equ7_pos = (1000, 6000, 2500)
			equ7_point_in = (1500, 6000, 3000)
			equ7_point_in_dir = (0,1,0)
			equ7_point_out = (2000, 6500, 3000)
			equ7_point_out_dir = (1,0,0)
			equ7_length = 1000
			equ7_width = 1000
			equ7_height = 1000

			# Equipment 8
			equ8_pos = (5000, 6000, 6500)
			equ8_point_in = (5500, 6500, 6500)
			equ8_point_in_dir = (0,0,1)
			equ8_point_out = (6000, 6500, 7000)
			equ8_point_out_dir = (1,0,0)
			equ8_length = 1000
			equ8_width = 1000
			equ8_height = 1000

			# Equipment 9
			equ9_pos = (9000, 4000, 6500)
			equ9_point_in = (9500, 5000, 7000)
			equ9_point_in_dir = (0,-1,0)
			equ9_point_out = (10000, 4500, 7000)
			equ9_point_out_dir = (1,0,0)
			equ9_length = 1000
			equ9_width = 1000
			equ9_height = 1000

			# Equipment 10
			equ10_pos = (13000, 4000, 2500)
			equ10_point_in = (13500, 4500, 3500)
			equ10_point_in_dir = (0,0,-1)
			equ10_point_out = (13500, 5000, 3000)
			equ10_point_out_dir = (0,1,0)
			equ10_length = 1000
			equ10_width = 1000
			equ10_height = 1000

			equ1_args = [equ1_pos, equ1_point_in, equ1_point_in_dir, equ1_point_out, equ1_point_out_dir, equ1_length, equ1_width, equ1_height]
			equ2_args = [equ2_pos, equ2_point_in, equ2_point_in_dir, equ2_point_out, equ2_point_out_dir, equ2_length, equ2_width, equ2_height]
			equ3_args = [equ3_pos, equ3_point_in, equ3_point_in_dir, equ3_point_out, equ3_point_out_dir, equ3_length, equ3_width, equ3_height]
			equ4_args = [equ4_pos, equ4_point_in, equ4_point_in_dir, equ4_point_out, equ4_point_out_dir, equ4_length, equ4_width, equ4_height]
			equ5_args = [equ5_pos, equ5_point_in, equ5_point_in_dir, equ5_point_out, equ5_point_out_dir, equ5_length, equ5_width, equ5_height]
			equ6_args = [equ6_pos, equ6_point_in, equ6_point_in_dir, equ6_point_out, equ6_point_out_dir, equ6_length, equ6_width, equ6_height]
			equ7_args = [equ7_pos, equ7_point_in, equ7_point_in_dir, equ7_point_out, equ7_point_out_dir, equ7_length, equ7_width, equ7_height]
			equ8_args = [equ8_pos, equ8_point_in, equ8_point_in_dir, equ8_point_out, equ8_point_out_dir, equ8_length, equ8_width, equ8_height]
			equ9_args = [equ9_pos, equ9_point_in, equ9_point_in_dir, equ9_point_out, equ9_point_out_dir, equ9_length, equ9_width, equ9_height]
			equ10_args = [equ10_pos, equ10_point_in, equ10_point_in_dir, equ10_point_out, equ10_point_out_dir, equ10_length, equ10_width, equ10_height]

			equs_args = [equ1_args, equ2_args, equ3_args, equ4_args, equ5_args, equ6_args, equ7_args, equ8_args, equ9_args, equ10_args]

		else:
			raise ValueError(f"Solution not created for {number_of_equipments_or_id} equipments or ID not found.")

		# Pipe
		pipe_diameter_outer = 200
		pipe_diameter_inner = 150
		elbow_radius = 90

		env_args = [env_pos, env_point_A, env_point_A_dir, env_point_B, env_point_B_dir, env_length, env_width, env_height]
		pipe_args = [pipe_diameter_outer, pipe_diameter_inner, elbow_radius]
		
		return env_args, equs_args, pipe_args


		''' ARE YOU AN ENGINEER LOOKING TO ADD A SPECIFIC CASE? 
			Modify the template below, and insert your elif above the else statement above.'''
		# elif(number_of_equipments_or_id == Your_ID_as_a_3-digit_int):
		# 	# Environment, this must be in 1st quadrant! (positive values for env_pos coordinates)
		# 	env_pos = (, , )
		# 	env_point_A = (, , )
		# 	env_point_A_dir = ( , , )
		# 	env_point_B = ( , , )
		# 	env_point_B_dir = ( , , )
		# 	env_length = 
		# 	env_width = 
		# 	env_height = 

		# 	# Equipment x (replace x with 1, 2, 3, 4 etc as you add more equipment)
		# 	equx_pos = (, , )
		# 	equx_point_in = (, , )
		# 	equx_point_in_dir=( , , )
		# 	equx_point_out = (, , )
		# 	equx_point_out_dir=( , , )
		# 	equx_length = 
		# 	equx_width = 
		# 	equx_height = 

		# 	equx_args = [equx_pos, equx_point_in, equx_point_in_dir, equx_point_out, equx_point_out_dir, equx_length, equx_width, equx_height]

		# 	equs_args = [equx_args]

		# pipe_diameter_outer = 
		# pipe_diameter_inner = 
		# elbow_radius = 
