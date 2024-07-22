# my_package/__init__.py
import logging

# Set up basic logging configuration
logging.basicConfig(level=logging.INFO)

# Package-level variable
VERSION = '0.1.0'


from .functions import read_data, t_embryo
