import re
from pathlib import Path

import yaml

from utility import AttrDict, redirect_stdout

def markup(string):
    string = re.sub(r"[_＿](.*?)[_＿]", r"\\e{\1}", string)
    string = re.sub(r"[(（](.*?)[)）][\[「](.*?)[]」]", r"\\f{\1}{\2}", string)
    string = re.sub(r"(.)[\[「](.*?)[]」]", r"\\f{\1}{\2}", string)
    string = re.sub(r"⇒", r"$\\Rightarrow$", string)

    return string

with open("src/gram.yaml") as file:
    data = AttrDict(yaml.safe_load(file))

Path("tex").mkdir(parents=True, exist_ok=True)

for key, e in data.items():
    with open(f"tex/{key}.tex", "w") as file, redirect_stdout(file):
        options = [e.tezina]

        if e.bless in ["y", "Y", "yes", "Yes", "YES", "true", "True", "TRUE", "on", "On", "ON"]:
            options += ["bless"]

        options = str.join(",", options)
        print(rf"\documentclass[{options}]{{grampig}}")
        print()
        superscript = None
        rbr = e.get("rbr", None)

        if rbr:
            superscript = rf"\textsuperscript{{{rbr}}}"

        print(rf"\title{{{e.kljuc}{superscript}}}")
        print(rf"\pos{{{e.vrsta}}}")
        print()

        print(r"\begin{document}")
        print(r"    \maketitle")
        print(rf"    {markup(e.obj1)}\\")
        print(rf"    {markup(e.obj2)}")
        print(r"    \vspace{0.5em}")
        print()

        n_fields = len(re.split(r"([＋⇒])", e.tvorba[0].jap))
        cols = "c" * n_fields
        print(r"    \begin{table}")
        print(r"        \label{tab:tvorba}")
        print(r"        \centering")
        print(rf"        \begin{{tabular}}{{@{{}}{cols}@{{}}}}")

        for tvorba in e.tvorba:
            chunks = re.split(r"([＋⇒])", tvorba.jap)
            chunks = map(markup, chunks)
            chunks = str.join(" & ", chunks) + r" \bh"
            print(rf"            {chunks}")
            chunks = re.split(r"(\+|(?:=>))", tvorba.hrv)
            chunks = [chunk if chunk not in ["+", "=>"] else "" for chunk in chunks]
            chunks = map(markup, chunks)
            chunks = str.join(" & ", chunks) + r" \\"
            print(rf"            {chunks}")
        print(r"        \end{tabular}")
        print(r"    \end{table}")
        print()

        print(r"    \begin{itemize}")

        for primjer in e.primjeri:
            print(rf"        \item {markup(primjer.jap)}\bh")
            print(rf"        {markup(primjer.hrv)}")

        print(r"    \end{itemize}")
        print(r"\end{document}")
