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

# Use
parcels = [
    WarehouseParcelDetail(23456, 66234, 'Filters'),
    WarehouseParcelDetail(66234, 86643, 'Automobil_parts'),
    WarehouseParcelDetail(98432, 53463, 'Cargo_containeer'),
    WarehouseParcelDetail(96355, 86643, 'Filters'),
    WarehouseParcelDetail(86643, 53463, 'Automobil_parts'),
    WarehouseParcelDetail(53463, 87653, 'Cargo_containeer'),
    WarehouseParcelDetail(83722, 64326, 'Filters'),
    WarehouseParcelDetail(64326, 87653, 'Automobil_parts'),
    WarehouseParcelDetail(87653, 98432, 'Cargo_containeer'),
]

warehouse = WarehouseParcelDetail(0, 0, '')
warehouse.save_and_display_parcel_details(parcels)
