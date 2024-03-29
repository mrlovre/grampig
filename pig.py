import re
import sys
from pathlib import Path
import unicodedata

import yaml

from utility import AttrDict, redirect_stdout

def furiganize(string):
    string = re.sub(r"[(（](.*?)[)）][\[「](.*?)[]」]", r"\\f{\1}{\2}", string)
    string = re.sub(r"(.)「(.*?)」", r"\\f{\1}{\2}", string)
    return string

def parse_entry(entry):
    kanji, *rest = re.split(r"\s*,\s*", entry)
    kanji = furiganize(kanji)
    kanji = rf"\e{{{kanji}}}"
    return kanji, *rest

with open("src/pig.yaml") as file:
    lines = file.read().split("\n")
    for i, line in enumerate(lines):
        if "　" in line:
            print(f"Popravljen japanski razmak u liniji {i}: '{line}'.", file=sys.stderr)
            is_wide = lambda c: unicodedata.east_asian_width(c) in ["W", "F"]
            print(len(f"Popravljen japanski razmak u liniji {i}: '") * " "
                  + str.join("", ["^^" if c == "　" else "  " if is_wide(c) else " " for c in line]), file=sys.stderr)

            line = line.replace("　", " ")
            lines[i] = line

    lines = str.join("\n", lines)
    lines

    data = AttrDict(yaml.safe_load(lines))

spaces = 4

Path("tex").mkdir(parents=True, exist_ok=True)

for key in data.keys():
    filename = key.replace(" ", "_")
    entry = data[key]

    with open(f"tex/{filename}.tex", "w") as file, redirect_stdout(file):
        print(rf"\renewcommand{{\backgroundcolor}}{{{entry.pozadina}}}")
        print(rf"\renewcommand{{\foregroundcolor}}{{{entry.prednjina}}}")
        print(rf"\renewcommand{{\accentcolor}}{{{entry.istaknuto}}}")

        indent = 0
        print(rf"\documentclass{{grampig}}")
        print()

        print(r"\begin{document}")
        indent += 1
        gap = " " * indent * spaces
        print(gap + r"\begin{minipage}{\width}")
        print(gap + r"\centering")

        title = [entry.pridjev, entry.imenica, entry.glagol]
        title = map(lambda x: re.split(r"\s*,\s*", x)[0], title)
        # title = map(furiganize, title)
        title = map(lambda x: re.sub(r"[（）()]", "", x), title)
        title = map(lambda x: re.sub(r"「.*?」", "", x), title)
        title = str.join("・", title)

        if entry.get("easy", "N") in ["y", "Y", "yes", "Yes", "YES",
                                      "true", "True", "TRUE",
                                      "on", "On", "ON", True]:
            print(gap + rf"{{\Large "
                        rf"\pbox[c]{{2em}}{{\includegraphics[height=1em]{{_assets/1f437}}}}\hspace{{0.8em}}"
                        rf"\pbox{{\linewidth}}{{{title}}}\hspace{{0.8em}}"
                        rf"\pbox[c]{{2em}}{{\includegraphics[height=1em]{{_assets/1f437}}}}}}")
        else:
            print(gap + rf"{{\Large {title}}}")

        print(gap + r"\vspace{2em}")
        print()

        indent += 1
        gap = " " * indent * spaces
        print(gap + r"\begin{tabular}{@{}r@{\hspace{2em}}c@{\hspace{2em}}l@{}}")

        indent += 1
        gap = " " * indent * spaces

        for key2 in ["pridjev", "imenica", "glagol"]:
            kanji, *znacenje, vrsta = parse_entry(entry[key2])
            znacenje = str.join(", ", znacenje)
            vrsta = rf"\textit{{{vrsta}}}"
            row = str.join(" & ", [kanji, znacenje, vrsta])
            row += r" \br"
            print(gap + row)

        print(gap + r"\multicolumn{3}{c}{\e{\textsc{GRATIS}}} \br")

        kanji, *znacenje, vrsta = parse_entry(entry["katakana"])
        znacenje = str.join(", ", znacenje)
        vrsta = rf"\textit{{{vrsta}}}"
        row = str.join(" & ", [kanji, znacenje, vrsta])
        row += r" \\"
        print(gap + row)

        print(gap + r"\end{tabular}")
        indent -= 1
        gap = " " * indent * spaces
        print(gap + r"\end{minipage}")
        print(r"\end{document}")
