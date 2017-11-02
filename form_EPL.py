import requests
import json

r = requests.get("http://api.football-api.com/2.0/standings/1204?Authorization=565ec012251f932ea4000001fa542ae9d994470e73fdb314a8a56d76")
data = json.loads(r.content.decode('utf-8'))
dd ={}
for i in range(0,len(data)):
        df = list(data[i]['recent_form'])
        total =0
        for j in range(0,len(df)):
            if(df[j]=='W'):
                total+=3
            elif(df[j]=='D'):
                total+=1
                

        home = data[i]['team_name']
        if(home == "Málaga"):
                del home
                home="Malaga"
        elif(home == "Atlético Madrid"):
                del home
                home="Atletico"
        elif(home=="Deportivo La Coruña"):
                del home
                home="Deportivo La Coruna"
        elif(home=="Leganés"):
                del home
                home="Leganes"
        elif(home=="Deportivo Alavés"):
                del home
                home="Alaves"
        elif(home == "Celta de Vigo"):
                del home
                home = "Celta Vigo"
        elif(home == "Leicester"):
                home = "Leicester City"
        elif(home == "West Brom"):
                home = "West Bromwich Albion"
        elif(home == "West Ham"):
                home = "West Ham United"
        elif(home == 'Newcastle Utd'):
                home = 'Newcastle United'
        elif(home=='Bournemouth'):
                home = 'AFC Bournemouth'
        elif(home=='Tottenham'):
                home = 'Tottenham Hotspur'
        elif(home=='Swansea'):
                home ='Swansea City'
        dd[home] = total
def Form_Cal(HT='',AT=''):
        return dd[HT],dd[AT]
    



        
    
        
