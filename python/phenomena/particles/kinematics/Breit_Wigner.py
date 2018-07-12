from __future__ import division, print_function
import math, random

import numpy as np
from scipy.stats import rv_continuous

class nonrel_breit_wigner_gen(rv_continuous):

# Nonrelativistic Breit-Wigner distribution for a particle
# given his math and his width.

    def _pdf(self, m, mass, width):

        k = 1/(np.pi/2.+np.arctan(mass/width))

        return k*width/((m-mass)**2+width**2)

    def _cdf(self, m, mass, width):

        k = 1/(np.pi/2.+np.arctan(mass/width))
        cdf=k*(np.arctan((m-mass)/width)+np.arctan(mass/width))

        return cdf

class rel_breit_wigner_gen(rv_continuous):

# Nonrelativistic Breit-Wigner distribution for a particle
# given his math and his width.

    def _argcheck(self, mass, width):
        return (mass > 0) & (width > 0)

    def _pdf(self, m, mass, width):

        alpha_ = width / mass
        gamma_ = mass**2 * (1. + alpha_**2)**0.5
        k = 2.**(3. / 2.) * mass**2 * alpha_ * gamma_ / (np.pi * (mass**2 + gamma_)**0.5)

        return k / ((m**2 - mass**2)**2 + mass**4 * alpha_**2)

    def _cdf(self, m, mass, width):

        alpha_ = width / mass
        gamma_ = mass**2 * (1. + alpha_**2)**0.5
        k = 2.**(3. / 2.) * mass**2 * alpha_ * gamma_ / (np.pi * (mass**2 + gamma_)**0.5)

        arg_1 = complex(-1)**(1. / 4.) / (-1j + alpha_)**0.5 * m / mass
        arg_2 = complex(-1)**(3. / 4.) / (1j + alpha_)**0.5 * m / mass

        shape_ = -1j * np.arctan(arg_1) / (-1j + alpha_)**0.5 - np.arctan(arg_2) / (1j + alpha_)**0.5
        norm_ = complex(-1)**(1. / 4.) * k / (2. * alpha_ * mass**3)

        cdf_ = norm_ * shape_
        cdf_ = cdf_.real

        return cdf_

# If one wants to randomly generate numbers that follow these distributions,
# use the rvs method of the SciPy class rv_continuous. For more detail, see
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.rv_continuous.html
