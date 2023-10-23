'''
Park Code to Name converter 
'''

# Dictionary for park codes
park_codes = {
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
park_keys = park_codes.keys()       # Keys (Park Codes)
park_values = park_codes.values()   # Values (Park Names)


# Functions
def list_keys():
    for key in park_keys:
        print(key)

def list_values():
    for value in park_values:
        print(value)

'''
def search_keys(key):
    key = park_codes.get(key)
    return key
'''
    
codes_or_names = input("Would you like a list of Park 'codes' or 'names'?\n")

if codes_or_names == "codes":
    print(list_keys())
elif codes_or_names == "names":
    print(list_values())
else:
    print("Incorrect entry, please type 'codes' or 'names'.")