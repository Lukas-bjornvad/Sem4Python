import numpy as np
import matplotlib.pyplot as plt
filename = "befkbhalderstatkode.csv"
#1,2
def get_Data():
    out = np.genfromtxt(filename, delimiter=',', dtype=np.uint, skip_header=1)
    return out

neighb = {1: 'Indre By', 2: 'Østerbro', 3: 'Nørrebro', 4: 'Vesterbro/Kgs. Enghave', 
       5: 'Valby', 6: 'Vanløse', 7: 'Brønshøj-Husum', 8: 'Bispebjerg', 9: 'Amager Øst', 
       10: 'Amager Vest', 99: 'Udenfor'}
#3
def people_per_area():
    info = get_Data()
    population = {}
    for ids, place in neighb.items():
       masked=info[(info[:,1]==ids) & (info[:,0]==2015)]
       population[place]= np.sum(masked[:,4])
    return population
pop=people_per_area()
#print(people_per_area())
#4
plt.figure
keys = pop.keys()
val = pop.values()
plt.bar(keys,val)
plt.title("Showing population difference")
plt.show()

#5
inf = get_Data()
mask =(inf[:,2]>=65)&(inf[:,4]==2015)
dat=inf[mask]
print(dat)
#6
#går udfra at vi snakke kun scandinaviske
country_codes = {5104: 'Finland', 5105: 'Island', 5106: 'Island', 5110: 'Norge', 5120: 'Sverige'}
mask_finnish =()
mask_islandic =()
mask_norwegian=()
mask_sweden=()
print(inf[mask])
