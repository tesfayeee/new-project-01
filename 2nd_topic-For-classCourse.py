class Hotel:
    def __init__(self, name, location, rooms):
    #initialize th hotel with a name , location, and number of rooms
        self.name = name
        self.location = location
        self.rooms = rooms
        self.booked_rooms = 0

    #Book info Create Operation
    def book_room(self, number_of_rooms):
        """Book a specified number of room  ."""
        if number_of_rooms <=0:
                print("Number of book must be positive")
                return
        if self.booked_rooms + number_of_rooms > self.rooms:  #room  means  available
             print("Not Enough Available rooms ot book.")
             
        self.booked_rooms += number_of_rooms
        print(f"{number_of_rooms} room(s) successfully book .")

    #book info delete operation 
    def checkout (self,number_of_rooms):
        if number_of_rooms <=0:
            print("Number of rooms to checkout must be positive." )
            return
        if number_of_rooms > self.booked_rooms:

            print(f"{number_of_rooms} room(s) successfully checked out .")
    def get_availablility(self):
        # Get the number of Available 
        available_rooms = self.rooms - self.booked_rooms
        return available_rooms 
    
        #return a string representation of the Hotel
        return f"Hotel: {self.name}, location; {self.location}, Total rooms: {self.rooms}, Booked rooms: {self.booked_rooms}"
    
#create an Object of the Hotel class
my_hotel = Hotel("seaside Report", "Caliafornia ", 40)
    
#Accessing  Attributes and methods
print(my_hotel) # display Hotel details

#Booking Rooms 

my_hotel.book_room(22)
print(f"Available rooms: {my_hotel.get_availablility()}")  #check available rooms


#Checking Out rooms 
my_hotel.checkout(7)
print(f"Available rooms: {my_hotel.get_availablility()}")  #check available rooms