from sfl_diagnoser.Diagnoser import Barinel


class FullMatrix(object):
    def __init__(self):
        self.matrix=[] # matrix size define the num of tests
        self.prob_matrix=[] # matrix size define the num of tests
        self.binary_th_matrix=[] # matrix size define the num of tests
        self.probabilities=[] # probabilities size define the num of components
        self.error=[]

    def diagnose(self, status):
        bar= Barinel.Barinel()
        bar.set_matrix_error(self.matrix, self.error, self.binary_matrix)
        bar.set_prior_probs(self.probabilities)
        return bar.run(status)

    def save_to_csv_file(self, out_file):
        import csv
        lines = [self.probabilities] + map(lambda x : x[0] + [x[1]] ,zip(self.matrix, self.error))
        with open(out_file, "wb") as f:
            writer = csv.writer(f)
            writer.writerows(lines)

    # optimization: remove unreachable components & components that pass all their tests
    # return: optimized FullMatrix, chosen_components( indices)
    @staticmethod
    def optimize_FullMatrix(fullMatrix, status):
        chosen = FullMatrix.get_used_comps(fullMatrix,status)
        optimizedMatrix=FullMatrix()
        optimizedMatrix.probabilities = map(lambda c: fullMatrix.probabilities[c], chosen)
        newErr=[]
        newMatrix=[]
        if status == 1:
            for test,err in zip(fullMatrix.matrix,fullMatrix.error):
                new_test = map(lambda c: test[c], chosen)
                if any(new_test): ## optimization could remove all comps of a test
                    newMatrix.append(new_test)
                    newErr.append(err)
        if status == 2:
            for test,err in zip(fullMatrix.prob_matrix,fullMatrix.error):
                new_test = map(lambda c: test[c], chosen)
                if any(new_test): ## optimization could remove all comps of a test
                    newMatrix.append(new_test)
                    newErr.append(err)
        if status == 3:
            for test,err in zip(fullMatrix.binary_th_matrix,fullMatrix.error):
                new_test = map(lambda c: test[c], chosen)
                if any(new_test): ## optimization could remove all comps of a test
                    newMatrix.append(new_test)
                    newErr.append(err)

        optimizedMatrix.matrix=newMatrix
        #=====
        optimizedMatrix.binary_matrix=fullMatrix.matrix
        # -----
        optimizedMatrix.error=newErr
        return optimizedMatrix, sorted(chosen)

    @staticmethod
    def get_used_comps(fullMatrix, status):
        chosen = []
        UnusedComps = range(len(fullMatrix.probabilities))
        if status == 1:
            for test, err in zip(fullMatrix.matrix, fullMatrix.error):
                if err == 0:
                    continue
                for comp in list(UnusedComps):
                    if test[comp] > 0:
                        chosen.append(comp)
                        UnusedComps.remove(comp)
            return chosen
        if status == 2:
            for test, err in zip(fullMatrix.prob_matrix, fullMatrix.error):
                if err == 0:
                    continue
                for comp in list(UnusedComps):
                    if test[comp] > 0:
                        chosen.append(comp)
                        UnusedComps.remove(comp)
            return chosen
        else:
            for test, err in zip(fullMatrix.binary_th_matrix, fullMatrix.error):
                if err == 0:
                    continue
                for comp in list(UnusedComps):
                    if test[comp] > 0:
                        chosen.append(comp)
                        UnusedComps.remove(comp)
            return chosen