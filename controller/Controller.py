

from controller.DFABuilder import DFABuilder
from controller.PathGenerator import PathGenerator
from controller.EmailHandler import EmailHandler
from model.Pipe import Pipe
from model.Environment import Environment
from model.Equipment import Equipment


class Controller: 
	

	def construct(env_args, equs_args, pipe_args, email):
		""" Makes neccessary calls to carry out the users commands. This class contains little logic. """

		# Environment
		env = Environment(
			position = env_args[0], 
			point_A = env_args[1], 
			point_A_dir=(1, 0, 0), 
			point_B = env_args[2], 
			point_B_dir= (1, 0, 0), 
			length = env_args[3], 
			width = env_args[4], 
			height = env_args[5])
		
		# Equipment
		equs = []
		for equ_args in equs_args:
			equs.append(Equipment(
				position = equ_args[0], 
				point_in = equ_args[1], 
				point_in_dir=(1,0,0), 
				point_out = equ_args[2], 
				point_out_dir = (1,0, 0), 
				length = equ_args[3], 
				width = equ_args[4], 
				height = equ_args[5]))
			
		# Pipe
		pipe = Pipe(
			diameter_outer = pipe_args[0], 
			diameter_inner = pipe_args[1], 
			elbow_curve_radius = pipe_args[2])

		# Create paths
		path_gen = PathGenerator(env, equs, pipe)
		all_paths = path_gen.all_paths


		# Create DFA
		design_id = DFABuilder.generate_dfa(env, equs, pipe, all_paths)

		# Send email
		EmailHandler.send_design_to_email(design_id, email)
