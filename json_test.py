import json

def write():
    data = {
        "A": ["A1", "A2", "A3"],
        "B": ["B1", "B2"],
        "C": ["C1", "C2", "C3", "C4"]
    }

    json.dump(data, open("data.txt", "w"))


def read():
    data = json.load(open("data.txt", "r"))
    print(data["C"][1])


read()