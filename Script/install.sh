#this script is a work in progress, working on adding library dependencies for project

# note: make sure that you only have one version of python 
# or that the version of python that is run here is the one 
# with the dependencies 

# Using Python 3.11.2
# for windows
# py -m pip install --upgrade pip
# py -m pip install numpy
# py -m pip install matplotlib
# py -m pip install tk
python -m pip install --upgrade pip setuptools wheel
pip install numpy
pip install matplotlib
pip install tk