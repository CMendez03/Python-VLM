from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from VLM.Lib.discretizer import Discretizer
from VLM.Lib.vortex_lattice_method_calculator import VortexLatticeMethodCalculator
from VLM.Lib.lifting_calculator import LiftingCalculator

class VLMController(QWidget):

    @staticmethod
    def VLMCalculator(AR, b, Lambda, nx, ny, air_density, V_inf, attack_angle , Oswald_coeff, is_flat_plate = True ,foil_coord = "" ):

        coordinate_matrix  = Discretizer.GridGeneratorSelector(AR,b,Lambda,nx,ny, is_flat_plate, foil_coord)
        AIC_matrix = VortexLatticeMethodCalculator.AICMatrixGenerator(coordinate_matrix)
        circulation_vector = VortexLatticeMethodCalculator.CirculationCalculator(AIC_matrix, V_inf, attack_angle)
        panel_span = 0.5 * b / ny
        total_lift = LiftingCalculator.TotalLifting(air_density, V_inf, circulation_vector, panel_span)
        surface = b**2 / AR
        CL = LiftingCalculator.LiftCoefficientCalculator(air_density, V_inf, surface, total_lift)


VLMController.VLMCalculator(5,1,45,1,4,1.225,30,3)
