

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
		



		""" Kommentarene under er skrevet av ? før Hallvard skrev kodebiten rett over. Usikker på relevanse av resten av denne klassen."""








		# Dele opp points_to_visit i complete_paths. Points_to_visit ser slik ut f.eks.:
		# [(xA,yA,zA), (x1,y1,z1), (x2,y2,z2), (xB, yB, zB)] (Kun ett equipment)
		# Blir da path mellom punkt A-1. og punkt 2-B. Mellom 1 og 2 er det et equipment
		# Dette er ikke ferdig, kun en start på en tankegang..
		# list_of_paths = [] #vil bli: [[path1], [path2]] = [[pointA, point1], [point2, pointB]]
		# for i in range(0, len(self.points_to_visit)): #må få denne til å lage path mellom to og to
		#     list_of_paths.append([points_to_visit])
		

	def get_next_direction(self, value_1, value_2):
		#TODO: implement
		# bestemme om vi skal ta inn hele punkter (x,y,z) eller koordinatverdier (x) el (y) el (z)
		# Sjekker de to opp mot hverandre hvor de ligger i forhold til hverandre,
		# og finner ut hvordan pathen skal gå.
		# Typ: x1 = 0, x2 = 5, da må path bevege seg fra 0 til 5 i x retn (???)
		
		return