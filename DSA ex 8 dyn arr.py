class Voter:
    def __init__(self, voter_id, name, age, address):
        self.voter_id = voter_id
        self.name = name
        self.age = age
        self.address = address

    def update_info(self, name=None, age=None, address=None):
        if name:
            self.name = name
        if age:
            self.age = age
        if address:
            self.address = address

    def __str__(self):
        return f"ID: {self.voter_id}, Name: {self.name}, Age: {self.age}, Address: {self.address}"

class DynamicArray:
    def __init__(self):
        self.capacity = 2
        self.size = 0
        self.array = [None] * self.capacity

    def add(self, voter):
        if self.size == self.capacity:
            self.resize(self.capacity * 2)
        self.array[self.size] = voter
        self.size += 1

    def remove(self, index):
        if index < 0 or index >= self.size:
            print("Invalid index.")
            return
        for i in range(index, self.size - 1):
            self.array[i] = self.array[i + 1]
        self.array[self.size - 1] = None
        self.size -= 1
        if self.size <= self.capacity // 4:
            self.resize(self.capacity // 2)

    def resize(self, new_capacity):
        new_array = [None] * new_capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def get(self, index):
        if index < 0 or index >= self.size:
            return None
        return self.array[index]

    def get_size(self):
        return self.size

    def list_all(self):
        if self.size == 0:
            print("No voters registered.")
        else:
            for i in range(self.size):
                print(self.array[i])

    def search_by_id(self, voter_id):
        # Iterate through the array to find the voter by ID
        for i in range(self.size):
            if self.array[i].voter_id == voter_id:
                print("ID found")
                return self.array[i]
        print("ID found")

    def search_by_name(self, name):
        # Iterate through the array to find the voter by Name
        for i in range(self.size):
            if self.array[i].name.lower() == name.lower():
                return self.array[i]
        return None

def manage_voter_system():
    voters = DynamicArray()

    while True:
        print("\n--- Voter Management System ---")
        print("1. Register Voter")
        print("2. Update Voter Information")
        print("3. Delete Voter")
        print("4. List All Voters")
        print("5. Search Voter")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            voter_id = input("Enter Voter ID: ")
            name = input("Enter Voter Name: ")
            age = int(input("Enter Voter Age: "))
            address = input("Enter Voter Address: ")
            new_voter = Voter(voter_id, name, age, address)
            voters.add(new_voter)
            print(f"Voter {name} registered successfully.")

        elif choice == '2':
            voter_id = input("Enter Voter ID to update: ")
            voter = voters.search_by_id(voter_id)
            if voter:
                print(f"Found voter: {voter}")
                name = input("Enter new Name (Leave empty to keep current): ")
                age = input("Enter new Age (Leave empty to keep current): ")
                address = input("Enter new Address (Leave empty to keep current): ")

                # Update only non-empty fields
                voter.update_info(
                    name if name else None,
                    int(age) if age else None,
                    address if address else None
                )
                print("Voter information updated.")
            else:
                print("Voter not found.")

        elif choice == '3':
            voter_id = input("Enter Voter ID to delete: ")
            voter = voters.search_by_id(voter_id)
            if voter:
                # Find the index and remove the voter
                index = next(i for i, v in enumerate(voters.array) if v == voter)
                voters.remove(index)
                print(f"Voter {voter.name} deleted.")
            else:
                print("Voter not found.")

        elif choice == '4':
            print("\n--- List of All Voters ---")
            voters.list_all()

        elif choice == '5':
            search_choice = input("Search by (1) ID or (2) Name: ")
            if search_choice == '1':
                voter_id = input("Enter Voter ID: ")
                voter = voters.search_by_id(voter_id)
                if voter:
                    print(f"Voter Found: {voter}")
                else:
                    print("Voter not found.")
            elif search_choice == '2':
                name = input("Enter Voter Name: ")
                voter = voters.search_by_name(name)
                if voter:
                    print(f"Voter Found: {voter}")
                else:
                    print("Voter not found.")

        elif choice == '6':
            print("Exiting Voter Management System.")
            break

        else:
            print("Invalid choice. Please try again.")

# Run the voter management system
manage_voter_system()
