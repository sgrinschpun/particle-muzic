from __future__ import division
import math, random

class CMcalc(object):
    @staticmethod
    def E(m0, m1, m2):
        E1 = (math.pow(m0,2)+math.pow(m1,2)-math.pow(m2,2))/(2*m0)
        E2 = (math.pow(m0,2)-math.pow(m1,2)+math.pow(m2,2))/(2*m0)
        return [E1,E2]

    @staticmethod
    def p(m0, m1, m2):
        num1 = math.pow(m0,2)-math.pow(m1-m2,2)
        num2 = math.pow(m0,2)-math.pow(m1+m2,2)
        p = math.sqrt(num1*num2)/(2*m0)
        return [p,p]

    @staticmethod
    def pxy(m0,m1,m2,theta_cm):
        px = CMcalc.p(m0,m1,m2)[0]*math.cos(theta_cm)
        py = CMcalc.p(m0,m1,m2)[0]*math.sin(theta_cm)
        return [{'x':px,'y':py},{'x':-px,'y':-py}]

    #@staticmethod
    #def theta():
    #    angle = math.pi * random.random()
    #    return (angle,-angle)

class LABcalc(object):
    @staticmethod
    def beta_from_gamma(gamma):
        return math.sqrt(1-1/math.pow(gamma,2))

    @staticmethod
    def pxy(m0,m1,m2,theta_cm,gamma):
        beta = LABcalc.beta_from_gamma(gamma)
        CMpxy = CMcalc.pxy(m0,m1,m2,theta_cm)
        CME = CMcalc.E(m0,m1,m2)
        return [
            {
            'x':gamma*(CMpxy[0]['x']+ beta*CME[0]),
            'y':CMpxy[0]['y']
            },
            {
            'x':gamma*(CMpxy[1]['x']+ beta*CME[1]),
            'y':CMpxy[1]['y']
            }
        ]

    @staticmethod
    def p(m0,m1,m2,theta_cm,gamma):
        pxy = LABcalc.pxy(m0,m1,m2,theta_cm,gamma)
        return [math.sqrt(pxy[0]['x']**2+pxy[0]['y']**2),math.sqrt(pxy[1]['x']**2+pxy[1]['y']**2)]

    @staticmethod
    def boostedTheta(m0,m1,m2,theta_cm,gamma):
        ttheta0 = LABcalc.pxy(m0,m1,m2,theta_cm,gamma)[0]['y']/LABcalc.pxy(m0,m1,m2,theta_cm,gamma)[0]['x']
        ttheta1 = LABcalc.pxy(m0,m1,m2,theta_cm,gamma)[1]['y']/LABcalc.pxy(m0,m1,m2,theta_cm,gamma)[1]['x']
        return [math.atan(ttheta0),math.atan(ttheta1)]
