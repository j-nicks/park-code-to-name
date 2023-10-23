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

# Variables
park_codes = park_dict.keys()       # Keys (Park Codes)
park_names = park_dict.values()     # Values (Park Names)

# Functions
def list_codes():
    print("\nHere are all Park Codes:\n")
    for code in park_codes:
        print(code)

def list_names():
    print("\nHere are all Park Names:\n")
    for name in park_names:
        print(name)
        
def search_code(code):
    code = code.upper() # Convert code to uppercase
    return park_dict.get(code, "\nIncorrect entry. Please try again.")

# Program start
while True:
    request_park_info = input("*****\nType park code, or get a list by typing 'codes' or 'names'.\nType 'exit' to quit program.\n*****\n\n")

    if request_park_info.lower() == "exit":
        print("\n*****\nExiting program. Goodbye!\n*****\n")
        break

    if request_park_info == "codes":
        print(list_codes())
    elif request_park_info == "names":
        print(list_names())
    else:
        result = search_code(request_park_info)
        print(f"\nThe park for {request_park_info} is:\n{result}\n")