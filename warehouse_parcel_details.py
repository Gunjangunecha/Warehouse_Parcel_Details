# Import necessary libraries
import csv

# Class defined
class WarehouseParcelDetail:
    def __init__(self, parcel_number, parcel_weight, parcel_category):
        self.parcel_number = parcel_number
        self.parcel_weight = parcel_weight
        self.parcel_category = parcel_category
    
    def save_and_display_parcel_details(self, parcels):
        categories = ['Filters', 'Automobil_parts', 'Cargo_containeer']
        data = {category: [] for category in categories}
        
        for parcel in parcels:
            data[parcel.parcel_category].append(parcel.parcel_number)
        
        # Display the parcel numbers in the form of a centered table
        print("\n" + "="*52)
        print("          WAREHOUSE PARCEL DETAILS")
        print("="*52)
        print("+----------+-----------------+-------------------+")
        print("| Filters  | Automobil_parts | Cargo_containeer  |")
        print("+----------+-----------------+-------------------+")
        
        max_len = max(len(data['Filters']), len(data['Automobil_parts']), len(data['Cargo_containeer']))
        
        for i in range(max_len):
            filters = str(data['Filters'][i]).center(8) if i < len(data['Filters']) else ''.center(8)
            auto_parts = str(data['Automobil_parts'][i]).center(15) if i < len(data['Automobil_parts']) else ''.center(15)
            cargo = str(data['Cargo_containeer'][i]).center(17) if i < len(data['Cargo_containeer']) else ''.center(17)
            print(f"| {filters} | {auto_parts} | {cargo} |")
            if i < max_len - 1:
                print("+----------+-----------------+-------------------+")
            else:
                print("+----------+-----------------+-------------------+")
        
        # Save the parcel numbers in a CSV file
        with open('parcel_numbers.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Filters', 'Automobil_parts', 'Cargo_containeer'])
            for i in range(max_len):
                filters = data['Filters'][i] if i < len(data['Filters']) else ''
                auto_parts = data['Automobil_parts'][i] if i < len(data['Automobil_parts']) else ''
                cargo = data['Cargo_containeer'][i] if i < len(data['Cargo_containeer']) else ''
                writer.writerow([filters, auto_parts, cargo])
        
        print("\n✓ Data saved to 'parcel_numbers.csv' successfully!")

def get_user_input():
    """Get parcel details from user input"""
    parcels = []
    
    print("\n" + "="*52)
    print("     WAREHOUSE PARCEL MANAGEMENT SYSTEM")
    print("="*52)
    print("\nAvailable Categories:")
    print("1. Filters")
    print("2. Automobil_parts")
    print("3. Cargo_containeer")
    print("-"*52)
    
    while True:
        print("\n--- Enter Parcel Details ---")
        
        # Get parcel number
        while True:
            try:
                parcel_number = int(input("Enter Parcel Number (or 0 to finish): "))
                if parcel_number == 0:
                    return parcels
                if parcel_number < 0:
                    print("Parcel number must be positive. Try again.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        # Get parcel weight
        while True:
            try:
                parcel_weight = float(input("Enter Parcel Weight (kg): "))
                if parcel_weight <= 0:
                    print("❌ Weight must be positive. Try again.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        # Get parcel category
        while True:
            print("\nSelect Category:")
            print("1 - Filters")
            print("2 - Automobil_parts")
            print("3 - Cargo_containeer")
            category_choice = input("Enter choice (1-3): ")
            
            if category_choice == '1':
                parcel_category = 'Filters'
                break
            elif category_choice == '2':
                parcel_category = 'Automobil_parts'
                break
            elif category_choice == '3':
                parcel_category = 'Cargo_containeer'
                break
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
        
        # Create parcel object and add to list
        parcel = WarehouseParcelDetail(parcel_number, parcel_weight, parcel_category)
        parcels.append(parcel)
        print(f"✓ Parcel #{parcel_number} added successfully!")
    
# Main execution
if __name__ == "__main__":
    # Get parcels from user
    parcels = get_user_input()
    
    if len(parcels) > 0:
        # Create warehouse instance and display/save details
        warehouse = WarehouseParcelDetail(0, 0, '')
        warehouse.save_and_display_parcel_details(parcels)
    else:
        print("\n No parcels were entered.")
