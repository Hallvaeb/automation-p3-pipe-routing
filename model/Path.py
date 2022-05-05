

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
        if self.point_in[0] == self.point_out[0]: #x is the same
            if self.point_in[1] < self.point_out[1] and self.point_in[2] < self.point_out[2]: #self.point_out is in Q1 for self.point_in
                if self.point_in_dir == (0,1,0) and self.point_out_dir == (0,0,1): #one elbow
                    self.complete_path[0] = [ self.point_in[0], self.point_in[1], self.point_in[2] ]
                    self.complete_path[1] = [ self.point_in[0], self.point_out[1] - self.pipe.elbow_radius, self.point_in[2]]
                    self.complete_path[3] = [ (self.point_in[0], self.point_out[1] - self.pipe.elbow_radius, self.point_in[2] + elbow rad), (1,0,0), (0,-1,0) ]
                    self.complete_path[4] = [ self.point_in[0], self.point_out[1], self.point_in[2] + self.pipe.elbow_radius]
                    self.complete_path[5] = [ self.point_in[0], self.point_out[1], self.point_out[2] ]
        return self.complete_path
