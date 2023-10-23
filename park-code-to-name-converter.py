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
    print("Here are the Park Codes:\n")
    for code in park_codes:
        print(code)

def list_names():
    print("Here are the Park Names:\n")
    for name in park_names:
        print(name)
        
def search_code(code):
    return park_dict.get(code, "Incorrect entry, please enter park code, or type 'codes' or 'names' for a list.")

# Program start    
request_park_info = input("Type park code, or get a list by typing 'codes' or 'names'.\n")

if request_park_info == "codes":
    print(list_codes())
elif request_park_info == "names":
    print(list_names())
else:
    result = search_code(request_park_info)
    print(f"The park for {request_park_info} is:\n{result}\n")
#else:
#    print("Incorrect entry, please enter park code, or type 'codes' or 'names' for a list.")