import csv
import matplotlib.pyplot as plt

def graphPlot(x,y,xl,yl,tt):
    fig= plt.figure(figsize=(30,5))
    plt.bar(x,y)
    plt.xlabel(xl)
    plt.ylabel(yl)
    plt.title(tt)
    plt.show()

# 1. Total runs scored by team
def total_run_scored(totalRun):
    #print(len(totalRun))
    teamList= list(totalRun.keys())
    runList= list(totalRun.values())
    graphPlot(teamList,runList,"Team Name","runs","Teams and their total runs in the IPL history.")

# 2. Top batsman for Royal Challengers Bangalore
def top_betsman(batsman):
    batsmanSorted = sorted(batsman.items(),key= lambda x: x[1], reverse=True)
    batsmanName, runs = [],[]
    for i in range(0,10):
        batsmanName.append(batsmanSorted[i][0])
        runs.append(batsmanSorted[i][1])
    graphPlot(batsmanName,runs,"Batsman Name","Runs","Batsman and their runs in IPL history")

# 5. Number of matches played per year for all the years in IPL.
def numberOfMatchPlayedEveryYear(years):
    year= list(years.keys())
    count= list(years.values())
    graphPlot(year,count,"Years","Total matches","Years v/s number of matches played.")

# 7. Extra runs conceded per team in the year 2016
def extraRuns(extraRun):
    team= list(extraRun.keys())
    run= list(extraRun.values())
    graphPlot(team,run,"Team name","extra runs","7. Extra runs conceded per team in the year 2016")
    
 # 8. Top 10 economical bowlers in the year 2015"  
def economicalBowlers(bowlerRun,bowlerOver):
    ecoBowlers={}
    for bowler in bowlerRun:
        ecoBowlers[bowler]= bowlerRun[bowler]/bowlerOver[bowler]
    
    ecoBowlersSorted = sorted(ecoBowlers.items(),key= lambda x: x[1])
    bowlerName, runs = [],[]
    for i in range(0,10):
        bowlerName.append(ecoBowlersSorted[i][0])
        runs.append(ecoBowlersSorted[i][1])
    graphPlot(bowlerName,runs, "bowler name","runs","8. Top 10 economical bowlers in the year 2015")

