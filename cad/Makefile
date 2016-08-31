pdf:
	mkdir -p ./build
	cd ./src/lab1/ && convert lab1.JPG drawing.pdf
	cd ./src/lab2/ && convert lab2_element_1_2.JPG lab2_element_1_2.pdf
	cd ./src/lab3/ && convert drawing.png drawing.pdf
	cd ./src/lab4/ && convert drawing.png drawing.pdf
	echo "Generating pdf...\n"
	xelatex -output-directory=./build -shell-escape document.tex

