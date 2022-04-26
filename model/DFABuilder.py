

from model.Environment import Environment
from model.Equipment import Equipment
from model.PathGenerator import PathGenerator
from model.Pipe import Pipe


class DFABuilder():


	def generate_dfa(objects):
		""" Generates the DFA file. objects should be Environment, Equipment, Pipe or PathGenerator instances. """
		for obj in objects:
			if isinstance(obj, Environment):
				DFABuilder.append_env_to_DFA(obj)

			elif isinstance(obj, Equipment):
				DFABuilder.append_equ_to_DFA(obj)

			elif isinstance(obj, Pipe):
				DFABuilder.append_pipe_to_DFA(obj)
			elif isinstance(obj, PathGenerator):
				for path in obj.paths:
					DFABuilder.append_path_to_DFA(path)
			else:
				print("generate_dfa() in DFABuilder didnt recognice obj as env, equ, or pipe")	
		
		DFABuilder.sweep_paths()
			
	def append_env_to_DFA(obj):
		""" Append environment to the current DFA file """
		# TODO: implement
		pass

	def append_equ_to_DFA(obj):
		""" Append environment to the current DFA file """
		# TODO: implement
		pass

	def append_pipe_to_DFA(obj):
		""" Append environment to the current DFA file """
		# TODO: implement
		pass

	def append_path_to_DFA(path):
		""" Append path to the current DFA file """
		# TODO: implement
		pass

	def sweep_paths():
		""" Sweeps on the paths to make the pipes """
		# TODO: implement
		pass