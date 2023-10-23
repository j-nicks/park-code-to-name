'''
Park Code to Name converter 
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
    for code in park_codes:
        print(code)

def list_names():
    for name in park_names:
        print(name)
        
def search_code(code):
    return park_dict.get(code, "Park code not found.")

    
codes_or_names = input("Would you like a list of Park 'codes' or 'names'?\n")

if codes_or_names == "codes":
    print(list_codes())
elif codes_or_names == "names":
    print(list_names())
else:
    print("Incorrect entry, please type 'codes' or 'names'.")
    

enter_code = input("Type code:\n")
result = search_code(enter_code)
print(result)