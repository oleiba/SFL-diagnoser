from SFL_diagnoser.Diagnoser.diagnoserUtils import readPlanningFile
from SFL_diagnoser.Diagnoser.Diagnosis_Results import Diagnosis_Results
import SFL_diagnoser.Diagnoser.ExperimentInstance


inst = readPlanningFile("C:\\Users\\eyalhad\\Desktop\\SFL-diagnoser\\MatrixFileProb2.txt")
inst.diagnose()
results = Diagnosis_Results(inst.diagnoses, inst.initial_tests, inst.error)
results.get_metrics_names()
results.get_metrics_values()
ei = SFL_diagnoser.Diagnoser.ExperimentInstance.addTests(inst, inst.hp_next())
i=5