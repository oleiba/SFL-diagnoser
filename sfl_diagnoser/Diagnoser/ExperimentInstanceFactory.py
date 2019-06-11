import sfl_diagnoser.Diagnoser.ExperimentInstance
import sfl_diagnoser.Diagnoser.ExperimentInstanceInfluence
from sfl_diagnoser.Diagnoser.Experiment_Data import Experiment_Data


class ExperimentInstanceFactory(object):

    @staticmethod
    def get_experiment_instance(initials, error, experiment_type='normal'):
        classes = {'normal': sfl_diagnoser.Diagnoser.ExperimentInstance.ExperimentInstance,
                   'influence' : sfl_diagnoser.Diagnoser.ExperimentInstanceInfluence.ExperimentInstanceInfluence}
        return classes.get(experiment_type, classes['normal'])(initials, error)