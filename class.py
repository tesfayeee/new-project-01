class Hotel:   #i`m defining class, (ibsa isaa)
    def __init__(self,name,numberOfRooms,location,services):
        self.name = name #= is an attributes the hol   d to  name  
        self.numberOfRoms #= is an attributes the hold to 
        self.location #= is an attributes the hold to 
        self.services   #= is an attributes the hold to

    #To Create a read operation function 
    def ViewHotelRoms(self):
        return f"The hotel {self.name} has {self.numberOfRooms} rooms"
    
    def ViewHotelLocation(self):
        return f"The hotel {self.name} is in {self.location}"
 #create  an object on the class
object_1 = Hotel("elina",150, "A.A", "swimming pool, spa, Meeting hall")
object_2 = Hotel("sheraton",1500,"A.A", "swimming pool, spa, Meeting hall")

print(object_1.ViewHotelRooms)