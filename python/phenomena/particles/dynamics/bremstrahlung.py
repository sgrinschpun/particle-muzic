from skhep.math.vectors import Vector3D
from skhep.constants import c_light
from fields import Fields

class Bforce(object):

    @staticmethod
    def Bforce(B,velocity,charge):
        return charge * velocity.cross(B)

    def _set_B_force(self):
        self.F = self.charge * self.vel.cross(field().B)
