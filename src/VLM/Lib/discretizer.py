import numpy as np
import math

class Discretizer(object):

    @staticmethod
    def GridGeneratorSelector(AR,b,Lambda,nx,ny, is_flat_plate = True ,foil_coord = ""):

        if(is_flat_plate):
            return Discretizer.GridGeneratorFlatPlate(AR,b,Lambda,nx,ny)
        else:
            return Discretizer.GridGeneratorFoil(AR,b,Lambda,nx,ny,foil_coord)

    @staticmethod
    def GridGeneratorFlatPlate(AR,b,Lambda,nx,ny):

        panel_width = 0.5 * b / ny
        panel_height = b / (AR * nx)
        Lambda = Lambda * math.pi / 180

        y_m = - panel_width / 2
        y_n1 = - panel_width
        y_n2 = 0
        count = 1
        array = []

        for i in range(nx):
            x_m0 = i * panel_height + 3 * panel_height / 4
            x_n0 = i * panel_height + panel_height / 4
            for j in range(ny):
                data_panel = []
                data_panel.append(count)
                y_m = y_m + panel_width
                x_m = x_m0 + y_m * math.tan(Lambda)
                y_n1 = y_n1 + panel_width
                x_n1 = x_n0 + y_n1 * math.tan(Lambda)
                y_n2 = y_n2 + panel_width
                x_n2 = x_n0 + y_n2*math.tan(Lambda)
                data_panel.append(x_m)
                data_panel.append(y_m)
                data_panel.append(x_n1)
                data_panel.append(y_n1)
                data_panel.append(x_n2)
                data_panel.append(y_n2)
                count = count + 1
                array.append(data_panel)

            y_m = - panel_width / 2
            y_n1 = - panel_width
            y_n2 = 0

        matrix = np.array(array)
        return matrix

    @staticmethod
    def GridGeneratorFoil(AR,b,Lambda,nx,ny,foil_coord):
        return 0




