import csv
import matplotlib.pyplot as plt


def calculate(csv_data):
    """This function used to store the data in dictionary of total
    run score by each team in IPL history.
    """

    total_run_scored_by_each_team = {}
    for lines in csv_data:
        if total_run_scored_by_each_team.get(lines['batting_team']) == None:
            total_run_scored_by_each_team[lines['batting_team']] = int(
                lines['total_runs'])
        else:
            total_run_scored_by_each_team[lines['batting_team']
                                          ] += int(lines['total_runs'])
    return total_run_scored_by_each_team


def transfer(total_run_scored_by_each_team):
    """This function used to transfer the dictionary data into two lists."""

    team_names = list(total_run_scored_by_each_team.keys())
    team_scores = list(total_run_scored_by_each_team.values())
    return team_names, team_scores


def graph_plot(team_names, team_scores):
    """This function is used to plot the bar graph of runs score by each team."""

    plt.bar(team_names, team_scores)
    plt.xlabel("Team Name")
    plt.ylabel("runs")
    plt.title("Teams and their total runs in the IPL history.")
    plt.xticks(fontsize = 6, rotation = 90)
    plt.show()


def main():
    file = open('deliveries.csv', mode='r')
    csv_data = csv.DictReader(file)

    total_run_scored_by_each_team = calculate(csv_data)
    team_names, team_scores = transfer(total_run_scored_by_each_team)
    graph_plot(team_names, team_scores)


if __name__ == "__main__":
    main()
