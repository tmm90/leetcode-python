set -e
pip2 install coverage pytest pytest-pylint --user
pytest --pylint
coverage run -m pytest src/*.py 
coverage report -m src/*.py
