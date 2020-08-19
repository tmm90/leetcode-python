set -e
pip2 install coverage pytest pytest-pylint --user &> /dev/null
pytest --pylint src/*.py
coverage run -m pytest src/*.py 
coverage report -m src/*.py
