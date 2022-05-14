clean: 
	rm -fr .tox .mypy_cache src/aerodynamics/__pycache__

format:
	black .