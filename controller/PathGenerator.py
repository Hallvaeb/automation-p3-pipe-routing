

from model.Path import Path


class PathGenerator():
	
	
	def __init__(self, env, list_of_equ, pipe):
		'''populates points_to_visit[], and calls fill_paths() to populate completepaths[]'''
		# Points to visit should be like this: [A, eq1_in, eq1_out, eq2_in, eq2_out, B]
		self.all_paths = []
		self.path_objects = []
		self.points_to_visit = []
		self.points_to_visit.append(env.point_A)
		for equ in list_of_equ:
			self.points_to_visit.append(equ.point_in)
			self.points_to_visit.append(equ.point_out)
		self.points_to_visit.append(env.point_B)
		self.pipe = pipe
		self.fill_paths()
	
	def fill_paths(self):
		""" Helper function to populate self.completepaths[], containing the paths between endpoints and eqs or between equipments."""
		for i in range (0, len(self.points_to_visit), 2):
			# Clear array
			endpoints_for_path = []
			# Append next two points
			endpoints_for_path.append(self.points_to_visit[i])
			endpoints_for_path.append(self.points_to_visit[i+1])
			# Create a path object with the start and end for this path
			path = Path(endpoints_for_path, self.pipe)
			# To keep track of what paths we've generated
			self.path_objects.append(path)
			# Append this path to the list of complete paths. 
			self.all_paths.append(path.complete_path)
			print("all_paths = ", self.all_paths,  ", after i = ", i)