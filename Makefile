
#ANYFILE!=ls * |grep -v CHANGELOG
PYFILES!=ls *.py
ZSHFILES=

.BEGIN:
	@echo $(ANYFILES)


.PHONY: CHANGELOG python-scripys zsh-scripts install uninstall depends 
	
python-scripts: $(PYFILES)		
	@echo installing python scripts	
	@install -vpd $(IMPSRC) $(HOME)/bin/$(basename -s py $(IMPSRC))

zsh-scripts: $(ZSHFILES)
	@echo installing python scripts	
	@install -vpd $(IMPSRC) $(HOME)/bin/$(basename -s zsh $(IMPSRC))

install: python-scripts zsh-scripts

chg: CHANGELOG

uninstall: $(ZSHFILES) $(PYFILES)
	@rm -fv $(IMPSRC)
	
depends:
	@pip install -U click
test:
	@echo i will run them test

CHANGELOG:
	@echo generating changelog
	@git2cl >> CHANGELOG
	@git add CHANGELOG
	#@git commit --amend --no-edit
