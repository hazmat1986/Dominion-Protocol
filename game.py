#Variables
ship_name = "USS Rio Grande"
registry = "NCC-72452"
ship_class = "Danube-class runabout"
sector = "Bajoran Sector"
assignment = "Patrol"
hull = 60
max_hull = 60
power = 70
shields = 2
weapons_accuracy = 12
maneuverability = 18
warp_factor = 5.0
sisko = "Benjamin Sisko"
kira = "Kira Nerys"
obrien = "Miles O'Brien"
bashir = "Julian Bashir"
dax = "Jadzia Dax"
odo = "Odo"
divider = "="*3
#Printing
print(f"{divider} Ship Status Report: {divider}")
print(f"Ship Name: {ship_name}")
print(f"Registry: {registry}")
print(f"Ship Class: {ship_class.upper()}")
print(f"Sector: {sector}")
print(f"Assignment: {assignment}")
print(f"Hull: {hull} / {max_hull}")
print(f"Power: {power}")
print(f"Shields: {shields // 1}%")
print(f"Weapons Accuracy: {weapons_accuracy}")
print(f"Maneuverability {maneuverability}")
print(f"Warp Factor: {warp_factor}")
print("Crew Registry:")
print(f"Commanding Officer: {sisko}")
print(f"First Officer: {kira}")
print(f"Chief Engineer: {obrien}")
print(f"Chief Medical Officer: {bashir}")
print(f"Chief Science Officer: {dax}")
print(f"Security Chief: {odo}")
print("End Report")