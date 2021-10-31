#!/bin/sh

mkdir -p png
mkdir -p _xelatex_output

truncate -s0 errors.log

for filepath in tex/*.tex; do
  file=$(basename -- "$filepath")
  if [ -r "tex/.$file.md5" ] && md5sum --status -c "tex/.$file.md5"; then
    printf "%s\n" "Skipping $file."
  else
    printf "%s" "Doing $file... "
    md5sum "tex/$file" >"tex/.$file.md5"
    xelatex -synctex=1 -interaction=nonstopmode -output-directory=_xelatex_output "tex/$file" > /dev/null 2>> errors.log
    convert -density 300 "_xelatex_output/${file%.*}".pdf "png/${file%.*}".png > /dev/null 2>> errors.log
    printf "%s\n" "done!"
  fi
done
