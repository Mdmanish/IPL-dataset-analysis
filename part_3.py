import csv
import matplotlib.pyplot as plt


def calculate(matches_data, umpire_data):
    """This function is used to store the umpires country name in a
    dictionary and then by using this dictionary, this function creates
    another dictionary and used to store umpires country name and counts
    how many umpires are in IPL from each country except India.
    """

    umpires_and_region = {}
    for lines in umpire_data:
        if lines['country'] != ' India':
            umpires_and_region[lines['umpire']] = lines['country']

    umpire_region_count = {}
    for lines in matches_data:
        if umpires_and_region.get(lines['umpire1']) != None:
            if umpire_region_count.get(umpires_and_region[lines['umpire1']]) == None:
                umpire_region_count[umpires_and_region[lines['umpire1']]] = 1
            else:
                umpire_region_count[umpires_and_region[lines['umpire1']]] += 1

        if umpires_and_region.get(lines['umpire2']) != None:
            if umpire_region_count.get(umpires_and_region[lines['umpire2']]) == None:
                umpire_region_count[umpires_and_region[lines['umpire2']]] = 1
            else:
                umpire_region_count[umpires_and_region[lines['umpire2']]] += 1

        if umpires_and_region.get(lines['umpire3']) != None:
            if umpire_region_count.get(umpires_and_region[lines['umpire3']]) == None:
                umpire_region_count[umpires_and_region[lines['umpire3']]] = 1
            else:
                umpire_region_count[umpires_and_region[lines['umpire3']]] += 1
    return umpire_region_count


def transfer(umpire_region_count):
    """This function used to transfer the dictionary data into two lists."""

    region = list(umpire_region_count.keys())
    count = list(umpire_region_count.values())
    return region, count


def graph_plot(region, count):
    """This function is used to plot the bar graph of each country and number
    of umpires from each of country.
    """

    plt.bar(region, count)
    plt.xlabel("Country Name")
    plt.ylabel("Count")
    plt.title("3. Foreign umpire analysis.")
    # plt.xticks(rotation=90)
    plt.show()


def main():
    file = open('umpires2.csv', mode='r')
    umpire_data = csv.DictReader(file)

    file = open('matches.csv', mode='r')
    matches_data = csv.DictReader(file)

    umpire_region_count = calculate(matches_data, umpire_data)
    region, count = transfer(umpire_region_count)
    graph_plot(region, count)


if __name__ == "__main__":
    main()
