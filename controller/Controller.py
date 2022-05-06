

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
			point_A_dir=env_args[2], 
			point_B = env_args[3], 
			point_B_dir= env_args[4], 
			length = env_args[5], 
			width = env_args[6], 
			height = env_args[7])
		
		# Equipment
		equs = []
		for equ_args in equs_args:
			equs.append(Equipment(
				position = equ_args[0], 
				point_in = equ_args[1], 
				point_in_dir=equ_args[2], 
				point_out = equ_args[3], 
				point_out_dir = equ_args[4], 
				length = equ_args[5], 
				width = equ_args[6], 
				height = equ_args[7]))
			
		# Pipe
		pipe = Pipe(
			diameter_outer = pipe_args[0], 
			diameter_inner = pipe_args[1], 
			elbow_radius = pipe_args[2])

		# Create paths
		path_gen = PathGenerator(env, equs, pipe)
		# all_paths = path_gen.all_paths
		path_objects = path_gen.path_objects

		# Create DFA
		design_id = DFABuilder.generate_dfa(env, equs, pipe, path_objects)

		# Send email
		EmailHandler.send_design_to_email(design_id, email)

		print(f"DFA file created and sent to email. \nDesignID: {design_id} \nEmail: {email}")
