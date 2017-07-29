## Quentin Perret's PhD thesis

This repository contains the source tex files of Quentin Perret's PhD dissertation.
* Title: _Predictable execution on many-core processors_
* Context: Industrial agreement Airbus/ONERA
* Defense: 25/04/2017 at ISAE-Supaero in Toulouse, France
* Supervised by Claire Pagetti (ONERA), Éric Noulard (ONERA), Pascal Maurère (Airbus), Benoît Triquet (Airbus) and Pascal Sainrat (IRIT)

### Repository structure
```
├── README.md                                   # this file
├── main.tex                                    # the main document which includes chapters & co
├── style_tikz.tex                              # Global tikz stuffs (package include, common styles, ...)
├── biblio.bib                                  # References
├── plan.docx                                   # Thesis summary working doc
├── chps/                                       # chapters directories
│   └── chps/chap_XXX.tex                       # content of chapter XXX
├── imgs/                                       # all images
│   ├── imgs/png                                # PNG images (jpeg, bmp, ..., images must be converted)
│   ├── imgs/pdf                                # PDF images (eps, ..., must be converted)
│   ├── imgs/raw                                # Raw images, not exported (openoffice files, ...)
│   └── imgs/tex                                # Tikz images
│       ├── imgs/tex/wrapper.tex                # minimal tex to compile image - useful during dev
│       ├── imgs/tex/chap_XXX_YYY.tex           # figure YYY of chapiter XXX
│       ├── imgs/tex/all_ZZZ.tex                # shared figure ZZZ (used in several chapters)
│       └── imgs/tex/dat                        # dat files used in pgfplot to draw curves
│           ├── imgs/tex/dat/chap_XXX_YYY.dat   # data YYY of chapter XXX 
│           └── imgs/tex/dat/all_ZZZ.dat        # Shared data ZZZ
└── tlsflyleaf\*                                # University of Toulouse flyleaf
```


### Workflow
* Chapters should:
    * be packaged in documents based on the "subfiles" class
    * be compilable independentely from each others.
* TikZ figures should:
    * be raw (only `\begin{tikzpicture} ... \end{tikzpicture}` - no header, no footer)
    * have styles of nodes, arcs, ... defined globally in style\_tikz.tex
    * be compilable and tested easily thanks to `wrapper.tex` - it helps writting tikz promptly
* All labels should meet the following structure `xxx_YYY_ZZZ`:
    * YYY chapter title
    * ZZZ object title
    * xxx type of object
        * Figures           : fig
        * Tabs              : tab
        * Parts             : part
        * Chapiters         : chap
        * Sections          : sec
        * Subsections       : ssec
        * Subsubsections    : sssec
        * Paragraphs        : psec
        * Theorems          : thrm
        * Algorithms        : algo
        * Examples          : exmp
        * Remarks           : rmk
        * ...



