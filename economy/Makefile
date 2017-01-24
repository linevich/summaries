odt:
	mkdir -p ./build
	pandoc -s --smart config.yaml *.md -o build/build.odt

pdf:
	mkdir -p ./build
	pandoc --latex-engine=xelatex -sSN --smart --chapters --template=../templates/summary.latex config.yaml *.md -o build/build.pdf
