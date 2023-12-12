"""Module containing models representing patients and their data.

The Model layer is responsible for the 'business logic' part of the software.

Patients' data is held in an inflammation table (2D array) where each row contains 
inflammation data for a single patient taken over a number of days 
and each column represents a single day across all patients.
"""

import numpy as np
import matplotlib.pyplot as plt # add visualisation package for SR1.2.1
from functools import reduce


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


def daily_above_threshold(patient_num, data, threshold):
    """Count how many days a patient reported an inflammation rate bigger than treshold
    :param_patient_data: The patient row
    :param data: a 2D data array with inflammation data 
    :param threshold: check values above/below a value
    :returns: boolean list representing whether or not a value of a patient exceed the threshold
    """
    def count_above_threshold(a, b):
        if b:
            return a + 1
        else:
            return a
    # use map to determine if each daily inflammation is exceeds a given treshold
    above_threshold= map(lambda x: x>threshold, data[patient_num])
    # use reduce to count on how many days inflammation was above the threshold for a patient
    return reduce(count_above_threshold, above_threshold, 0)


# Structuring data functions


# def attach_names(data, names):
#     """Create data structure containing patient names records"""
#     assert len(data) == len(names)
#     output = []

#     for data_row, name in zip(data, names):
#         output.append({'patient_name': name,
#                        'data': data_row})


class Observation:
    def __init__(self, day, value):
        self.day = day
        self.value = value

    def __str__(self):
        return self.value

class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

class Patient(Person):
    """A patient in an inflammation study."""
    def __init__(self, name, observations=None):
        super().__init__(name)

        self.observations = []
        ### MODIFIED START ###
        if observations is not None:
            self.observations = observations
        ### MODIFIED END ###

    def add_observation(self, value, day=None):
        if day is None:
            try:
                day = self.observations[-1].day + 1

            except IndexError:
                day = 0

        new_observation = Observation(day, value)

        self.observations.append(new_observation)
        return new_observation