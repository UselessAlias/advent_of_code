class Space:
    def __init__(self,x,y,value):
        self.x = x
        self.y = y
        self.value = value

    def __repr__(self):
        return f"{self.value}"
    
    def __str__(self):
        return f"{self.value}"
    
    def __eq__(self, value):
        return (
            self.x == value.x and
            self.y == value.y and 
            self.value == value.value
        )
    
    def __lt__(self, value):
        if self.x == value.x:
            return self.y < value.y
        return self.x < value.x
    
    def __hash__(self):
        return hash(str(self))