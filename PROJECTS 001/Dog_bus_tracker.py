# 🐾 Dog Bus Tracker — Challenge Steps
#
# 1. Start with a bus dictionary holding current passengers.
#    - Each seat number (1, 2, 3, ...) is a key
#    - Each value is another dictionary with each pet's:
#        • name
#        • breed
#        • pickup time
#        • dropoff time
#
# 2. Print a starting roster showing each pet’s seat, name, and pickup time.
#
# 3. Add one new pet if there’s room on the bus.  
#    - Use MAX_SEATS to limit capacity.  
#    - Dynamically assign the next seat number.  
#    - Print the updated roster showing all pets after pickup.  
#
# 4. Ask which pet leaves early.  
#    - Remove that pet from the bus.  
#    - Print a message saying they’ve headed home.  
#
# 5. Print a final roster listing the remaining pets and their dropoff times. 
#----------------------------------------------------------------------------


MAX_SEATS = 5

# Starting bus dictionary with nested pet dictionaries
bus = {
    1: {
        "name": "Buddy",
        "breed": "Golden Retriever", 
        "pickup_time": "8:00 AM",
        "dropoff_time": "5:00 PM"
    },
    2: {
        "name": "Luna",
        "breed": "Husky",
        "pickup_time": "8:15 AM", 
        "dropoff_time": "4:45 PM"
    },
    3: {
        "name": "Max",
        "breed": "Labrador",
        "pickup_time": "8:30 AM",
        "dropoff_time": "5:15 PM"
    }
}

def print_roster(bus, show_dropoff=False):
    """Print the current roster of pets on the bus"""
    print(f"\n�� Current Bus Roster ({len(bus)} pets):")
    print("-" * 50)
    
    for seat, pet in bus.items():
        if show_dropoff:
            print(f"Seat {seat}: {pet['name']} ({pet['breed']}) - Dropoff: {pet['dropoff_time']}")
        else:
            print(f"Seat {seat}: {pet['name']} ({pet['breed']}) - Pickup: {pet['pickup_time']}")

def add_new_pet(bus):
    """Add a new pet to the bus if there's room"""
    if len(bus) >= MAX_SEATS:
        print(f"\n❌ Bus is full! Maximum capacity is {MAX_SEATS} pets.")
        return False
    
    # Find the next available seat
    next_seat = max(bus.keys()) + 1 if bus else 1
    
    print(f"\n🐕 Adding new pet to seat {next_seat}...")
    
    # Get pet details from user
    name = input("Enter pet name: ")
    breed = input("Enter pet breed: ")
    pickup_time = input("Enter pickup time (e.g., 9:00 AM): ")
    dropoff_time = input("Enter dropoff time (e.g., 6:00 PM): ")
    
    # Add pet to bus
    bus[next_seat] = {
        "name": name,
        "breed": breed,
        "pickup_time": pickup_time,
        "dropoff_time": dropoff_time
    }
    
    print(f"✅ {name} has been added to seat {next_seat}!")
    return True

def remove_pet(bus):
    """Remove a pet from the bus"""
    if not bus:
        print("\n❌ No pets on the bus to remove.")
        return
    
    print(f"\n🐾 Current pets on the bus:")
    for seat, pet in bus.items():
        print(f"Seat {seat}: {pet['name']} ({pet['breed']})")
    
    try:
        seat_to_remove = int(input("\nEnter the seat number of the pet leaving early: "))
        
        if seat_to_remove in bus:
            pet_name = bus[seat_to_remove]["name"]
            del bus[seat_to_remove]
            print(f"🏠 {pet_name} has headed home from seat {seat_to_remove}!")
        else:
            print(f"❌ No pet found in seat {seat_to_remove}.")
    except ValueError:
        print("❌ Please enter a valid seat number.")

def main():
    print("🐾 Welcome to the Dog Bus Tracker! 🐾")
    print("=" * 50)
    
    # Step 2: Print starting roster
    print_roster(bus)
    
    # Step 3: Add new pet if there's room
    print(f"\n�� Bus capacity: {len(bus)}/{MAX_SEATS} seats occupied")
    add_choice = input("\nWould you like to add a new pet? (y/n): ").lower()
    
    if add_choice == 'y':
        if add_new_pet(bus):
            print("\n📋 Updated roster after adding new pet:")
            print_roster(bus)
    
    # Step 4: Ask which pet leaves early
    if bus:
        leave_choice = input("\nWould you like a pet to leave early? (y/n): ").lower()
        if leave_choice == 'y':
            remove_pet(bus)
    
    # Step 5: Print final roster with dropoff times
    if bus:
        print_roster(bus, show_dropoff=True)
    else:
        print("\n�� Bus is now empty - all pets have gone home!")

if __name__ == "__main__":
    main()


    