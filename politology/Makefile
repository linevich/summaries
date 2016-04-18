odt:
	mkdir -p ./build
	pandoc -s --smart config.yaml *.md -o build/build.odt

pdf:
	mkdir -p ./build
	pandoc --latex-engine=xelatex -sS config.yaml *.md -o build/build.pdf
