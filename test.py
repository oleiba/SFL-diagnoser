from sfl_diagnoser.Diagnoser.diagnoserUtils import readPlanningFile, write_planning_file, write_merged_matrix
# from sfl_diagnoser.Diagnoser.diagnoserUtils import readPlanningFile, write_planning_file, write_merged_matrix
# from sfl_diagnoser.Diagnoser.Diagnosis_Results import Diagnosis_Results


def merge_same_components(self):
    components_vector = {}
    for test in self.TestsComponents:
        for component in test:
            components_vector.setdefault(component, []).append(test)
    similiar_componets = {}
    for component in components_vector:
        similiar_componets.setdefault(str(sorted(components_vector[component])), []).append(component)


def check_influence():
    base = readPlanningFile(r"c:\temp\base_matrix.txt")
    base.diagnose()
    base_results = Diagnosis_Results(base.diagnoses, base.initial_tests, base.error)
    added = readPlanningFile(r"c:\temp\added_matrix.txt")
    added.diagnose()
    added_results = Diagnosis_Results(added.diagnoses, added.initial_tests, added.error)
    pass

def get_xref_diagnoses(instance, seperator="$"):
    def xref_comp_to_function(xref_comp):
        return xref_comp.split(seperator)[1]
    instance.diagnose()
    diagnoses = map(lambda diagnosis: map(xref_comp_to_function, diagnosis), instance.diagnoses)
    for diagnosis in diagnoses:
        diagnosis.diagnosis = list(set(diagnosis))
    return diagnoses

def abstraction():
    write_planning_file(r"c:\temp\yemp_matrix.txt", ["a"], [["T1", ["a", "b", "d"], 1],
                                                            ["T2", ["b"], 0],
                                                            ["T3", ["a", "b", "c"], 1],
                                                            ["T4", ["a", "b", "c"], 0]])
    instance = readPlanningFile(r"c:\temp\yemp_matrix.txt")
    write_planning_file(r"c:\temp\yemp_matrix.txt", ["a"], [["T1", ["a", "b", "d"], 1],
                                                            ["T2", ["b"], 0],
                                                            ["T3", ["a", "b"], 1],
                                                            ["T4", ["a", "b"], 0]])
    instance = readPlanningFile(r"c:\temp\yemp_matrix.txt")
    write_planning_file(r"c:\temp\yemp_matrix.txt", ["a"], [["T1", ["a", "b"], 1],
                                                            ["T2", ["b"], 0],
                                                            ["T3", ["a", "b"], 1],
                                                            ["T4", ["a", "b"], 0]])
    instance = readPlanningFile(r"c:\temp\yemp_matrix.txt")
    print "a"
