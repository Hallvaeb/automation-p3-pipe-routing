

from model.Environment import Environment
from model.Equipment import Equipment
from model.Pipe import Pipe


class DFABuilder():


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

	def generate_dfa(objects):
		for obj in objects:
			if isinstance(obj, Environment):
				DFABuilder.append_env_to_DFA(obj)

			elif isinstance(obj, Equipment):
				DFABuilder.append_equ_to_DFA(obj)

			elif isinstance(obj, Pipe):
				DFABuilder.append_pipe_to_DFA(obj)
			else:
				print("object isinstance didnt recognice obj as env, equ, or pipe")	
			