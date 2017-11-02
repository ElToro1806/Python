import pandas as pd

df = pd.read_csv('C:\\Users\\chinkasoni\\Desktop\\H2H_LaLiga.csv')

def H2H_Cal(HT='',AT=''):
    HTT =0
    ATT =0
    total = 0
    for i in range(0,len(df['homeTeam'])):
        if(df.homeTeam[i]==HT):
            if(df.awayTeam[i] ==AT):
                total+=1
                #print(str(df.homeGoalFT[i]) + " - " + str(df.awayGoalFT[i]) + " // "+str(df.date[i]) )
                if((int(df.homeGoalFT[i])-int(df.awayGoalFT[i]))>0):
                    HTT+=3
                elif((df.homeGoalFT[i]-df.awayGoalFT[i])<0):
                    ATT+=3
                else:
                    HTT+=1
                    ATT+=1
    #print(str(HTT)+" / "+str(ATT))
               
    #print('---------------')
    for i in range(0,len(df['homeTeam'])):
        if(df.homeTeam[i]==AT):
            if(df.awayTeam[i] ==HT):
                total+=1
                #print(str(df.homeGoalFT[i]) + " - " + str(df.awayGoalFT[i]) + " // "+str(df.date[i]) )
                if((int(df.homeGoalFT[i])-int(df.awayGoalFT[i]))>0):
                    ATT+=3
                elif((df.homeGoalFT[i]-df.awayGoalFT[i])<0):
                    HTT+=3
                else:
                    HTT+=1
                    ATT+=1
    return HTT,ATT,total*3

