"""Module containing models representing patients and their data.

The Model layer is responsible for the 'business logic' part of the software.

Patients' data is held in an inflammation table (2D array) where each row contains 
inflammation data for a single patient taken over a number of days 
and each column represents a single day across all patients.
"""

import numpy as np
import matplotlib.pyplot as plt # add visualisation package for SR1.2.1


def load_csv(filename):
    """Load a Numpy array from a CSV

    :param filename: Filename of CSV to load
    """
    return np.loadtxt(fname=filename, delimiter=',')


def daily_mean(data):
    """Calculate the daily mean of a 2D inflammation data array for each day.

    :param data: a 2D data array with inflammation data (each row contains measurements for a single patient across all days).
    :returns: an array of mean values for each day.
    """
    return np.mean(data, axis=0)

def daily_stdv(data):
    """SR1.1.1: Calculate the daily standard deviation of a 2D inflammation data array for each day.

    :param data: a 2D data array with inflammation data (each row contains measurements for a single patient across all days).
    :returns: an array of standard deviation values for each day.
    """
    return np.std(data, axis=0)


def daily_max(data):
    """Calculate the daily maximun of a 2D inflammation data array for each day.
    
    :param data: a 2D data array with inflammation data (each row contains measurements for a single patient across all days).
    :returns: an array of max values of measurements for each day.
    
    """
    return np.max(data, axis=0)


def daily_min(data):
    """Calculate the daily minimun of a 2D inflammation data array for each day.
    
    :param data: a 2D data array with inflammation data (each row contains measurements for a single patient across all days).
    returns: an array of minimun values of measurements for each day.
    """
    return np.min(data, axis=0)

