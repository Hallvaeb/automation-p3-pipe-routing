

from model.Environment import Environment
from model.Equipment import Equipment
from model.PathGenerator import PathGenerator
from model.Pipe import Pipe


class DFABuilder():


	def generate_dfa(env, equs, pipe, complete_paths):
		""" Generates the DFA file. 
		Input: Environment, List<Equipment>, Pipe, List<List<tuples/point>>. """
		DFABuilder.append_env_to_DFA(env)
		for equ in equs:
			DFABuilder.append_equ_to_DFA(equ)
		DFABuilder.append_pipe_to_DFA(pipe)
		for path in complete_paths:
			DFABuilder.append_path_to_DFA(path)
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