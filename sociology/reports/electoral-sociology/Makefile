odt:
	mkdir -p ./build
	pandoc -s config.yaml *.md -o build/build.odt

pdf:
	mkdir -p ./build
	pandoc --latex-engine=xelatex -S *.md *.yaml --include-before-body titlepage.tex -o build/build.pdf
