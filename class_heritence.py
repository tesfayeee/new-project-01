# basic/parent /super
class Hotel:
    #the Hotel Construaction 
    def __init__(self,name ,location ):

        #this class has two attributes  ; name and Location 
        self.name = name
        self.location = location

        # Method for  read operation ( read it / display the name the Location of the hotedl)
    def HotelDescription (self):
            return f"|The Hotel {self.name} is Located in {self.location } area"

    def removeLocation(self):
        return f"the hotel {self.name} "   

    def removeName(self):
        return f" the hotel  is located at {self.location}" 

        # The Child class
class LuxuryHotel(Hotel):
        def __init__(self, name, location, VIPservice ): # The structure Method of the child
            super().__init__(name, location) # the structure method  of the parent Class
            self.VIPservice = VIPservice #the attributes of the child class

        def HotelDescription (self):
              print("The Luxury Hotel ", self.name,"is located", self.location, " area and provides ", self.VIPservice, "service")

my_luxury_hotel_project = LuxuryHotel (" Sheraton","A.Abeba","swimming pool")
print(my_luxury_hotel_project.HotelDescription())

print(my_luxury_hotel_project.removeLocation())