# -*- coding: utf-8 -*-
# -*- python 3 -*-
# -*- hongzhong Lu -*-


# Import packages
import re
import numpy as np
import pandas as pd
import os    ##for directory
import sys
import pprint



def setDirectory():
    """
    This function is used to set the directory of python project
    where it has three subfold files - code, data, result.
    The script file is put in the code file.
    This function will make sure the script could be run in other computer.
    :return:
    """

    #import os
    #import sys
    # directory setting
    current_dir = os.getcwd()
    # in my script, the "code" is reset as the current directory
    new_current_dir = current_dir + "/code"
    os.chdir(new_current_dir)
    sys.path.append(new_current_dir)
# run the directory setting
# setDirectory()