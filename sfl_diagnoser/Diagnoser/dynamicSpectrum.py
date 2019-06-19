import sfl_diagnoser.Diagnoser
import math
# from sfl_diagnoser.Diagnoser.diagnoserUtils import write_planning_file
from sfl_diagnoser.Diagnoser.FullMatrix import FullMatrix
from sfl_diagnoser.Diagnoser.Experiment_Data import Experiment_Data


class dynamicSpectrum(object):
    def __init__(self):
        self.TestsComponents=[] # TestsComponents size define the num of tests
        self.probabilities=[] # probabilities size define the num of components
        self.tests_names = []
        self.error=[]

    def convertToFullMatrix(self):
        ans=FullMatrix()
        ans.probabilities=list(self.probabilities)
        ans.error=list(self.error)
        #TODO change to prob
        ans.matrix = map(lambda test: map(lambda comp: 1 if comp in test else 0, range(len(self.probabilities))), self.TestsComponents)
        ans.prob_matrix = map(lambda test_name: map(lambda comp: float(Experiment_Data().top_40_dict[test_name][str(comp)]) if str(comp) in Experiment_Data().top_40_dict[test_name].keys() else 0,range(len(self.probabilities))), self.tests_names)
        tmp_matrix = map(lambda test: [(comp - min(test)) / (max(test) - min(test)) for comp in test], ans.prob_matrix)
        ans.binary_th_matrix = map(lambda test: [round(comp) for comp in test], tmp_matrix)

        return ans

    def remove_duplicate_tests(self):
        distinct_tests = set(map(str, zip(self.TestsComponents, self.error)))
        names = []
        chosen = []
        error = []
        for name, test, e in zip(self.tests_names, self.TestsComponents, self.error):
            repr = str((test, e))
            if repr in distinct_tests:
                names.append(name)
                chosen.append(test)
                error.append(e)
                distinct_tests.remove(repr)
        ds = dynamicSpectrum()
        ds.probabilities = self.probabilities
        ds.tests_names= names
        ds.TestsComponents = chosen
        ds.error = error
        return ds

    def get_tests_by_error(self, error):
        return map(lambda test: test[1], filter(lambda test: self.error[test[0]] == error, enumerate(self.TestsComponents)))

    def get_failed_tests(self):
        return self.get_tests_by_error(1)

    def get_passed_tests(self):
        return self.get_tests_by_error(0)

    def get_components(self):
        return set(reduce(list.__add__, self.TestsComponents))

    def get_components_in_failed_tests(self):
        return set(reduce(list.__add__, self.get_failed_tests(), []))

    def optimize(self):
        """
        return new DS object without components that not included in any failed tests.
        """
        failed_components = self.get_components_in_failed_tests()
        new_names = []
        new_tests = []
        new_probabilities = map(lambda p: p[1], filter(lambda p: p[0] in failed_components, enumerate(self.probabilities)))
        new_error = []
        for name, test, e in zip(self.tests_names, self.TestsComponents, self.error):
            new_test = filter(lambda comp: comp in failed_components, test)
            if new_test == []:
                continue
            new_names.append(name)
            new_tests.append(new_test)
            new_error.append(e)
        ds = dynamicSpectrum()
        ds.probabilities = new_probabilities
        ds.tests_names = new_names
        ds.TestsComponents = new_tests
        ds.error = new_error
        return ds

    #return diagnoses
    def diagnose(self,status):
        optimaized_matrix,chosen=FullMatrix.optimize_FullMatrix(self.convertToFullMatrix(), status)
        chosenDict=dict(enumerate(chosen))
        Opt_diagnoses=optimaized_matrix.diagnose(status)
        diagnoses=[]
        for diag in Opt_diagnoses:
            diag=diag.clone()
            diag_comps=[chosenDict[x] for x in diag.diagnosis]
            diag.diagnosis=list(diag_comps)
            diagnoses.append(diag)
        return diagnoses
