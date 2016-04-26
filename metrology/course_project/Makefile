odt:
	mkdir -p ./build
	pandoc -s --smart config.yaml *.md -o build/build.odt

pdf:
	mkdir -p ./build
	pandoc --latex-engine=xelatex  --number-sections -sS config.yaml *.md  --bibliography bibliography.bib --biblatex -o build/build.pdf

# Демо команда для конфігурації LaTeX
latex:
	mkdir -p ./build
	pandoc --number-sections -sS config.yaml *.md  --bibliography bibliography.bib --biblatex -o build/build.tex
