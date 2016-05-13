pdf:
	mkdir -p ./build
	echo "Processing svg...\n"
	for f in $$(ls images/*.svg); do  inkscape -D -z --file="$$f" --export-png="$$f".png; done;
	cd ../
	echo "Generating pdf...\n"
	xelatex -output-directory=./build document.tex
