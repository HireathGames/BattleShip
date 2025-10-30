class Point:
    #ID represents if a ship is present and what type it is.
    #state refers to whether it unknown, a hit or a miss. 
    #The destroyed state (-2) is only visual and is functionally the same as a miss.
    def __init__(self, _ID = 0, _State = 0):
        self.ID = _ID
        self.state = _State
    def __str__(self):
        output = str(self.ID) + ", " + str(self.state)
        return(output)
    def __repr__(self):
        output = str(self.state)
        return(output)
    #Basic getters and setters
    def get_ID(self):
        return(self.ID)
    def get_State(self):
        return(self.state)
    def set_ID(self, input):
        self.ID = input
    def set_State(self, input):
        self.state = input
    #This is code for when the player selects a target, the sets it to it's proper state and returns if it hit or missed.
    def chosen_target(self):
        if self.state == 0:
            if self.ID == 0:
                self.state = -1
                return("Miss!")
            else:
                self.state = 1
                return("Hit!")
                
        else:
            return("INVALID TARGET")
class Ship:
    def __init__(self, _name, _length, _ID, _ref):
        self.name = _name
        self.length = _length
        self.ID = _ID
        self.ref = _ref
    def get_name(self):
        return(self.name)
    def get_length(self):
        return(self.length)
    def get_ID(self):
        return(self.ID)
    def get_ref(self):
        return(self.ref)
    def set_name(self, new):
        self.name = new
    def set_length(self, new):
        self.length = new
    def set_ID(self, new):
        self.ID = new
    def set_ref(self, new):
        self.ref = new
        