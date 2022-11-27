import csv
import matplotlib.pyplot as plt


def calculate(csv_data):
    """This function is used to store the data into dictionary of dictionary
    of each team played number of matches in particular seasion.
    """

    team_and_season_match_played = {}
    for lines in csv_data:
        if team_and_season_match_played.get(lines['team1']) == None:
            team_and_season_match_played[lines['team1']] = {
                2008: 0, 2009: 0, 2010: 0, 2011: 0, 2012: 0, 2013: 0, 2014: 0, 2015: 0, 2016: 0, 2017: 0}
            team_and_season_match_played[lines['team1']][int(
                lines['season'])] = 1
        else:
            team_and_season_match_played[lines['team1']][int(
                lines['season'])] += 1
        if team_and_season_match_played.get(lines['team2']) == None:
            team_and_season_match_played[lines['team2']] = {
                2008: 0, 2009: 0, 2010: 0, 2011: 0, 2012: 0, 2013: 0, 2014: 0, 2015: 0, 2016: 0, 2017: 0}
            team_and_season_match_played[lines['team2']][int(
                lines['season'])] = 1
    return team_and_season_match_played


def graph_plot(team_and_season_match_played):
    """This function is used to plot the stacked bar graph of each 
    team played number of matches in particular seasion. And also 
    updates the value of bottom height.
    """

    team_names = list(team_and_season_match_played.keys())
    years = [2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017]
    clr = ["blue", "grey", "yellow", "green", "navy",
           "olive", "red", "pink", "purple", "black"]
    buttom_height = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    for i in range(0, 10):
        curr_year_played_count = []
        if i == 0:
            for team in team_and_season_match_played:
                curr_year_played_count.append(
                    team_and_season_match_played[team][years[i]])
            plt.bar(team_names, curr_year_played_count,
                    color=clr[i], label=years[i])
        else:
            for team in team_and_season_match_played:
                curr_year_played_count.append(
                    team_and_season_match_played[team][years[i]])
            plt.bar(team_names, curr_year_played_count, bottom=list(
                buttom_height), color=clr[i], label=years[i])

        # calculates buttom parameter (buttom_height).
        for j in range(0, 14):
            buttom_height[j] += int(curr_year_played_count[j])

    plt.xlabel("Teams")
    plt.ylabel("Match pleayed every season.")
    plt.title("4. Stacked chart of matches played by team by season")
    plt.xticks(fontsize = 7, rotation = 90)
    plt.legend()
    plt.show()


def main():
    file = open('matches.csv', mode='r')
    csv_data = csv.DictReader(file)

    team_and_season_match_played = calculate(csv_data)
    graph_plot(team_and_season_match_played)


if __name__ == "__main__":
    main()
