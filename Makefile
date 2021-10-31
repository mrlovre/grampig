.PHONY: gram pig gram_tex pig_tex png all clean

all: pig_tex gram_tex png

gram: gram_tex png

pig: pig_tex png

gram_tex:
	@python3 gram.py

pig_tex:
	@python3 pig.py

png:
	@sh make_all.sh

clean:
	@rm -rf tex _xelatex_output png
