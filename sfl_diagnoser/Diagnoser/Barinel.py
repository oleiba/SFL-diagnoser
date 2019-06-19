__author__ = 'amir'

import csv
import math
import sys

import Diagnosis
import Staccato
import TF
import copy

prior_p = 0.05

class Barinel:

    def __init__(self):
        self.M_matrix = []
        self.e_vector = []
        self.prior_probs = []
        self.diagnoses = []


    def set_matrix_error(self, M , e,binary):
        self.M_matrix = M
        self.binary_matrix= binary
        self.e_vector = e

    def set_prior_probs(self, probs):
        self.prior_probs=probs


    def non_uniform_prior(self, diag):
        comps = diag.get_diag()
        prob = 1
        for i in range(len(comps)):
            prob *= self.prior_probs[comps[i]]
        return prob

    def generate_probs(self,status,orig_eVector):
        try:
            new_diagnoses = []
            probs_sum = 0
            for diag in self.diagnoses:
                dk = 0.0
                if (self.prior_probs == []):
                    dk = math.pow(prior_p, len(diag.get_diag()))  # assuming same prior prob. for every component.
                else:
                    dk = self.non_uniform_prior(diag)

                if status == 2:
                    tmp_matrix = map(lambda test: [round(comp) for comp in test], self.M_matrix)
                    self.M_matrix =tmp_matrix
                # tf = TF.TF(self.M_matrix, self.e_vector, diag.get_diag()) # M
                tf = TF.TF(self.M_matrix, orig_eVector, diag.get_diag()) # M
                e_dk = tf.maximize()
                diag.probability = (e_dk * dk) + 0.000005  # temporary probability
                probs_sum += diag.probability
            for diag in self.diagnoses:
                temp_prob = diag.get_prob() / probs_sum
                diag.probability = temp_prob
                new_diagnoses.append(diag)
            self.diagnoses = new_diagnoses
        except:
            print("err")

    def run(self,status):
        #initialize
        self.diagnoses = []
        orig_eVector = copy.copy(self.e_vector)
        diags = Staccato.Staccato().run(self.M_matrix, self.e_vector,status)
        for  diag in diags:
            d= Diagnosis.Diagnosis()
            d.diagnosis=diag
            self.diagnoses.append(d)
        #generate probabilities
        self.generate_probs(status,orig_eVector)

        return self.diagnoses
