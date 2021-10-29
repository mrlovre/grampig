import yaml
import re

def parse_entry(entry):
    kanji, *rest = re.split(r"\s*,\s*", entry)
    kanji = re.sub(r"(.)「(.*?)」", r"\\f{\1}{\2}", kanji)
    return kanji, *rest

with open("_test/test_4.yaml") as file:
    data = yaml.safe_load(file)

for key in data.keys():
    filename = key.replace(" ", "_")

    with open(f"{filename}.tex", "w") as file:
        indent = 0
        print(r"\begin{tabular}{rcl}", file=file)
        entry = data[key]

        indent += 2
        for key2 in entry:
            items = parse_entry(entry[key2])
            row = " " * indent
            row += str.join(" & ", items)
            row += r" \\"
            print(row, file=file)

        print(r"\end{tabular}", file=file)
