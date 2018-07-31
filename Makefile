PROGRAM= cheers.py
.include "python.prog.mk"

#BINOWN=
#BINGRP=
#BINMODE=
BINDIR=$(HOME)/bin
BINNAME=cheer


.ifndef MESSAGE
MESSAGE!=date
MESSAGE+= WIP commit
.endif

commit:
	@echo "commiting"
	git commit -m "$(MESSAGE)"

commit-all: add-all
	@git commit -m "$(MESSAGE)"

add-all:
	@git add .

