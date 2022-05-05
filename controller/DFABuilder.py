

from itertools import product
from model.Environment import Environment
from model.Equipment import Equipment
from controller.PathGenerator import PathGenerator
from model.Pipe import Pipe
from controller.IDGenerator import IDGenerator
import pathlib

path_to_dfa_folder = str(pathlib.Path().absolute().as_posix())+"/DFAs/"


class DFABuilder():


	def generate_dfa(env, equs, pipe, path_objects):
		""" Generates the DFA file. 
		Input: Environment, List<Equipment>, Pipe, List<List<tuples/point>>. """
		design_id = DFABuilder.append_pipe_system_to_DFA(pipe)
		DFABuilder.append_env_to_DFA(env, design_id)
		DFABuilder.append_equ_to_DFA(equs, design_id)
		
		elements_in_path = []
		for path in path_objects:
			path_list = path.complete_path
			elements_in_path = DFABuilder.append_path_to_DFA(path_list, design_id)
			DFABuilder.sweep_elements(elements_in_path, design_id, path)
		return design_id
			
	def append_env_to_DFA(env, design_id):
		""" Append environment to the current DFA file """
		env_ID = IDGenerator.create_dfa_element_ID("environment")
		f = open(path_to_dfa_folder + "templates/Environment.dfa", "r")
		txt = f.read()
		txt = txt.replace("<ENV_ID>", env_ID)
		txt = txt.replace("<HEIGHT>", str(env.height))
		txt = txt.replace("<WIDTH>", str(env.width))
		txt = txt.replace("<LENGTH>", str(env.length))
		f.close()

		f = open(path_to_dfa_folder + "products/" + design_id + ".dfa", "a")
		f.write(txt)
		f.close
		return design_id

	def append_equ_to_DFA(equs, design_id):
		""" Append equ to the current DFA file """
		for equ in equs:
			equ_ID = IDGenerator.create_dfa_element_ID("equipment")
			f = open(path_to_dfa_folder + "templates/Equipment.dfa", "r")
			txt = f.read()
			txt = txt.replace("<EQU_ID>", equ_ID)
			txt = txt.replace("<X_POS>", str(equ.position[0]))
			txt = txt.replace("<Y_POS>", str(equ.position[1]))
			txt = txt.replace("<Z_POS>", str(equ.position[2]))
			txt = txt.replace("<HEIGHT>", str(equ.height))
			txt = txt.replace("<WIDTH>", str(equ.width))
			txt = txt.replace("<LENGTH>", str(equ.length))
			f.close()

			f = open(path_to_dfa_folder + "products/" + design_id + ".dfa", "a")
			f.write(txt)
			f.close
			return design_id

	def append_pipe_system_to_DFA(pipe):
		""" Append pipe to the current DFA file """
		design_id = IDGenerator.create_design_ID()
		f = open(path_to_dfa_folder + "templates/PipeSystem.dfa", "r")
		txt = f.read()
		txt = txt.replace("<ID>", design_id)
		txt = txt.replace("<CURVE_RADIUS>", str(pipe.elbow_curve_radius))
		txt = txt.replace("<OUTER_RADIUS>", str(pipe.diameter_outer))
		txt = txt.replace("<INNER_RADIUS>", str(pipe.diameter_inner))
		f.close()

		f = open(path_to_dfa_folder + "products/" + design_id + ".dfa", "w")
		f.write(txt)
		f.close

		return design_id




	def append_path_to_DFA(path, design_id):  #[[(2,0,0), (2,0,8)] , [(92,0,8), (1,0,0), (0,1,0)]]
		""" Append path to the current DFA file """
		paths_to_sweep = []
#-------------------------- ARCS ---------------------------------------------
		for elem in path:
			if len(elem) == 3:
				elbow = []
				elbow.append(elem)
				for elb in elbow:
					elb_ID = IDGenerator.create_dfa_element_ID("elbow")
					f = open(path_to_dfa_folder + "templates/Elbow.dfa", "r")
					txt = f.read()
					txt = txt.replace("<CURVE>", elb_ID)
					txt = txt.replace("<CENTER>", str(elb[0]))
					txt = txt.replace("<X_ARC_VECTOR>", str(elb[1]))
					txt = txt.replace("<Y_ARC_VECTOR>", str(elb[2]))
					f.close()

					f = open(path_to_dfa_folder + "products/" + design_id + ".dfa", "a") #design_ID is created in append_pipe_to_DFA and returned. need to fetch it form there.
					f.write(txt)
					f.close
					paths_to_sweep.append(elb_ID)

#-------------------------- LINES -----------------------------------------------
			if len(elem) == 2:
				straights = []
				straights.append(elem)
				for st in straights:
					str_ID = IDGenerator.create_dfa_element_ID("straigth")
					f = open(path_to_dfa_folder + "templates/Straight.dfa", "r")
					txt = f.read()
					txt = txt.replace("<START_POINT>", str(st[0]))
					txt = txt.replace("<END_POINT>", str(st[1]))
					txt = txt.replace("<LINE>", str_ID)
					f.close()

					f = open(path_to_dfa_folder + "products/" + design_id + ".dfa", "a") #design_ID is created in append_pipe_to_DFA and returned. need to fetch it form there.
					f.write(txt)
					f.close
					paths_to_sweep.append(str_ID)
		print("paths_to_sweep", paths_to_sweep )
		return paths_to_sweep

					

	def sweep_elements(elements_in_path, design_id, path):
		""" Sweeps on the paths to make the pipes """
		path_element_string_names = ''
		for e in elements_in_path:
			print(e)
			path_element_string_names += e + ':, '
		path_element_string_names = path_element_string_names[:-2]
		print("path", path_element_string_names)
		f = open(path_to_dfa_folder + "templates/Sweep.dfa", "r")
		txt = f.read()
		txt = txt.replace("<PIPE_PATH>", path_element_string_names) #"(0, 5000, 5000)"
		txt = txt.replace("<PROFILE_CENTER>", str(path.end_points[0])) #TODO: oppdater med rett punkt
		f.close()

		f = open(path_to_dfa_folder + "products/" + design_id + ".dfa", "a")
		f.write(txt)
		f.close()
		

