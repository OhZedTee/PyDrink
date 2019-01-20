.PHONY: python3 python

run: clean-pyc
	python3 PyDrink.py || python PyDrink.py
	
clean-pyc:
	@-find . -name '*.pyc' -exec rm -f {} +
	@-find . -name '*.pyo' -exec rm -f {} +
	@-find . -name '*~' -exec rm -f {} +