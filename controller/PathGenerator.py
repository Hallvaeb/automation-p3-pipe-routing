

from model.Path import Path


class PathGenerator():
	
	
	points_to_visit = []
	complete_paths = []
	
	def __init__(self, env, list_of_equ, pipe):
		'''populates points_to_visit[], and calls fill_paths() to populate completepaths[]'''
		# Points to visit should be like this: [A, eq1_in, eq1_out, eq2_in, eq2_out, B]
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
			points_in_path = []
			# Append next two points
			points_in_path.append(self.points_to_visit[i])
			points_in_path.append(self.points_to_visit[i+1])
			# Create a path object with the start and end for this path
			path = Path(points_in_path, self.pipe)
			# Ask path to make necessary turns etc to connect start to end
			path_for_this_path = path.gen_path()
			# Append this path to the list of complete paths. 
			self.complete_paths.append(path_for_this_path)