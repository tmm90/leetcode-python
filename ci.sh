set -e
pip3 install pytest==6.0.1 pytest-pylint==0.16.1 --user
pytest --pylint
pytest *.py

