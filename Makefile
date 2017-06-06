
.PHONY: clean

CHAP_DIR=chps
CHAP_PFIX=chap_
CHAP_PATH=$(CHAP_DIR)/$(CHAP_PFIX)

# List of chapters targets
#  - intro
#  - stateOfTheArt
#  - stateOfTheArt_2
#  - execModel
#  - framework
#  - implemExecModel
#  - validation
#  - allocation
#  - conclu


# Build the main document
main: main.tex
	pdflatex main.tex
	bibtex main
	pdflatex main.tex
	pdflatex main.tex

# Build the chapters
%: $(CHAP_PATH)%.tex
	pdflatex $^ 
	bibtex $(CHAP_PFIX)$@
	pdflatex $^ 
	pdflatex $^ 




# Cleaning procedures
clean:
	rm -rf *.aux *.out *.aux *.toc *.lof *.lot *.log *.bbl *.blg *.mtc* *.maf *-blx.bib *.run.xml *.brf *.bcf


clean_pdf:
	rm -f *.pdf
	rm -f imgs/tex/*.pdf

