#5A
import pandas as pd 
urlFraskilt = 'https://api.statbank.dk/v1/data/FOLK1A/CSV?valuePresentation=CodeAndValue&delimiter=Semicolon&Tid=*&Civilstand=F'
ulrIalt = 'https://api.statbank.dk/v1/data/FOLK1A/CSV?valuePresentation=CodeAndValue&delimiter=Semicolon&Tid=*&Civilstand=TOT'
dvst = pd.read_csv(urlFraskilt, sep=';')
tog = pd.read_csv(ulrIalt, sep=';')
filtered=dvst[dvst.iloc[: 0:3]]
count=0
filtered = filtered.drop(columns=['CIVILSTAND'])
for n in dvst["INDHOLD"]:
    filtered["INDHOLD"][count]=dvst["INDHOLD"][count]/tog["INDHOLD"][count] * 100
    filtered["TID"][count]= dvst["TID"][count]
    #print(dvst["INDHOLD"][count])
    count+=1
print(filtered)

#5b
urlugif = 'https://api.statbank.dk/v1/data/FOLK1A/CSV?valuePresentation=CodeAndValue&delimiter=Semicolon&Omr%C3%A5de=*&Civilstand=U'
ulrIalt = 'https://api.statbank.dk/v1/data/FOLK1A/CSV?valuePresentation=CodeAndValue&delimiter=Semicolon&Omr%C3%A5de=*&Civilstand=TOT'
dvst = pd.read_csv(urlugif, sep=';')
tog = pd.read_csv(ulrIalt, sep=';')
df= pd.DataFrame(data=tog)
filtered=dvst[dvst.iloc[: 0:3]]
count=0
df=df.sort_values(by=["INDHOLD"], ascending=False)
df2=dvst.sort_values(by=["INDHOLD"], ascending=False)
df = df.iloc[0:5]
df = df.sort_index()
filt = df.sort_index()
print(filt)
print(dvst)
#print(tog['OMRÅDE'].isin(filt['OMRÅDE']))
for n in dvst['OMRÅDE']:
    #print(n)
   
    if n in df['OMRÅDE'].unique():
        filt.loc[count,"INDHOLD"]=dvst.loc[count,"INDHOLD"]/tog.loc[count,"INDHOLD"] * 100
    count +=1
filtered.drop(columns=['CIVILSTAND'])   
print(filt)
#5C
import matplotlib.pyplot as plot
urlDvst = 'https://api.statbank.dk/v1/data/FOLK1A/CSV?valuePresentation=CodeAndValue&delimiter=Semicolon&Tid=*&Omr%C3%A5de=101&Civilstand=F'
urlUgift = 'https://api.statbank.dk/v1/data/FOLK1A/CSV?valuePresentation=CodeAndValue&delimiter=Semicolon&Tid=*&Omr%C3%A5de=101&Civilstand=U'
urlGift = 'https://api.statbank.dk/v1/data/FOLK1A/CSV?valuePresentation=CodeAndValue&delimiter=Semicolon&Tid=*&Omr%C3%A5de=101&Civilstand=E'
urlEnke = 'https://api.statbank.dk/v1/data/FOLK1A/CSV?valuePresentation=CodeAndValue&delimiter=Semicolon&Tid=*&Omr%C3%A5de=101&Civilstand=G'
ugf =pd.read_csv(urlUgift, sep=';')
dvst = pd.read_csv(urlDvst, sep=';')
gift = pd.read_csv(urlGift, sep=';')
enke = pd.read_csv(urlEnke, sep=';')

barD = plot.bar(ugf['TID'], ugf['INDHOLD'])
barU = plot.bar(dvst['TID'], dvst['INDHOLD'])
barG = plot.bar(gift['TID'], gift['INDHOLD'])
barE = plot.bar(enke['TID'], enke['INDHOLD'])

plot.legend([barU,barD, barE, barG],["Ugift","Gift","Fraskilt", "Enke"], loc=1)
plot.show()

#5D
plot.figure()
fig,f =plot.subplots()
urlUgift = 'https://api.statbank.dk/v1/data/FOLK1A/CSV?valuePresentation=CodeAndValue&Civilstand=U&alder=*'
urlGift = 'https://api.statbank.dk/v1/data/FOLK1A/CSV?valuePresentation=CodeAndValue&Civilstand=G&alder=*'
ugf =pd.read_csv(urlUgift, sep=';')
gift = pd.read_csv(urlGift, sep=';')
ugf = ugf.drop(ugf.index[0])
gift = gift.drop(gift.index[0])
bar1 = f.bar(ugf['ALDER'], ugf['INDHOLD'])
bar2 = f.bar(gift['ALDER'], gift['INDHOLD'])
f.legend()  
plot.show()
