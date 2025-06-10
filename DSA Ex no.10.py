# Define the initial array to store vehicle information
fleet = []

def add_vehicle(vehicle_id, vehicle_type, status, mileage):
    """Add a new vehicle to the fleet."""
    vehicle = {
        'vehicle_id': vehicle_id,
        'vehicle_type': vehicle_type,
        'status': status,
        'mileage': mileage
    }
    fleet.append(vehicle)
    print(f"Vehicle {vehicle_id} added to the fleet.")

def remove_vehicle(vehicle_id):
    """Remove an existing vehicle from the fleet by vehicle ID."""
    global fleet
    for i in range(len(fleet)):
        if fleet[i]['vehicle_id'] == vehicle_id:
            fleet.pop(i)
            print(f"Vehicle {vehicle_id} removed from the fleet.")
            return
    print(f"Vehicle with ID {vehicle_id} not found.")

def update_vehicle_status(vehicle_id, new_status):
    """Update the status of a vehicle."""
    for vehicle in fleet:
        if vehicle['vehicle_id'] == vehicle_id:
            vehicle['status'] = new_status
            print(f"Vehicle {vehicle_id} status updated to {new_status}.")
            return
    print(f"Vehicle with ID {vehicle_id} not found.")

def display_fleet():
    """Display information of all vehicles in the fleet."""
    if not fleet:
        print("No vehicles in the fleet.")
    else:
        print("\nFleet Information:")
        for vehicle in fleet:
            print(f"ID: {vehicle['vehicle_id']}, Type: {vehicle['vehicle_type']}, Status: {vehicle['status']}, Mileage: {vehicle['mileage']}")

# Example usage
while True:
    print("\nVehicle Fleet Management System")
    print("1. Add Vehicle")
    print("2. Remove Vehicle")
    print("3. Update Vehicle Status")
    print("4. Display Fleet Information")
    print("5. Exit")
    
    choice = input("Enter your choice (1-5): ")
    
    if choice == "1":
        vehicle_id = input("Enter vehicle ID: ")
        vehicle_type = input("Enter vehicle type: ")
        status = input("Enter vehicle status (Active, In Maintenance, Under Repair): ")
        mileage = float(input("Enter vehicle mileage: "))
        add_vehicle(vehicle_id, vehicle_type, status, mileage)
    
    elif choice == "2":
        vehicle_id = input("Enter vehicle ID to remove: ")
        remove_vehicle(vehicle_id)
    
    elif choice == "3":
        vehicle_id = input("Enter vehicle ID to update status: ")
        new_status = input("Enter new status (Active, In Maintenance, Under Repair): ")
        update_vehicle_status(vehicle_id, new_status)
    
    elif choice == "4":
        display_fleet()
    
    elif choice == "5":
        print("Exiting system.")
        break
    
    else:
        print("Invalid choice! Please select a valid option.")
