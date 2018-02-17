import csv

places = []


def read_file():
    try:
        f = open('/Users/laurencesugars/Documents/PythonProjects/Locations/latlongs.txt')
        for student in f.readlines():
            places.append(student)
        f.close()
    except Exception:
        print("could not read file")


def save_file(results):
    try:
        f = open("places.txt", "a")
        for place in results:
            f.write("%s\n" % place)
        f.close()
    except Exception:
        print("could not write to file")


def create_csv(results):
    with open("latlongs.csv", "w") as f:
        w = csv.writer(f)
        w.writerows(results)