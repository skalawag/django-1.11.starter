rm requirements.txt development.txt
pip-compile requirements.in --output-file requirements.txt
pip-compile requirements.in development.in --output-file development.txt
