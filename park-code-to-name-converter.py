'''
Park Info (Code / Name converter)
'''

# Dictionary for park codes
park_dict = {
    "AH": "Kent Coast",
    "BD": "Blue Dolphin",
    "BE": "Berwick",
    "BR": "Burnham On Sea",
    "CC": "Caister-on-Sea",
    "CF": "Church Farm",
    "CG": "Cala Gran",
    "CH": "Combe Haven",
    "CT": "Craig Tara",
    "DE": "Devon Cliffs",
    "DF": "Doniford Bay",
    "FG": "Far Grange",
    "GR": "Greenacres",
    "GS": "Golden Sands",
    "HA": "Haggerston Castle",
    "HM": "Hafan Y Mor",
    "HO": "Hopton",
    "KP": "Kiln Park",
    "LA": "Lakeland",
    "LS": "Littlesea",
    "LY": "Lydstep Beach",
    "MM": "Marton Mere",
    "OR": "The Orchards",
    "PC": "Penally Court",
    "PH": "Presthaven",
    "PS": "Perran Sands",
    "PV": "Primrose Valley",
    "QW": "Quay West",
    "RE": "Reighton Sands",
    "RP": "Rockley Park",
    "RV": "Riviere Sands",
    "SA": "Seashore",
    "SE": "Seton Sands",
    "SN": "Skegness Holiday Park",
    "SV": "Seaview",
    "TP": "Cleepthorpes Beach",
    "TW": "Thornwick",
    "WD": "Wild Duck",
    "WM": "Weymouth Bay"
}

# Function to get park code from user
def get_park_code(code):
    code = code.upper()  # Convert request to uppercase
    
    if code in park_dict:
        return park_dict[code]
    else:
        return "\nIncorrect entry. Please try again."

# Program start
while True:
    park_info = input("*****\nType park code, or get a list by typing 'codes' or 'names'.\nType 'exit' to quit program.\n*****\n\n")

    if park_info.lower() == "exit":
        print("\n*****\nExiting program. Goodbye!\n*****\n")
        break

    if park_info == "codes":
        print("\nHere are all Park Codes:\n")
        for code in park_dict.keys():
            print(code)
    elif park_info == "names":
        print("\nHere are all Park Names:\n")
        for name in park_dict.values():
            print(name)
    else:
        result = get_park_code(park_info)
        print(f"\nThe park for {park_info} is: {result}\n")