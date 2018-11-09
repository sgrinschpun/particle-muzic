from skhep.math.vectors import Vector3D

class Fields(object):

    def __init__(self, B=Field(Vector3D(0,0,1)), E=Field(Vector3D(0,0,0))):
        self._B = B
        self._E = E

    @property
    def B(self):
        return self._B.vector

    @B.setter
    def B(self, B):
        self._B = B

    @property
    def Bforce(self,velocity,charge):
        return charge * velocity.cross(self.B)

    @property
    def E(self):
        return self._E.vector

    @E.setter
    def E(self, E):
        self._E = E

    @property
    def Eforce(self,charge):
        return charge*self.E

class Field(object):

    def __init__(self, vector):
        self._vector = vector

    @property
    def vector(self):
        pass
