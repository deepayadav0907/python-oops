# Vehicle Class

class Vehicle:

    def __init__(self, name, registration_no, model):
        self.name = name
        self.registration_no = registration_no
        self.model = model
        self.available = True

    # Display vehicle details
    def __str__(self):
        status = "Available" if self.available else "Not Available"

        return (f"Name: {self.name}, "
                f"Registration No: {self.registration_no}, "
                f"Model: {self.model}, "
                f"Availability: {status}")

# Customer Class

class Customer:

    def __init__(self, name):
        self.name = name
        self.__rented_vehicles = []

    # Rent a vehicle
    def rent_vehicle(self, vehicle):
        if vehicle.available:
            vehicle.available = False
            self.__rented_vehicles.append(vehicle)
            print(self.name, "successfully rented", vehicle.name)
        else:
            print(vehicle.name, "is not available!")

    # Return a vehicle
    def return_vehicle(self, vehicle):
        if vehicle in self.__rented_vehicles:
            vehicle.available = True
            self.__rented_vehicles.remove(vehicle)
            print(self.name, "returned", vehicle.name)
        else:
            print("This vehicle was not rented by", self.name)

    # Count rented vehicles
    def __len__(self):
        return len(self.__rented_vehicles)

    # Display customer details
    def __str__(self):
        return (f"Customer Name: {self.name}, "
                f"Rented Vehicles: {len(self)}")



# RentalShop Class

class RentalShop:

    def __init__(self):
        self.vehicles = [
            Vehicle("Honda City", "UP70AB1010", "2022"),
            Vehicle("Swift", "UP70CD2020", "2021"),
            Vehicle("Thar", "UP70EF3030", "2023"),
            Vehicle("Creta", "UP70GH4040", "2022"),
            Vehicle("Baleno", "UP70IJ5050", "2020")
        ]

    # Display all vehicles
    def show_vehicles(self):
        print("\nAll Vehicles in Rental Shop:")

        for vehicle in self.vehicles:
            print(vehicle)


# Main Program

# Create rental shop object
shop = RentalShop()

# Create two customers
customer1 = Customer("Rahul")
customer2 = Customer("Amit")

# Display all vehicles
shop.show_vehicles()

print("VEHICLE RENTAL PROCESS")

# Customer 1 rents a vehicle
customer1.rent_vehicle(shop.vehicles[0])

# Customer 2 tries to rent the same vehicle
customer2.rent_vehicle(shop.vehicles[0])

# Customer 2 rents another vehicle
customer2.rent_vehicle(shop.vehicles[1])

# Display customer details
print("CUSTOMER DETAILS")
print(customer1)
print(customer2)

# Display number of rented vehicles
print("RENTED VEHICLE COUNT")
print("Rahul rented vehicles:", len(customer1))
print("Amit rented vehicles:", len(customer2))

# Return a vehicle
print("VEHICLE RETURN")
customer1.return_vehicle(shop.vehicles[0])

# Display updated vehicle details
print("UPDATED VEHICLE STATUS")
shop.show_vehicles()

print("Program Completed Successfully!")