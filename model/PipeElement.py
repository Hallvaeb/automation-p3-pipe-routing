from controller.IDGenerator import IDGenerator


class PipeElement():


	def __init__(self, path):
		if len(path) == 3:
			# ELBOW
			self.ID = IDGenerator.create_dfa_element_ID("elbow")
			self.type = "elbow"
			self.center = str(path[0])
			self.x_arc_vector = str(path[1])
			self.y_arc_vector = str(path[2])
			
		if len(path) == 2:
			# Straight
			self.ID = IDGenerator.create_dfa_element_ID("straight")
			self.type = "straight"
			self.start_point = str(path[0])
			self.end_point = str(path[1])
