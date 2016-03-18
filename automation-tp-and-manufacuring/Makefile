odt:	
	pandoc -s config.yaml *.md -o build/build.odt

pdf:
	pandoc --latex-engine=xelatex --template=../templates/default.latex  config.yaml  *.md  -o build/build.pdf
