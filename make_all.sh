#!/bin/sh

mkdir -p png
mkdir -p _xelatex_output

for file in *.tex; do
  echo -n "Doing $file... "
  xelatex -synctex=1 -interaction=nonstopmode -output-directory=_xelatex_output "$file" >/dev/null
  convert -density 300 "_xelatex_output/${file%.*}".pdf "png/${file%.*}".png >/dev/null
  echo "done!"
done
