import random
import datetime

class IDGenerator():
    
    def create_dfa_element_ID(element):
        """
            Used for DFA file children names
            Returns "zone_rrrrrrrrr" where r = random(0,9) 
        """
        r1 = str(random.randint(0, 9))
        r2 = str(random.randint(0, 9))
        r3 = str(random.randint(0, 9))
        r4 = str(random.randint(0, 9))
        r5 = str(random.randint(0, 9))
        r6 = str(random.randint(0, 9))
        r7 = str(random.randint(0, 9))
        r8 = str(random.randint(0, 9))
        r9 = str(random.randint(0, 9))
        r_all = r1+r2+r3+r4+r5+r6+r7+r8+r9
        id = element + r_all
        #print("ID generated for " +self.type+", id = " + id)
        return id
    
    def create_design_ID():
        """
            Used for DFA file names and DefClass
            Returns "type_yyyymmddhhmmrrrr" where r = random(0,9)... 16 numbers
        """
        id_date_part = datetime.datetime.now().strftime('%Y%m%d%H%M')
        r6 = str(random.randint(0, 9))
        r7 = str(random.randint(0, 9))
        r8 = str(random.randint(0, 9))
        r9 = str(random.randint(0, 9))
        r_all = id_date_part+r6+r7+r8+r9
        id = "design_" + r_all
        return id

    def create_ID():
        """
            Used for all the zones when making ID for KB
            Returns "type_rrrrrrrrr" where r = random(0,9) 
        """
        r1 = str(random.randint(0, 9))
        r2 = str(random.randint(0, 9))
        r3 = str(random.randint(0, 9))
        r4 = str(random.randint(0, 9))
        r5 = str(random.randint(0, 9))
        r6 = str(random.randint(0, 9))
        r7 = str(random.randint(0, 9))
        r8 = str(random.randint(0, 9))
        r9 = str(random.randint(0, 9))
        r_all = r1+r2+r3+r4+r5+r6+r7+r8+r9
        id = "element_" + r_all
        #print("ID generated for " +self.type+", id = " + id)
        return id