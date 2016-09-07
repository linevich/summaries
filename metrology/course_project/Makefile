pdf:
	mkdir -p ./build
	mkdir -p ./py

	echo "Processing svg...\n"
	for f in $$(ls images/*.svg); do  inkscape -D -z --export-dpi=300 --file="$$f" --export-png="$$f".png; done;

	echo "Processing python scripts"
	python3 compile.py
	tree py

	echo "Generating pdf...\n"
	xelatex -output-directory=./build -shell-escape document.tex
#	bibtex bibliography.bib
	xelatex -output-directory=./build -shell-escape document.tex
