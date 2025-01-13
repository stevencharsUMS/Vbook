"""
Vbook Package
Author: stevencharsUMS
Description: Initialization of the Vbook package, a project for [add a brief description of the purpose].
"""

# Import essential modules and functions
from .main import add, divide  # Replace these with actual functions/modules in the package
from .utils import helper_function  # Replace with any utilities or helper functions

__all__ = ["add", "divide", "helper_function"]  # Define what is exported when using `from vbook import *`

# Package metadata
__version__ = "1.0.0"
__author__ = "stevencharsUMS"
__license__ = "MIT"

# Optional: Configure logging for the package
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger("vbook")

logger.info("Vbook package initialized.")
