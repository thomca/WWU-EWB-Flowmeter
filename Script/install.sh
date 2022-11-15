#this script is a work in progress, working on adding library dependencies for project

# note: make sure that you only have one version of python 
# or that the version of python that is run here is the one 
# with the dependencies 

# if things are going poorly 
# python -m pip install --upgrade --force-reinstall pip

# numpy - a complex numbers library
# matplotlib - for graphing functions
# tk - for working on GUIs in python
# reportlab - for creating pdfs if we need it

# ad python to path
# Using Python 3.11.2
# for windows check other folder

python3 -m pip install --upgrade pip setuptools wheel
pip install numpy
pip install matplotlib
pip install tk
pip install reportlab
pip install pdfrw