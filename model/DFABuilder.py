

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
#-------------------------- ARCS ---------------------------------------------
		for el in path:
			if len(el) == 3:
				elbow = []
				elbow.append(el)
				for elb in straights:
					f = open("templates/Arc.dfa", "r")
					txt = f.read()
					txt = txt.replace("CENTER", elb[0])
					txt = txt.replace("X_ARC_VECTOR", elb[1])
					txt = txt.replace("Y_ARC_VECTOR", elb[2])
					pass

#-------------------------- LINES -----------------------------------------------
		for el in path:
			if len(el) == 2:
				straights = []
				straights.append(el)
				for st in straights:
					f = open("templates/Line.dfa", "r")
					txt = f.read()
					txt = txt.replace("START_POINT", st[0])
					txt = txt.replace("END_POINTT", st[1])
					pass

	def sweep_paths():
		""" Sweeps on the paths to make the pipes """
		# TODO: implement
		pass