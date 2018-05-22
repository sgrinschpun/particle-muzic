from mappings_available import ConstMapping, MirrorMapping
from phenomena.particles.particle import Particle, BasicParticle


class MappingsController:

    def __init__(self):
        self._map_dictionary = {"charge": ConstMapping(),
                               "mass": ConstMapping(),
                               "decay_time": ConstMapping(),
                               "composition": MirrorMapping()}

    def translateParticle(self, particle):
        assert issubclass(type(particle), Particle)
        translated_values = {'name': particle}
        for characteristic, mapping in self._map_dictionary:
            original_value = getattr(particle, characteristic)
            translated_value = mapping.translateValue(original_value)
            translated_values[characteristic] = translated_value
        translated_particle = BasicParticle(**translated_values)
        return translated_particle