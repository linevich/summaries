odt:	
	pandoc -s --smart config.yaml *.md -o build/build.odt

pdf:
	pandoc --latex-engine=xelatex -sS config.yaml *.md -o build/build.pdf

latex:
	pandoc --latex-engine=xelatex config.yaml -Ss *.md -o build/build.latex
	pandoc --latex-engine=xelatex build/build.latex -o build/build.pdf
