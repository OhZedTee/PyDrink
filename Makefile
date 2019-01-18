.PHONY: python3 python

run: clean-pyc
	python3 PyDrink.py || python PyDrink.py
	
clean-pyc:
	find . -name '*.pyc' -exec rm --force {} +
	find . -name '*.pyo' -exec rm --force {} +
	find . -name '*~' -exec rm --force {} +