# 6. Number of matches won per team per year in IPL.
def wonPerTeamPerYear(teamAndYear):
    #print(len(teamAndYear))
    teamName= list(teamAndYear.keys())
    years= [2008,2009,2010,2011,2012,2013,2014,2015,2016,2017]
    clr= ["blue","grey","yellow","green","navy","olive","red","pink","purple","black"]
    bottMarks= [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    fig= plt.figure(figsize=(30,5))
    for i in range(0,10):
        currYearWon=[]
        if i==0:
            for team in teamAndYear:
                currYearWon.append(teamAndYear[team][years[i]])
            plt.bar(teamName,currYearWon,color=clr[i],label= years[i])
        else:
            for team in teamAndYear:
                currYearWon.append(teamAndYear[team][years[i]])
            plt.bar(teamName,currYearWon,bottom=list(bottMarks),color=clr[i],label= years[i])
        # calculates bottom parameter.
        for j in range(0,15):
            bottMarks[j]+= int(currYearWon[j])
    
    plt.xlabel("Teams")
    plt.ylabel("match won every season.")
    plt.title("6. Stacked chart of matches won by team by season")
    plt.legend()
    plt.show()
                

# 4. Stacked chart of matches played by team by season
def numberOfGamePlayed(teamAndSeason):
    teamName= list(teamAndSeason.keys())
    years= [2008,2009,2010,2011,2012,2013,2014,2015,2016,2017]
    clr= ["blue","grey","yellow","green","navy","olive","red","pink","purple","black"]
    bottMarks= [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    #print(len(teamAndSeason))
    fig= plt.figure(figsize=(30,5))
    for i in range(0,10):
        currYearPlayedCount =[]
        if i==0:
            for team in teamAndSeason:
                currYearPlayedCount.append(teamAndSeason[team][years[i]])
            plt.bar(teamName,currYearPlayedCount,color=clr[i],label= years[i])
        else:
            for team in teamAndSeason:
                currYearPlayedCount.append(teamAndSeason[team][years[i]])
            plt.bar(teamName,currYearPlayedCount,bottom=list(bottMarks),color=clr[i],label= years[i])
        
        # calculates bottom parameter.
        for j in range(0,14):
            bottMarks[j]+= int(currYearPlayedCount[j])
    plt.xlabel("Teams")
    plt.ylabel("match pleayed every season.")
    plt.title("4. Stacked chart of matches played by team by season")
    plt.legend()
    plt.show()

'''
In my dataset I was not having umpires region(country), so I have taken data manually from
this link "https://stats.espncricinfo.com/ci/engine/records/individual/most_matches_umpire.html?id=117;type=trophy".
And I stored the data in csv file.
    Below this function is used to store the data in csv file.
    No need to run this function again.

def dataCollection():
    header= ["UmpireName","Country"]
    umpires=[
        ["S Ravi","India"],
        ["AK Chaudhary","India"],
        ["HDPK Dharmasena","Sri Lanka"],
        ["C Shamshuddin","India"],
        ["Nitin Menon","India"],
        ["CB Gaffaney","New Zealand"],
        ["M Erasmus","South Africa"],
        ["CK Nandan","India"],
        ["BNJ Oxenford","Australia"],
        ["KN Ananthapadmanabhan","India"],
        ["SJA Taufel","India"],
        ["RJ Tucker","Australia"],
        ["Asad Rauf","Pakistan"],
        ["VA Kulkarni","India"],
        ["VK Sharma","India"],
        ["BR Doctrove","West Indies"],
        ["RE Koertzen","South Africa"],
        ["RK Illingworth","England"],
        ["Aleem Dar","Pakistan"],
        ["BF Bowden","New Zealand"],
        ["NJ Llong","England"],
        ["AY Dandekar","India"],
        ["S Asnani","India"],
        ["SK Tarapore","India"],
        ["RB Tiffin","Zimbabwe"],
        ["YC Barde","India"],
        ["DJ Harper","Australia"],
        ["PR Reiffel","Australia"],
        ["AM Saheba","India"],
        ["A Nand Kishore","India"],
        ["K Hariharan","India"],
        ["UV Gandhe","India"],
        ["BG Jerling","South Africa"],
        ["JD Cloete","South Africa"],
        ["SS Hazare","India"],
        ["PG Pathak","India"],
        ["K Srinath","India"],
        ["IL Howell","South Africa"],
        ["SL Shastri","India"],
        ["MR Benson","England"],
        ["S Das","India"],
        ["A Deshmukh","India"],
        ["MA Gough","England"],
        ["J Madanagopal","India"],
        ["K Srinivasan","India"],
        ["RM Deshpande","India"],
        ["Tapan Sharma","India"]
    ]
    with open('umpires.csv' , 'w') as f:
        csvwriter= csv.writer(f)
        csvwriter.writerow(header)
        csvwriter.writerows(umpires)
'''
# 3. Foreign umpire analysis
def foreignUmpire(umpireSet):
    tempUmpireDict={}
    finalUmpireDict={}
    with open('umpires.csv',mode='r') as file:
        data= csv.DictReader(file)
        for lines in data:
            tempUmpireDict[lines['UmpireName']]= lines['Country']

    for umpire in umpireSet:
        if tempUmpireDict.get(umpire)!= None and tempUmpireDict[umpire]!="India" and finalUmpireDict.get(tempUmpireDict[umpire])==None:
            finalUmpireDict[tempUmpireDict[umpire]]= 1
        elif tempUmpireDict.get(umpire)!= None and tempUmpireDict[umpire]!="India" and finalUmpireDict.get(tempUmpireDict[umpire])!=None:
            finalUmpireDict[tempUmpireDict[umpire]] +=1
    umpireCountry= list(finalUmpireDict.keys())
    count= list(finalUmpireDict.values())
    #print(len(umpireSet))
    graphPlot(umpireCountry,count,"Country Name","no. of umpires", "Foreign umpire analysis")


def main():
    deliveriesData, matchesData = [],[]
    totalRun, batsman={},{}
    extraRun={}
    bowlerRun, bowlerOver ={},{}
    prev= "PrevTeam"
    with open('deliveries.csv',mode='r') as file:
        data= csv.DictReader(file)
        for lines in data:

            # 1. Total runs scored by team
            if totalRun.get(lines['batting_team'])==None:
                totalRun[lines['batting_team']]= int(lines['total_runs'])
            else:
                totalRun[lines['batting_team']] += int(lines['total_runs'])

            # 2. Top batsman for Royal Challengers Bangalore
            if lines['batting_team']== "Royal Challengers Bangalore":
                if batsman.get(lines['batsman'])==None:
                    batsman[lines['batsman']]= int(lines['batsman_runs'])
                else:
                    batsman[lines['batsman']] += int(lines['batsman_runs'])

            # 7. Extra runs conceded per team in the year 2016
            if int(lines['match_id'])>= 577 and int(lines['match_id'])<=636:
                if extraRun.get(lines['batting_team'])==None:
                    extraRun[lines['batting_team']]= int(lines['extra_runs'])
                else:
                    extraRun[lines['batting_team']] += int(lines['extra_runs'])

            # 8. Top 10 economical bowlers in the year 2015"
            if int(lines['match_id'])>= 518 and int(lines['match_id'])<=576:
                if bowlerRun.get(lines['bowler'])==None:
                    bowlerRun[lines['bowler']]= int(lines['total_runs'])
                    bowlerOver[lines['bowler']]= 0
                else:
                    bowlerRun[lines['bowler']] += int(lines['total_runs'])
                if lines['bowler']!= prev:
                    bowlerOver[lines['bowler']] += 1
                    prev= lines['bowler']

            
    years={}
    teamAndYear={}
    teamAndSeason={}
    umpireSet= set()
    with open('matches.csv',mode='r') as file:
        data= csv.DictReader(file)
        for lines in data:

            # 5. Number of matches played per year for all the years in IPL.
            if years.get(lines['season'])==None:
                years[lines['season']]= 1
            else:
                years[lines['season']] += 1

            # 6. Number of matches won per team per year in IPL.
            if teamAndYear.get(lines['winner'])==None:
                teamAndYear[lines['winner']]= {2008:0,2009:0,2010:0,2011:0,2012:0,2013:0,2014:0,2015:0,2016:0,2017:0}
                teamAndYear[lines['winner']][int(lines['season'])]= 1
            else:
                teamAndYear[lines['winner']][int(lines['season'])] += 1
            
            # 4. Stacked chart of matches played by team by season
            if teamAndSeason.get(lines['team1'])==None:
                teamAndSeason[lines['team1']]= {2008:0,2009:0,2010:0,2011:0,2012:0,2013:0,2014:0,2015:0,2016:0,2017:0}
                teamAndSeason[lines['team1']][int(lines['season'])]= 1
            else:
                teamAndSeason[lines['team1']][int(lines['season'])] += 1
            if teamAndSeason.get(lines['team2'])==None:
                teamAndSeason[lines['team2']]= {2008:0,2009:0,2010:0,2011:0,2012:0,2013:0,2014:0,2015:0,2016:0,2017:0}
                teamAndSeason[lines['team2']][int(lines['season'])]= 1
            else:
                teamAndSeason[lines['team2']][int(lines['season'])] += 1

            # 3. Foreign umpire analysis
            umpireSet.add(lines['umpire1'])
            umpireSet.add(lines['umpire2'])
            umpireSet.add(lines['umpire3'])


    while True :
        print("What do you want to execute? enter: \n1 for total_run_scored()\n2 for top_betsman()\n3 for foreignUmpire()\n4 for numberOfGamePlayed()\n5 for numberOfMatchPlayedEveryYear()\n6 for wonPerTeamPerYear()\n7 for extraRuns()\n8 for economicalBowlers()\n9 for dataCollection()\n0 for all.")
        fun= int(input())
        match fun:
            case 0:
                total_run_scored(totalRun)
                top_betsman(batsman)
                foreignUmpire(umpireSet)
                numberOfGamePlayed(teamAndSeason)
                numberOfMatchPlayedEveryYear(years)
                wonPerTeamPerYear(teamAndYear)
                extraRuns(extraRun)
                economicalBowlers(bowlerRun,bowlerOver)
                #dataCollection()
            case 1:
                total_run_scored(totalRun)
            case 2:
                top_betsman(batsman)
            case 3:
                foreignUmpire(umpireSet)
            case 4:
                numberOfGamePlayed(teamAndSeason)
            case 5:
                numberOfMatchPlayedEveryYear(years)
            case 6:
                wonPerTeamPerYear(teamAndYear)
            case 7:
                extraRuns(extraRun)
            case 8:
                economicalBowlers(bowlerRun,bowlerOver)
            case 9:
                #dataCollection()
                pass
            case default:
                print("You have entered wrong.")
        print("Do you want to continue(1) or not(0)?")
        flag= int(input())
        if flag==0:
            break

if __name__=="__main__":
    main()