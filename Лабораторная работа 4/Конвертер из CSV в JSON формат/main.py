import json
import csv

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"

def task() -> None:
    a = open(INPUT_FILENAME, "r")
    b = open(OUTPUT_FILENAME, "w")

    reader = csv.DictReader(a)
    c = []
    for i in reader:
        c.append(i)

    json.dump(c, b, indent = 4)
    b.close()
    a.close()


if __name__ == '__main__':
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")



