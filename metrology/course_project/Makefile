pdf:
	mkdir -p ./build
	echo "Processing svg...\n"
	for f in $$(ls images/*.svg); do  inkscape -D -z --export-dpi=300 --file="$$f" --export-png="$$f".png; done;
	cd ../
	echo "Generating pdf...\n"
	xelatex -output-directory=./build -shell-escape document.tex
