# Vehicle Fleet Management System using low-level arrays
class VehicleFleetManagement:
    def __init__(self):
        # Low-level arrays (lists) to store vehicle information
        self.vehicle_ids = []
        self.vehicle_types = []
        self.vehicle_statuses = []
        self.vehicle_mileages = []

    def add_vehicle(self):
        # Get input from user to add a vehicle
        vehicle_id = int(input("Enter Vehicle ID: "))
        vehicle_type = input("Enter Vehicle Type (e.g., Car, Truck, Van): ")
        status = input("Enter Vehicle Status (Active, In Maintenance, Under Repair): ")
        mileage = int(input("Enter Vehicle Mileage (in km): "))
        
        # Add the new vehicle data to the lists
        self.vehicle_ids.append(vehicle_id)
        self.vehicle_types.append(vehicle_type)
        self.vehicle_statuses.append(status)
        self.vehicle_mileages.append(mileage)
        print(f"Vehicle with ID {vehicle_id} added to the fleet.")

    def remove_vehicle(self):
        # Get input from user to remove a vehicle
        vehicle_id = int(input("Enter Vehicle ID to remove: "))
        
        if vehicle_id in self.vehicle_ids:
            index = self.vehicle_ids.index(vehicle_id)
            # Remove corresponding entries from all lists
            self.vehicle_ids.pop(index)
            self.vehicle_types.pop(index)
            self.vehicle_statuses.pop(index)
            self.vehicle_mileages.pop(index)
            print(f"Vehicle with ID {vehicle_id} removed from the fleet.")
        else:
            print(f"Vehicle with ID {vehicle_id} not found.")

    def update_vehicle_status(self):
        # Get input from user to update vehicle status
        vehicle_id = int(input("Enter Vehicle ID to update status: "))
        
        if vehicle_id in self.vehicle_ids:
            index = self.vehicle_ids.index(vehicle_id)
            new_status = input("Enter new status (Active, In Maintenance, Under Repair): ")
            self.vehicle_statuses[index] = new_status
            print(f"Vehicle with ID {vehicle_id} status updated to {new_status}.")
        else:
            print(f"Vehicle with ID {vehicle_id} not found.")

    def display_fleet_info(self):
        # Display information about all vehicles in the fleet
        if not self.vehicle_ids:
            print("No vehicles in the fleet.")
            return
        print("Fleet Information:")
        for i in range(len(self.vehicle_ids)):
            print(f"ID: {self.vehicle_ids[i]}, Type: {self.vehicle_types[i]}, Status: {self.vehicle_statuses[i]}, Mileage: {self.vehicle_mileages[i]} km")

# Example usage
def main():
    fleet_manager = VehicleFleetManagement()

    while True:
        print("\n--- Vehicle Fleet Management System ---")
        print("1. Add Vehicle")
        print("2. Remove Vehicle")
        print("3. Update Vehicle Status")
        print("4. Display Fleet Information")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            fleet_manager.add_vehicle()
        elif choice == '2':
            fleet_manager.remove_vehicle()
        elif choice == '3':
            fleet_manager.update_vehicle_status()
        elif choice == '4':
            fleet_manager.display_fleet_info()
        elif choice == '5':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    main()
