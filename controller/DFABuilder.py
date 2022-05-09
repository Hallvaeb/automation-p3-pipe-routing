

from os import path
import os
from controller.IDGenerator import IDGenerator
import pathlib
path_to_inputOutput_folder = str(pathlib.Path().absolute().as_posix())+"/inputOutput/"


class DFABuilder():

	if(not path.exists(path_to_inputOutput_folder+ "products/")):
		os.mkdir(path_to_inputOutput_folder+ "products/")

	def generate_dfa(env, equs, pipe, path_objects):
		""" Generates the DFA file. 
		Input: Environment, List<Equipment>, Pipe, List<List<tuples/point>>. """
		design_id = DFABuilder.append_pipe_system_to_DFA(pipe)
		DFABuilder.append_env_to_DFA(env, design_id)
		DFABuilder.append_equ_to_DFA(equs, design_id)
		for path in path_objects:	
			elements_in_path = DFABuilder.append_path_to_DFA(path, design_id) 
			DFABuilder.sweep_elements(elements_in_path, design_id, path)
		return design_id
			
	def append_env_to_DFA(env, design_id):
		""" Append environment to the current DFA file """
		env_ID = IDGenerator.create_dfa_element_ID("environment")
		f = open(path_to_inputOutput_folder + "templates/Environment.dfa", "r")
		txt = f.read()
		txt = txt.replace("<ENV_ID>", env_ID)
		txt = txt.replace("<HEIGHT>", str(env.height))
		txt = txt.replace("<WIDTH>", str(env.width))
		txt = txt.replace("<LENGTH>", str(env.length))
		f.close()
		f = open(path_to_inputOutput_folder + "products/" + design_id + ".dfa", "a")
		f.write(txt)
		f.close
		
	def append_equ_to_DFA(equs, design_id):
		""" Append equ to the current DFA file """
		for equ in equs:
			equ_ID = IDGenerator.create_dfa_element_ID("equipment")
			f = open(path_to_inputOutput_folder + "templates/Equipment.dfa", "r")
			txt = f.read()
			txt = txt.replace("<EQU_ID>", equ_ID)
			txt = txt.replace("<X_POS>", str(equ.position[0]))
			txt = txt.replace("<Y_POS>", str(equ.position[1]))
			txt = txt.replace("<Z_POS>", str(equ.position[2]))
			txt = txt.replace("<HEIGHT>", str(equ.height))
			txt = txt.replace("<WIDTH>", str(equ.width))
			txt = txt.replace("<LENGTH>", str(equ.length))
			f.close()
			f = open(path_to_inputOutput_folder + "products/" + design_id + ".dfa", "a")
			f.write(txt)
			f.close

	def append_pipe_system_to_DFA(pipe):
		""" Append pipe to the current DFA file """
		design_id = IDGenerator.create_design_ID()
		f = open(path_to_inputOutput_folder + "templates/PipeSystem.dfa", "r")
		txt = f.read()
		txt = txt.replace("<ID>", design_id)
		txt = txt.replace("<CURVE_RADIUS>", str(pipe.elbow_radius))
		txt = txt.replace("<OUTER_RADIUS>", str(pipe.diameter_outer))
		txt = txt.replace("<INNER_RADIUS>", str(pipe.diameter_inner))
		f.close()
		f = open(path_to_inputOutput_folder + "products/" + design_id + ".dfa", "w")
		f.write(txt)
		f.close
		return design_id

	def append_path_to_DFA(path, design_id):  
		""" Append path to the current DFA file 
			Exampple path: [[(2,0,0), (2,0,8)] , [(92,0,8), (1,0,0), (0,1,0)]]"""
		paths_to_sweep = []
		for pipe_e in path.pipe_elements:
			if(pipe_e.type == "elbow"):
				f = open(path_to_inputOutput_folder + "templates/Elbow.dfa", "r")
				txt = f.read()
				txt = txt.replace("<CURVE>", pipe_e.ID)
				txt = txt.replace("<ARC_CENTER>", pipe_e.center)
				txt = txt.replace("<X_ARC_VECTOR>", pipe_e.x_arc_vector)
				txt = txt.replace("<Y_ARC_VECTOR>", pipe_e.y_arc_vector)
				f.close()
			elif(pipe_e.type == "straight"):
				f = open(path_to_inputOutput_folder + "templates/Straight.dfa", "r")
				txt = f.read()
				txt = txt.replace("<START_POINT>", pipe_e.start_point)
				txt = txt.replace("<END_POINT>", pipe_e.end_point)
				txt = txt.replace("<LINE>", pipe_e.ID)
				f.close()
			f = open(path_to_inputOutput_folder + "products/" + design_id + ".dfa", "a") 
			f.write(txt)
			f.close
			paths_to_sweep.append(pipe_e.ID)
		return paths_to_sweep		

	def sweep_elements(elements_in_path, design_id, path):
		""" Sweeps on the paths to make the pipes """
		path_element_string_names = ''
		for e in elements_in_path:
			path_element_string_names += e + ':, '
		path_element_string_names = path_element_string_names[:-2]
		path_ID = IDGenerator.create_dfa_element_ID("path_")
		f = open(path_to_inputOutput_folder + "templates/Sweep.dfa", "r")
		txt = f.read()
		txt = txt.replace("<PATH_ID>", path_ID)
		txt = txt.replace("<PIPE_PATH>", path_element_string_names) 
		txt = txt.replace("<PROFILE_CENTER>", str(path.point_in)) 
		
		if path.point_in_dir == (1,0,0) or path.point_in_dir == (-1,0,0):
			# print("valg 1, ut av høyre / venste vegg")
			txt = txt.replace("<X_VECTOR>", str((0,1,0)))
			txt = txt.replace("<Y_VECTOR>", str((0,0,1)))
		elif path.point_in_dir == (0,0,1) or path.point_in_dir == (0,0,-1):
			# print("valg 3, ut av taket / gulvet")
			txt = txt.replace("<X_VECTOR>", str((1,0,0)))
			txt = txt.replace("<Y_VECTOR>", str((0,1,0)))

		elif path.point_in_dir == (0,1,0) or path.point_in_dir == (0,-1,0):
			# print("valg 5, ut av taket / gulvet")
			txt = txt.replace("<X_VECTOR>", str((1,0,0)))
			txt = txt.replace("<Y_VECTOR>", str((0,0,1)))
		f.close()
		f = open(path_to_inputOutput_folder + "products/" + design_id + ".dfa", "a")
		f.write(txt)
		f.close()