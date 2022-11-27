import csv
import matplotlib.pyplot as plt


def calculate(csv_data):
    """This function is used to store the data in dictionary of Royal Challengers Bangalore
    top 10 batsman name and their runs scored in IPL. And this function also sorts the 
    dictionary in decreasing order based on runs scored by a batsman.
    """

    top_10_betsman_of_rcb = {}
    for lines in csv_data:
        if lines['batting_team'] == "Royal Challengers Bangalore":
            if top_10_betsman_of_rcb.get(lines['batsman']) == None:
                top_10_betsman_of_rcb[lines['batsman']] = int(
                    lines['batsman_runs'])
            else:
                top_10_betsman_of_rcb[lines['batsman']
                                      ] += int(lines['batsman_runs'])

    top_10_betsman_of_rcb_sorted = sorted(
        top_10_betsman_of_rcb.items(), key=lambda x: x[1], reverse=True)
    betsman_names, betsman_scores = [], []
    for i in range(0, 10):
        betsman_names.append(top_10_betsman_of_rcb_sorted[i][0])
        betsman_scores.append(top_10_betsman_of_rcb_sorted[i][1])
    return betsman_names, betsman_scores


def graph_plot(betsman_names, betsman_scores):
    """This function is used to plot the bar graph of batsman name and their score."""

    plt.bar(betsman_names, betsman_scores)
    plt.xlabel("Team Name")
    plt.ylabel("runs")
    plt.title("Teams and their total runs in the IPL history.")
    plt.show()


def main():
    file = open('deliveries.csv', mode='r')
    csv_data = csv.DictReader(file)
    betsman_names, betsman_scores = calculate(csv_data)
    graph_plot(betsman_names, betsman_scores)


if __name__ == "__main__":
    main()
