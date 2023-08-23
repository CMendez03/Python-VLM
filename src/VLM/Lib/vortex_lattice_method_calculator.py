import numpy as np
import math

class VortexLatticeMethodCalculator(object):

    @staticmethod
    def AICMatrixGenerator(coordinate_matrix):

        AIC_matrix = []
        aux_list = []

        for i in range(len(coordinate_matrix)):
            for j in range(len(coordinate_matrix)):
                s_contribution = VortexLatticeMethodCalculator.VLMEquation(coordinate_matrix[i,1], coordinate_matrix[i,2], coordinate_matrix[j,3],
                                                                           coordinate_matrix[j,5], coordinate_matrix[j,4], coordinate_matrix[j,6])
                p_contribution = VortexLatticeMethodCalculator.VLMEquation(coordinate_matrix[i,1], coordinate_matrix[i,2], coordinate_matrix[j,5],
                                                                           coordinate_matrix[j,3], -coordinate_matrix[j,6], -coordinate_matrix[j,4])
                aux_list.append(VortexLatticeMethodCalculator.CompleteCoeficient(s_contribution , p_contribution))

            AIC_matrix.append(aux_list)
            aux_list = []

        AIC_matrix = np.array(AIC_matrix)

        return AIC_matrix


    @staticmethod
    def VLMEquation(x_m,y_m,x_1n,x_2n,y_1n, y_2n):
        term_ab_1 = ( (x_2n - x_1n)*(x_m - x_1n) + (y_2n - y_1n)*(y_m - y_1n) ) / (math.sqrt((x_m - x_1n)**2 + (y_m - y_1n)**2))
        term_ab_2 = ( (x_2n - x_1n)*(x_m - x_2n) + (y_2n - y_1n)*(y_m - y_2n) ) / (math.sqrt((x_m - x_2n)**2 + (y_m - y_2n)**2))
        w_ab =( 1 / ( (x_m - x_1n)*(y_m - y_2n) - (x_m - x_2n)*(y_m-y_1n) ) ) * (term_ab_1 - term_ab_2)
        w_a = ( 1 / (y_1n - y_m) ) * (1 + (x_m - x_1n) / math.sqrt( (x_m - x_1n)**2 + (y_m - y_1n)**2 ) )
        w_b = - ( 1 / (y_2n - y_m) ) * (1 + (x_m - x_2n) / math.sqrt( (x_m - x_2n)**2 + (y_m - y_2n)**2 ) )

        return (1 / (4*math.pi)) * (w_ab + w_a + w_b)

    @staticmethod
    def CompleteCoeficient(s_contribution, p_contribution):
        return s_contribution + p_contribution

    @staticmethod
    def CirculationCalculator(AIC_matrix, V_inf, attack_angle):

        attack_angle = attack_angle * (math.pi / 180)

        AIC_matrix = np.matrix(AIC_matrix)
        AIC_matrix_inverse = AIC_matrix.getI()

        w_n_vector = [-V_inf * attack_angle] * len(AIC_matrix)
        w_n_vector = np.array(w_n_vector)
        w_n_vector = np.matrix(w_n_vector)
        w_n_vector = w_n_vector.getT()

        circulation_vector = np.matmul(AIC_matrix_inverse, w_n_vector)

        return circulation_vector


from VLM.Lib.discretizer import Discretizer

print(VortexLatticeMethodCalculator.CirculationCalculator(VortexLatticeMethodCalculator.AICMatrixGenerator(Discretizer.GridGeneratorSelector(5, 1, 45, 1 , 4)), 30, 3))
