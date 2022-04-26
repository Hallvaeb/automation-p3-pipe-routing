

from model.Path import Path


class PathGenerator():
	
	
	points_to_visit = []
	paths = []
	
	def __init__(self, env, list_of_equ):
		'''populates points_to_visit[], and calls fill_paths() to populate paths[]'''
		self.points_to_visit.append(env.point_A)
		for equ in list_of_equ:
			self.points_to_visit.append(equ.point_in, equ.point_out)
		self.points_to_visit.append(env.point_B)
		self.fill_paths(self)
	
	def fill_paths(self):
		""" Helper function to populate self.paths[]."""
		for i in range (0, len(self.points_to_visit), 2):
			points_in_path = []
			points_in_path.append(self.points_to_visit[i])
			points_in_path.append(self.points_to_visit[i+1])
			path = Path(points_in_path)
			self.paths.append(path)
		
		for path in self.paths:
			self.paths.append(path.gen_path())

		""" Kommentarene under er skrevet av ? før Hallvard skrev kodebiten rett over
		Jeg tenker vi har et eget objekt, path, som vi lager for hvert path. Usikker på relevanse av resten av denne klassen."""

		# Dele opp points_to_visit i paths. Points_to_visit ser slik ut f.eks.:
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