# CSE 101
# Name: DongYoon Lee
# Email: DongYoon.Lee.1@stonybrook.edu

# Part 1
import csv
def read_statistics(year):
    print('Name,', year, 'Population,', year, 'Cellular Subscriptions per 100 people', '\n', end='')
    with open('global_development.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[1] == year:
                population = round(int(float(row[9])))
                Cellular_subscriptions = round(int(float(row[11])))
                print(row[0], ',', population, ',', Cellular_subscriptions)


# Test
print('Part 1')
read_statistics("2013")
print()
# Part 2

def write_statistics_change(initial_year, later_year):
    with open('global_development.csv', 'r') as file:
        reader = csv.reader(file)
        f = open("output.csv", "w")
        temp = []
        for row in reader:
            #print(row)
            if row[1] == initial_year:
                a = row
            if row[1] == later_year:
                b = row
                temp.append([a[0], b[9], round(float(float(b[9])/float(a[9])), 2), round(float(b[11])), round(float(b[11])-(float(a[11])))])

        #print(temp)

        f.write("Name, " + later_year + " Population, Population Growth since " + initial_year + ", " + later_year + " Cellular Subscriptions per 100 people, Cellular increase since " + initial_year + "\n")
        for x in temp:
            f.write('"' + str(x[0]) + '"' + ", " + str((x[1])) + ", " + str(x[2]) + ", " + str(x[3]) + ", " + str(x[4]) + ("\n"))


# Test
print('Part 2')
write_statistics_change("2003", "2013")