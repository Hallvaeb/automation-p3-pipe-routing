

class Path():

    
    end_points = []
    complete_path = []
    
    def __init__(self, end_points):
        """ Simple object to contain a path between endpoint and eq, or eq and eq, or eq and endpoint. """
        self.end_points = end_points

    def gen_path(self):
        """ Populate self.path_between_points[] with points to connect the endpoints. """
        path_between_endpoints = []
        
        for i in range (0, len(self.end_points), 2):
            p1 = self.end_points[i]
            p2 = self.end_points[i+1]
            self.complete_path.append(self.gen_path_x(p1, p2))
            self.complete_path.append(self.gen_path_y(p1, p2))
            self.complete_path.append(self.gen_path_z(p1, p2))
        
        return self.complete_path

    def gen_path_x(self, p1, p2):
        """ Compares x-coordinates and bridges the gap """
        points_x_ok = []
        points_x_ok.append(p1)
        
        if((p1.x - p2.x) == 0):
            points_x_ok.append(p2)
            return points_x_ok

        elif((p1.x - p2.x) < 0):
            # Hva skal skje her?
            pass

        elif((p1.x - p2.x) > 0):
            # Hva skal skje her?
            pass

        return points_x_ok

    def gen_path_y(self, p1, p2):
        """ Compares y-coordinates and bridges the gap """
        points_y_ok = []
        points_y_ok.append(p1)
        
        if((p1.y - p2.y) == 0):
            points_y_ok.append(p2)
            return points_y_ok

        elif((p1.y - p2.y) < 0):
            # Hva skal skje her?
            pass

        elif((p1.y - p2.y) > 0):
            # Hva skal skje her?
            pass

        return points_y_ok

    def gen_path_z(self, p1, p2):
        """ Compares z-coordinates and bridges the gap """
        points_z_ok = []
        points_z_ok.append(p1)
        
        if((p1.z - p2.z) == 0):
            points_z_ok.append(p2)
            return points_z_ok

        elif((p1.z - p2.z) < 0):
            # Hva skal skje her?
            pass

        elif((p1.z - p2.z) > 0):
            # Hva skal skje her?
            pass

        return points_z_ok
