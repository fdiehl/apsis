__author__ = 'Frederik Diehl'

import numpy as np


class Candidate(object):
    """
    Represents a candidate, that is a set of parameters which we are to check
    plus metadata.

    This class is used for optimizer-worker communications, and intra-optimizer
     storage. It stores the parameters,
    the result, cost and validity of the value and possesses a field for
    worker-relevant data.
    """

    params = None
    params_used = None
    result = None
    cost = None
    valid = None
    worker_information = None

    def __init__(self, params, params_used=None, result=None, valid=True,
                 worker_information=None):
        """
        Initializes the candidate object.

        It requires only the used parameter vector, the rest are optional
        information.
        :param params: A list of parameter values
        representing this candidate's parameters used.
        :param params_used: An (optional) vector of boolean values specifying
        whether a certain parameter from params
        is used. Use this function for example when describing a neural network
        where information about the third hidden layer is irrelevant when
        having less than three layers used.
        :param result: The currently achieved result for this candidate. May
        be None in the beginning.
        :param valid: Whether the candidate's result is valid.
        This may be False if, for example, the function to optimize crashes at
        certain (unknown) values.
        :param worker_information: A dictionary representing information for
        the workers. Keys should be strings.
        Can be used to, for example, store file paths where information
        necessary for continuation is stored.
        """
        #TODO add parameter validity check.
        self.params = params

        if params_used is None:
            params_used = [True]*len(self.params)
        self.params_used = params_used

        self.result = result
        self.cost = 0
        self.valid = valid

        if worker_information is None:
            worker_information = {}
        self.worker_information = worker_information

    def __eq__(self, other):
        """
        Compares two Candidates.

        Candidates are defined as being equal iff their params vectors are
        equal.
        :param other: The other Candidate.
        :return: True iff the Candidates are equal.
        """
        if not isinstance(other, Candidate):
            return False
        if self.params == other.params:
            return True
        return False

    def __str__(self):
        """
        Stringifies the object. Currently only prints the parameters and the
        result value.

        :return:
        """
        string = "\n"
        string += "params: " + str(self.params) + "\n"
        string += "result: " + str(self.result) + "\n"
        return string

    def __lt__(self, other):
        """
        Compares two Candidate instances.

        Compares their result fields.
        Parameters
        ----------

        other : Candidate
            The Candidate with whom to compare.
        """
        if not isinstance(other, Candidate):
            raise ValueError("Is not compared with a Candidate, but with "
                             + str(other) + ".")
        if self.result < other.result:
            return True
        return False