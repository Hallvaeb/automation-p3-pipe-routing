

from model.Environment import Environment
from model.Equipment import Equipment
from model.PathGenerator import PathGenerator
from model.Pipe import Pipe
from controller.IDGenerator import IDGenerator
import pathlib


path_to_dfa_folder = str(pathlib.Path().absolute().as_posix())+"/DFAs/"

class DFABuilder():


	def generate_dfa(env, equs, pipe, complete_paths):
		""" Generates the DFA file. 
		Input: Environment, List<Equipment>, Pipe, List<List<tuples/point>>. """
		DFABuilder.append_pipe_to_DFA(pipe)
		DFABuilder.append_env_to_DFA(env)
		for equ in equs:
			DFABuilder.append_equ_to_DFA(equ)
		
		for path in complete_paths:
			DFABuilder.append_path_to_DFA(path)
		DFABuilder.sweep_paths()
			
	def append_env_to_DFA(env):
		""" Append environment to the current DFA file """
		# TODO: implement
		pass

	def append_equ_to_DFA(equs):
		""" Append equ to the current DFA file """
		# TODO: implement
		pass

	def append_pipe_to_DFA(pipe):
		""" Append pipe to the current DFA file """
		design_id = IDGenerator.create_design_ID()
		f = open(path_to_dfa_folder + "templates/PipeSystem.dfa", "r")
		txt = f.read()
		txt = txt.replace("<ID>", design_id)
		f.close()
		f = open(path_to_dfa_folder + "products/" + design_id + ".dfa", "w")
		f.write(txt)
		f.close

		f1 = open(path_to_dfa_folder + "templates/Pipe.dfa", "r")
		txt1 = f1.read()
		txt1 = txt1.replace("<CURVE_RADIUS>", pipe.elbow_curve_radius)
		txt1 = txt1.replace("<OUTER_RADIUS>", pipe.diameter_outer)
		txt1 = txt1.replace("<INNER_RADIUS>", pipe.diameter_inner)
		f1.close()

		f1 = open(path_to_dfa_folder + "products/" + design_id + ".dfa", "a")
		f1.write(txt1)
		f1.close
		return design_id




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

p1 = Pipe(25, 20, 90)
DFABuilder.append_pipe_to_DFA(p1)