LATEXMK = latexmk -pdf -interaction=nonstopmode -halt-on-error

.PHONY: all student teacher automatismes qa clean

all: student teacher

automatismes:
	python3 scripts/generate_automatismes.py

student:
	mkdir -p build/student
	$(LATEXMK) -outdir=build/student main.tex
	$(MAKE) -s index-student
	$(LATEXMK) -outdir=build/student main.tex
	cp build/student/main.pdf build/manuel-mathematiques-t10-eleve.pdf

teacher:
	mkdir -p build/teacher
	$(LATEXMK) -outdir=build/teacher main-prof.tex
	$(MAKE) -s index-teacher
	$(LATEXMK) -outdir=build/teacher main-prof.tex
	cp build/teacher/main-prof.pdf build/manuel-mathematiques-t10-professeur.pdf

index-student:
	@if [ -f build/student/main.idx ]; then makeindex -q -o build/student/main.ind build/student/main.idx; fi

index-teacher:
	@if [ -f build/teacher/main-prof.idx ]; then makeindex -q -o build/teacher/main-prof.ind build/teacher/main-prof.idx; fi

qa:
	python3 scripts/qa.py

clean:
	latexmk -C -outdir=build/student main.tex
	latexmk -C -outdir=build/teacher main-prof.tex
