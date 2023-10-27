#DrawNames.py
#11/2/2022
#Matt Shaeffer

#Psudo Code:
# randomly chose a person to draw
#Iterate through the list:
#   randomly pick another position in the array
#   when currentposistion.secondtuple =! chosen.secondtuple:
#       remove chosen from array, append to drawnarray
import random

shaeffers = ["Matt", "Sarah", "Presley", "Nolan", "Cal", "Ben"]
lords = ['Josh','Holly','Levi','Noah','Isaac']
vaughans = ['Mitchel','Amanda','Sadie','Rachel']
powells = ['Steve','Anita']
draw_pool = shaeffers + lords + vaughans + powells
drawers = list(draw_pool)
master_list = []


#randomly chose a person to draw
for x in draw_pool:
    drawer = random.choice(draw_pool)
    drawers.remove(drawer)
    picked = random.choice(draw_pool[:draw_pool.index(drawer):])
    draw_pool.remove(picked)
    master_list.append((drawer, picked))
print(master_list)
#print("{} will be buying a gift for {}".format(drawer, picked))

#def draw_name (drawer, pool):
#    for firstname, lastname in enumerate(names):
#        draw = random.choice(names)
#        if 

