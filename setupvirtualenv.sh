# make a virtual environment called "osc" in the current directory
virtualenv osc --python=/usr/bin/python3

# install requirements inside virtualenv
osc/bin/pip install -r requirements.txt


# activate env
source osc/bin/activate