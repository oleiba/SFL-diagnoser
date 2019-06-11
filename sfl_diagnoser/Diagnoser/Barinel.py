__author__ = 'amir'

import csv
import math
import sys

import Diagnosis
import Staccato
import TF

prior_p = 0.05

class Barinel(object):

    def __init__(self):
        self.M_matrix = []
        self.e_vector = []
        self.prior_probs = []
        self.diagnoses = []


    def set_matrix_error(self, M, e):
        self.M_matrix = M
        self.e_vector = e

    def set_prior_probs(self, probs):
        self.prior_probs=probs

    def get_matrix(self):
        return self.M_matrix

    def get_error(self):
        return self.e_vector

    def get_diagnoses(self):
        return self.diagnoses

    def set_diagnoses(self, diagnoses):
        self.diagnoses = diagnoses

    def non_uniform_prior(self, diag):
        comps = diag.get_diag()
        prob = 1
        for i in range(len(comps)):
            prob *= self.prior_probs[comps[i]]
        return prob

    def generate_probs(self):
        new_diagnoses = []
        probs_sum = 0.0
        for diag in self.get_diagnoses():
            dk = 0.0
            if (self.prior_probs == []):
                dk = math.pow(prior_p,len(diag.get_diag())) #assuming same prior prob. for every component.
            else:
                dk = self.non_uniform_prior(diag)
            e_dk = self.tf_for_diag(diag.get_diag())
            diag.probability=e_dk * dk #temporary probability
            probs_sum += diag.probability
        for diag in self.get_diagnoses():
            temp_prob = diag.get_prob() / probs_sum
            diag.probability=temp_prob
            new_diagnoses.append(diag)
        self.set_diagnoses(new_diagnoses)

    def tf_for_diag(self, diagnosis):
        return TF.TF(self.get_matrix(), self.get_error(), diagnosis).maximize()

    def run(self):
        #initialize
        self.set_diagnoses([])
        new_diagnoses = []
        diags = Staccato.Staccato().run(self.get_matrix(), self.get_error())
        for diag in diags:
            new_diagnoses.append(Diagnosis.Diagnosis(diag))
        #generate probabilities
        self.set_diagnoses(new_diagnoses)
        self.generate_probs()
        return self.get_diagnoses()
