import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename, delimiter=',', new_line='\n') -> list[dict]:
    with open(filename) as input_f:
        inform = []
        for n, m in enumerate(input_f):
            filling = m.strip(new_line).split(delimiter)
            if n == 0:
                l = filling
                continue

            inform.append({})

            for i, _ in enumerate(l):
                inform[-1][l[i]] = filling[i]
    return inform


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
