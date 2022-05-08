

from model.PipeElement import PipeElement


class Path():

    
    def __init__(self, point_in, point_in_dir, point_out, point_out_dir, pipe):
        """ Simple object to contain a path between endpoint and eq, or eq and eq, or eq and endpoint. """
        self.point_in = point_in
        self.point_in_dir = point_in_dir
        self.point_out = point_out
        self.point_out_dir = point_out_dir
        self.pipe = pipe
        self.complete_path = []
        self.gen_path()
        self.pipe_elements = []
        for path in self.complete_path:
            pipe_e = PipeElement(path)
            self.pipe_elements.append(pipe_e)

    def gen_path(self):
        if self.point_in[1] == self.point_out[1]: #XZ-PLANE
            print("Dette er punktene", self.point_in, self.point_out)
            if self.point_in[0] < self.point_out[0] and self.point_in[2] < self.point_out[2]: #self.point_out(for pathen aka slutten av path) is in Q1 for self.point_in
                print("tredje: x1 < x2 og z1<z2")
                if self.point_in_dir == (1,0,0) and self.point_out_dir == (0,0,1): #one elbow
                    print("fjerde, elbow: går til høyre og rett opp")
                    self.complete_path.append([(self.point_in[0], self.point_in[1], self.point_in[2]),(self.point_out[0] - self.pipe.elbow_radius, self.point_in[1], self.point_in[2])])
                    self.complete_path.append([(self.point_out[0] - self.pipe.elbow_radius, self.point_in[1], self.point_in[2] + self.pipe.elbow_radius), (1,0,0), (0,0,-1) ])
                    self.complete_path.append([(self.point_out[0], self.point_in[1], self.point_in[2] + self.pipe.elbow_radius),(self.point_out[0], self.point_in[1], self.point_out[2])])
                    print("Complete_path ser slik ut nå:", self.complete_path)

                elif self.point_in_dir == (-1,0,0) and self.point_out_dir == (0,0,-1): #one elbow
                    print("fjerde, elbow: går venstre og ned")
                    self.complete_path.append([(self.point_in[0], self.point_in[1], self.point_in[2]),(self.point_out[0] - self.pipe.elbow_radius, self.point_in[1], self.point_in[2])])
                    self.complete_path.append([(self.point_out[0] - self.pipe.elbow_radius, self.point_in[1], self.point_in[2] + self.pipe.elbow_radius), (1,0,0), (0,0,-1) ])
                    self.complete_path.append([(self.point_out[0], self.point_in[1], self.point_in[2] + self.pipe.elbow_radius),(self.point_out[0], self.point_in[1], self.point_out[2])])
                    print("Complete_path ser slik ut nå:", self.complete_path)

                elif self.point_in_dir == (0,0,1) and self.point_out_dir == (1,0,0): #one elbow
                    print("fjerde, elbow: går opp og til høyre")
                    self.complete_path.append([(self.point_in[0], self.point_in[1], self.point_in[2]), (self.point_in[0], self.point_in[1], self.point_out[2] - self.pipe.elbow_radius)])
                    self.complete_path.append([(self.point_in[0] + self.pipe.elbow_radius, self.point_in[1], self.point_out[2] - self.pipe.elbow_radius), (-1,0,0), (0,0,1) ])
                    self.complete_path.append([(self.point_in[0] + self.pipe.elbow_radius, self.point_in[1], self.point_out[2]),(self.point_out[0], self.point_in[1], self.point_out[2])])
                    print("Complete_path ser slik ut nå:", self.complete_path)

                    #TODO: vet ikke om dette stemmer
                # elif self.point_in_dir == (0,0,-1) and self.point_out_dir == (1,0,0): #one elbow
                #     print("fjerde, elbow: går ned og til høyre")
                #     self.complete_path.append([(self.point_in[0], self.point_in[1], self.point_in[2]), (self.point_in[0], self.point_in[1], self.point_out[2] + self.pipe.elbow_radius)])
                #     self.complete_path.append([(self.point_in[0] + self.pipe.elbow_radius, self.point_in[1], self.point_out[2] + self.pipe.elbow_radius), (-1,0,0), (0,0,-1) ])
                #     self.complete_path.append([(self.point_in[0] + self.pipe.elbow_radius, self.point_in[1], self.point_out[2]),(self.point_out[0], self.point_in[1], self.point_out[2])])
                #     print("Complete_path ser slik ut nå:", self.complete_path)
            
            elif self.point_in[0] < self.point_out[0] and self.point_in[2] > self.point_out[2]: #self.point_out(for pathen aka slutten av path) is in Q4 for self.point_in
                print("tredje: x1 < x2 og z1 > z2")
                if self.point_in_dir == (1,0,0) and self.point_out_dir == (0,0,-1): #one elbow down in z (directions here are for the PATH! in and out of the path, not equ!)
                    print("fjerde, elbow: går høyre og ned")
                    self.complete_path.append([(self.point_in[0], self.point_in[1], self.point_in[2]),(self.point_out[0] - self.pipe.elbow_radius, self.point_in[1], self.point_in[2])])
                    self.complete_path.append([(self.point_out[0] - self.pipe.elbow_radius, self.point_in[1], self.point_in[2]- self.pipe.elbow_radius ), (1,0,0), (0, 0, 1) ]) #TODO: dobbeltsjekk vektorene, 
                    self.complete_path.append([(self.point_out[0], self.point_in[1], self.point_in[2] - self.pipe.elbow_radius),(self.point_out[0], self.point_in[1], self.point_out[2])])
                    print("Complete_path ser slik ut nå, med to elbows:", self.complete_path)

                elif self.point_in_dir == (0,0,-1) and self.point_out_dir == (1,0,0): #one elbow
                    print("fjerde, elbow: går ned og til høyre")
                    print("point_out_dir:", self.point_in_dir, "point out dir", self.point_out_dir)
                    self.complete_path.append([(self.point_in[0], self.point_in[1], self.point_in[2]), (self.point_in[0], self.point_in[1], self.point_out[2] + self.pipe.elbow_radius)])
                    self.complete_path.append([(self.point_in[0] + self.pipe.elbow_radius, self.point_in[1], self.point_out[2] + self.pipe.elbow_radius), (-1,0,0), (0,0,-1) ])
                    self.complete_path.append([(self.point_in[0] + self.pipe.elbow_radius, self.point_in[1], self.point_out[2]),(self.point_out[0], self.point_in[1], self.point_out[2])])
                    print("Complete_path ser slik ut nå:", self.complete_path)

        
        if self.point_in[2] == self.point_out[2]: #XY-PLANE
            print("Dette er punktene", self.point_in, self.point_out)
            if self.point_in[0] < self.point_out[0] and self.point_in[1] < self.point_out[1]: #self.point_out(for pathen aka slutten av path) is in Q1 for self.point_in
                print("tredje: done")
                if self.point_in_dir == (1,0,0) and self.point_out_dir == (0,1,0): #one elbow
                    print("fjerde, elbow: høyre og opp (xy)")
                    self.complete_path.append([(self.point_in[0], self.point_in[1], self.point_in[2]),(self.point_out[0] - self.pipe.elbow_radius, self.point_in[1], self.point_in[2])])
                    self.complete_path.append([(self.point_out[0] - self.pipe.elbow_radius, self.point_in[1] + self.pipe.elbow_radius, self.point_in[2]), (1,0,0), (0,-1,0) ])
                    self.complete_path.append([(self.point_out[0], self.point_in[1] + self.pipe.elbow_radius, self.point_in[2]),(self.point_out[0], self.point_in[1], self.point_out[2])])
                    print("Complete_path ser slik ut nå:", self.complete_path)

                elif self.point_in_dir == (0,1,0) and self.point_out_dir == (1,0,0): #one elbow
                    print("fjerde, elbow: opp og til høyre(xy)")
                    self.complete_path.append([(self.point_in[0], self.point_in[1], self.point_in[2]),(self.point_out[0], self.point_in[1] - self.pipe.elbow_radius, self.point_in[2])])
                    self.complete_path.append([(self.point_out[0] + self.pipe.elbow_radius, self.point_in[1] - self.pipe.elbow_radius, self.point_in[2]), (-1,0,0), (0,1,0) ])
                    self.complete_path.append([(self.point_out[0] + self.pipe.elbow_radius, self.point_in[1], self.point_in[2]),(self.point_out[0], self.point_in[1], self.point_out[2])])
                    print("Complete_path ser slik ut nå:", self.complete_path)

                elif self.point_in_dir == (0,-1,0) and self.point_out_dir == (1,0,0): #one elbow
                    print("fjerde, elbow: ned og til høyre(xy)")
                    self.complete_path.append([(self.point_in[0], self.point_in[1], self.point_in[2]), (self.point_in[0], self.point_in[1]- self.pipe.elbow_radius, self.point_out[2] )])
                    self.complete_path.append([(self.point_in[0] + self.pipe.elbow_radius, self.point_in[1]- self.pipe.elbow_radius, self.point_out[2] ), (-1,0,0), (0,-1,0) ])
                    self.complete_path.append([(self.point_in[0] + self.pipe.elbow_radius, self.point_in[1], self.point_out[2]),(self.point_out[0], self.point_in[1], self.point_out[2])])
                    print("Complete_path ser slik ut nå:", self.complete_path)

                elif self.point_in_dir == (1,0,0) and self.point_out_dir == (0,-1,0): #one elbow
                    print("fjerde, elbow: høyre og ned(xy)")
                    self.complete_path.append([(self.point_in[0], self.point_in[1], self.point_in[2]), (self.point_in[0] - self.pipe.elbow_radius, self.point_in[1], self.point_out[2])])
                    self.complete_path.append([(self.point_in[0] - self.pipe.elbow_radius, self.point_in[1] - self.pipe.elbow_radius, self.point_out[2]), (1,0,0), (0,1,0) ])
                    self.complete_path.append([(self.point_in[0] - self.pipe.elbow_radius, self.point_in[1], self.point_out[2]),(self.point_out[0], self.point_in[1], self.point_out[2])])
                    print("Complete_path ser slik ut nå:", self.complete_path)
            
            # elif self.point_in[0] < self.point_out[0] and self.point_in[2] > self.point_out[2]: #self.point_out(for pathen aka slutten av path) is in Q4 for self.point_in
            #     print("tredje: x1 < x2 og z1 > z2")
            #     if self.point_in_dir == (1,0,0) and self.point_out_dir == (0,0,-1): #one elbow down in z (directions here are for the PATH! in and out of the path, not equ!)
            #         print("fjerde, elbow: går høyre og ned")
            #         self.complete_path.append([(self.point_in[0], self.point_in[1], self.point_in[2]),(self.point_out[0] - self.pipe.elbow_radius, self.point_in[1], self.point_in[2])])
            #         self.complete_path.append([(self.point_out[0] - self.pipe.elbow_radius, self.point_in[1], self.point_in[2]- self.pipe.elbow_radius ), (1,0,0), (0, 0, 1) ]) #TODO: dobbeltsjekk vektorene, 
            #         self.complete_path.append([(self.point_out[0], self.point_in[1], self.point_in[2] - self.pipe.elbow_radius),(self.point_out[0], self.point_in[1], self.point_out[2])])
            #         print("Complete_path ser slik ut nå, med to elbows:", self.complete_path)

            #     elif self.point_in_dir == (0,0,-1) and self.point_out_dir == (1,0,0): #one elbow
            #         print("fjerde, elbow: går ned og til høyre")
            #         print("point_out_dir:", self.point_in_dir, "point out dir", self.point_out_dir)
            #         self.complete_path.append([(self.point_in[0], self.point_in[1], self.point_in[2]), (self.point_in[0], self.point_in[1], self.point_out[2] + self.pipe.elbow_radius)])
            #         self.complete_path.append([(self.point_in[0] + self.pipe.elbow_radius, self.point_in[1], self.point_out[2] + self.pipe.elbow_radius), (-1,0,0), (0,0,-1) ])
            #         self.complete_path.append([(self.point_in[0] + self.pipe.elbow_radius, self.point_in[1], self.point_out[2]),(self.point_out[0], self.point_in[1], self.point_out[2])])
            #         print("Complete_path ser slik ut nå:", self.complete_path)

            
            
            else:
                self.complete_path.append(self.gen_path_x(self.point_in, self.point_out))
        
       
    def gen_path_x(self, p1, p2):
        """ Compares x-coordinates and bridges the gap """
        points_x_ok = []

        # We always start from p1
        points_x_ok.append(p1)
        
        if(p1[0] == p2[0]):
            print("1")
            # Same x, må sjekke y om vi trenger en sving.

        elif((p2[0] - p1[0]) > 0):
            print("2")

            # p2 x largest
            if(p2[1] == p1[1]):
                print("3")
                # Same y
                points_x_ok.append(p2)

        elif((p1[0] - p2[0]) > 0):
            print("4")
            if(p1[1] - p2[1] < 0):
                pass
        print("returning", points_x_ok)
        return points_x_ok

    def gen_path_y(self, p1, p2):
        """ Compares y-coordinates and bridges the gap """
        points_y_ok = []
        points_y_ok.append(p1)
        
        if((p1[1] - p2[1]) == 0):
            points_y_ok.append(p2)
            return points_y_ok

        elif((p1[1] - p2[1]) < 0):
            # Hva skal skje her?
            pass

        elif((p1[1] - p2[1]) > 0):
            # Hva skal skje her?
            pass

        return points_y_ok

    def gen_path_z(self, p1, p2):
        """ Compares z-coordinates and bridges the gap """
        points_z_ok = []
        points_z_ok.append(p1)
        
        if((p1[2] - p2[2]) == 0):
            points_z_ok.append(p2)
            return points_z_ok

        elif((p1[2] - p2[2]) < 0):
            # Hva skal skje her?
            pass

        elif((p1[2] - p2[2]) > 0):
            # Hva skal skje her?
            pass

        return 