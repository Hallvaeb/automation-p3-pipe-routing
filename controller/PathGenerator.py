

from model.Path import Path


class PathGenerator():
	
	
	def __init__(self, env, list_of_equ, pipe):
		'''populates points_dir_to_visit[], and calls fill_paths() to populate completepaths[]'''
		# Points to visit should be like this: [A, eq1_in, eq1_out, eq2_in, eq2_out, B]
		self.all_paths = []
		self.path_objects = []
		self.points_dir_to_visit = []
		self.points_dir_to_visit.append(env.point_A)
		self.points_dir_to_visit.append(env.point_A_dir)

		for equ in list_of_equ:
			self.points_dir_to_visit.append(equ.point_in)
			self.points_dir_to_visit.append(equ.point_in_dir)
			self.points_dir_to_visit.append(equ.point_out)
			self.points_dir_to_visit.append(equ.point_out_dir)

		self.points_dir_to_visit.append(env.point_B)
		self.points_dir_to_visit.append(env.point_B_dir)

		self.pipe = pipe
		self.fill_paths()
	
	def fill_paths(self):
		""" Helper function to populate self.completepaths[], containing the paths between endpoints and eqs or between equipments."""
		for i in range (0, len(self.points_dir_to_visit), 4):
			path = Path(self.points_dir_to_visit[i], self.points_dir_to_visit[i+1], self.points_dir_to_visit[i+2], self.points_dir_to_visit[i+3], self.pipe) #point_in, point_in_dir, point_out, point_out_dir, pipe
			# To keep track of what paths we've generated
			self.path_objects.append(path)
			# Append this path to the list of complete paths. 
			self.all_paths.append(path.complete_path)