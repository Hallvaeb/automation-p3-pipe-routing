

class Path():
    start_point = None
    end_point = None
    points_to_visit = []
    

    def fill_points_to_visit(self, env, list_of_equ):
        #TODO: fill out def
        self.points_to_visit.append(env.point_A)
        for equ in list_of_equ:
            self.points_to_visit.append(equ.point_in, equ.point_out)
        self.points_to_visit.append(env.point_B)

        return self.points_to_visit
    
    def get_paths(self):
        #TODO: fill out def
        # Dele opp points_to_visit i paths. Points_to_visit ser slik ut f.eks.:
        # [(xA,yA,zA), (x1,y1,z1), (x2,y2,z2), (xB, yB, zB)] (Kun ett equipment)
        # Blir da path mellom punkt A-1. og punkt 2-B. Mellom 1 og 2 er det et equipment
        
        list_of_paths = [] #vil bli: [[path1], [path2]] = [[pointA, point1], [point2, pointB]]
        for i in range(0, len(self.points_to_visit)):
            list_of_paths.append([points_to_visit i])
        
        return list_of_paths

    def get_next_direction(self, value_1, value_2):
        #TODO: fill out def
        # bestemme om vi skal ta inn hele punkter (x,y,z) eller koordinatverdier (x) el (y) el (z)
        # Sjekker de to opp mot hverandre hvor de ligger i forhold til hverandre,
        # og finner ut hvordan pathen skal gå.
        # Typ: x1 = 0, x2 = 5, da må path bevege seg fra 0 til 5 i x retn (???)
        
        return