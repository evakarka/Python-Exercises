# Car class
class Car:
    def __init__(self, license_plate, model):
        # Initialize a car with license plate and model
        self.license_plate = license_plate
        self.model = model

    def __str__(self):
        # Return a string representation of the car
        return f"Car(Model: {self.model}, License Plate: {self.license_plate})"


# ParkingSpot class
class ParkingSpot:
    def __init__(self, spot_number):
        # Initialize a parking spot with a unique spot number
        self.spot_number = spot_number
        self.car = None  # Initially, the parking spot is empty

    def is_empty(self):
        # Check if the parking spot is empty
        return self.car is None

    def park_car(self, car):
        # Park the car in the spot if the spot is empty
        if self.is_empty():
            self.car = car
            return True  # Successfully parked the car
        return False  # The spot is already occupied

    def free_spot(self):
        # Free the parking spot by removing the car
        if not self.is_empty():
            self.car = None
            return True  # Successfully freed the spot
        return False  # The spot was already empty

    def __str__(self):
        # Return a string representation of the parking spot
        if self.is_empty():
            return f"Spot {self.spot_number}: Empty"
        else:
            return f"Spot {self.spot_number}: Occupied by {self.car}"


# ParkingLot class
class ParkingLot:
    def __init__(self, total_spots):
        # Initialize a parking lot with a given number of spots
        self.parking_spots = [ParkingSpot(i+1) for i in range(total_spots)]

    def park_car(self, car):
        # Try to park a car in the first available spot
        for spot in self.parking_spots:
            if spot.park_car(car):
                print(f"Car with license plate {car.license_plate} parked in Spot {spot.spot_number}.")
                return True  # Car parked successfully
        print("No available spots.")  # If no spots are available, notify the user
        return False

    def remove_car(self, license_plate):
        # Remove a car from the parking lot using its license plate
        for spot in self.parking_spots:
            if not spot.is_empty() and spot.car.license_plate == license_plate:
                spot.free_spot()
                print(f"Car with license plate {license_plate} has been removed from Spot {spot.spot_number}.")
                return True  # Car successfully removed
        print(f"No car with license plate {license_plate} found.")  # If the car isn't found, notify the user
        return False

    def display_status(self):
        # Display the status of all parking spots in the parking lot
        print("Parking Lot Status:")
        for spot in self.parking_spots:
            print(spot)  # Print the status of each spot


# Testing the parking lot simulation
if __name__ == "__main__":
    # Create a parking lot with 5 parking spots
    parking_lot = ParkingLot(5)

    # Create some cars
    car1 = Car("IOA5732", "Toyota Supra")
    car2 = Car("XTZ4556", "Honda Civic")
    car3 = Car("MNM1111", "Ford Mustang")

    # Park the cars in the parking lot
    parking_lot.park_car(car1)
    parking_lot.park_car(car2)
    parking_lot.park_car(car3)

    # Display parking lot status after parking the cars
    parking_lot.display_status()

    # Remove a car (using its license plate)
    parking_lot.remove_car("XTZ4556")

    # Display parking lot status after removing a car
    parking_lot.display_status()

    # Try to park a new car after removing one
    car4 = Car("GHI012", "Chevrolet Malibu")
    parking_lot.park_car(car4)

    # Display final parking lot status
    parking_lot.display_status()
