import numpy as np
import math

class LiftingCalculator(object):

    @staticmethod
    def TotalLifting(air_density, V_inf, circulation_vector, panel_span):

        fac_1 = 2 * air_density * V_inf
        fac_2 = 0

        for i in circulation_vector:
            fac_2 = fac_2 + panel_span * i

        total_lifting = fac_1 * fac_2

        return total_lifting

    @staticmethod
    def LiftCoefficientCalculator(air_density, V_inf, surface, total_lift):

        dynamic_pressure = 0.5 * air_density * V_inf**2

        CL = total_lif / (dynamic_pressure * surface)

        return CL
