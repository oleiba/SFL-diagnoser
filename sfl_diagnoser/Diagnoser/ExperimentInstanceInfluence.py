import copy
import math
import random
from math import ceil
import Diagnosis
import sfl_diagnoser.Diagnoser.dynamicSpectrumInfluence
from sfl_diagnoser.Diagnoser.Experiment_Data import Experiment_Data
import sfl_diagnoser.Planner.domain_knowledge
import numpy
import sfl_diagnoser.Diagnoser.diagnoserUtils
from sfl_diagnoser.Diagnoser.Singelton import Singleton
import sfl_diagnoser.Diagnoser.ExperimentInstance

TERMINAL_PROB = 0.7


class ExperimentInstanceInfluence(sfl_diagnoser.Diagnoser.ExperimentInstance.ExperimentInstance):
    def __init__(self, initial_tests, error):
        super(ExperimentInstanceInfluence, self).__init__(initial_tests, error)

    def initials_to_DS(self):
        ds = sfl_diagnoser.Diagnoser.dynamicSpectrumInfluence.DynamicSpectrumInfluence()
        ds.setTestsComponents(copy.deepcopy([Experiment_Data().POOL[test] for test in self.get_initials()]))
        ds.setprobabilities(list(Experiment_Data().PRIORS))
        ds.seterror([self.get_error[test] for test in self.get_initials()])
        ds.settests_names(list(self.get_initials()))
        ds.set_influence_matrix(Experiment_Data().influence_matrix)
        ds.set_influence_alpha(Experiment_Data().influence_alpha)
        return ds
