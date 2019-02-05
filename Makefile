.PHONY: python3 python

run:
	python3 PyDrink.py || python PyDrink.py
	
clean-pyc:
	@-find . -name '*.pyc' -exec rm -f {} +
	@-find . -name '*.pyo' -exec rm -f {} +
	@-find . -name '*~' -exec rm -f {} +