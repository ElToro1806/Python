import requests
import json


ff=0
LID = input('Enter the League ID: 1) EPL 2) La Liga: ')
if(int(LID) == 1):
    ff = 1204
    from FootballEurope import *

    
elif(int(LID) == 2):
    ff = 1399
    from LaLiga import *
else:
    print('Invalid Input')


team = requests.get("http://api.football-api.com/2.0/matches?comp_id="+str(ff)+"&from_date=2017-10-13&to_date=2018-06-01&Authorization=565ec012251f932ea4000001fa542ae9d994470e73fdb314a8a56d76")
data=[]
team2 = json.loads(team.content.decode('utf-8'))
for i in range(0,len(team2)):
    local = team2[i]['localteam_name']
    away = team2[i]['visitorteam_name']
    week = team2[i]['week']
    if(int(week)<10):
        week = "0" + str(week)
        
    data.append(week+ "/" +local+ "/" +away)
    #print(local + ' - ' + away)
data = sorted(data)
'''
for j in range(0,len(data)):
    print(data[j])
'''
GameWeek = input("For which game week you like to predict? // 8-38 ")
GameWeek = int(GameWeek)-8
for j in range(GameWeek*10,GameWeek*10+10):
    print(data[j])
    details = data[j].split('/')
    home = details[1]
    if(home == "Málaga"):
        del home
        home="Malaga"
    elif(home == "Atlético Madrid"):
        del home
        home="Atletico"
    elif(home=="Deportivo La Coruña"):
        del home
        home="Deportivo"
    elif(home=='Dep. La Coruna'):
        del home
        home="Deportivo"
    elif(home=="Leganés"):
        del home
        home="Leganes"
    elif(home=="Deportivo Alavés"):
        del home
        home="Alaves"
    elif(home == "Celta de Vigo"):
        del home
        home = "Celta Vigo"
    
        
    print(home)
    away = details[2]
    if(away == "Málaga"):
        del away
        away="Malaga"
    elif(away == "Atlético Madrid"):
        del away
        away="Atletico"
    elif(away=="Deportivo La Coruña"):
        del away
        away="Deportivo"
    elif(away=='Dep. La Coruna'):
        del away
        away="Deportivo"
    elif(away=="Leganés"):
        del away
        away="Leganes"
    elif(away=="Deportivo Alavés"):
        del away
        away="Alaves"
    elif(away == "Celta de Vigo"):
        del away
        away = "Celta Vigo"
    

        
    print(away)
    try:
        dd = odds(home,away)
    except:
        print("Predictions Not Available")
        
    

