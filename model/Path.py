

class Path():
    start_point = None
    end_point = None
    

    def fill_points_to_visit(env, list_of_equ):
        #TODO: fill out def
        points_to_visit = []
        points_to_visit.append(env.get_point_A())
        for equ in list_of_equ:
            points_to_visit.append(equ.get_point_in(),equ.get_point_out())
        points_to_visit.append(env.get_point_B())

        return points_to_visit
    
    def get_paths(list):
        #TODO: fill out def
        return list

    def get_next_direction(value_1, value_2):
        #TODO: fill out def
        return