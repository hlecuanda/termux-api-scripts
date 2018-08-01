PROGRAM= cheer.py
.include "python.prog.mk"

#BINOWN=hector
#BINGRP=hector
BINMODE=a+rx,u+w
BINDIR=/usr/local/bin
PYTHON=/usr/bin/env python3

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

