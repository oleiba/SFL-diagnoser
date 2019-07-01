from sfl_diagnoser.Diagnoser.diagnoserUtils import readPlanningFile, write_planning_file, write_merged_matrix, writePlanningFileProbabilities, write_merged_matrix_with_new_probabilities

# preprocessing - put the probabilities into the new matrix
write_merged_matrix_with_new_probabilities("./all_methods_prediction.csv", "./matrices/Math_21.txt", "./matrices/Math_21-with-probs.txt")

base = readPlanningFile(r"./matrices/Math_21-with-probs.txt")
base.diagnose()
from sfl_diagnoser.Diagnoser.Diagnosis_Results import Diagnosis_Results
res = Diagnosis_Results(base.diagnoses, base.initial_tests, base.error)
print res.get_metrics_names()
print res.get_metrics_values()
print res.diagnoses
print res.get_new_probabilities()
new_probabilities = res.get_new_probabilities()
writePlanningFileProbabilities("./matrices/Math_21-with-probs.txt", "./matrices/Math_21-with-probs-new.txt", new_probabilities)
# round 2
print "------------"
base = readPlanningFile(r"./matrices/Math_21-with-probs-new.txt")
base.diagnose()
from sfl_diagnoser.Diagnoser.Diagnosis_Results import Diagnosis_Results
res = Diagnosis_Results(base.diagnoses, base.initial_tests, base.error)
print res.get_metrics_names()
print res.get_metrics_values()
print res.diagnoses


