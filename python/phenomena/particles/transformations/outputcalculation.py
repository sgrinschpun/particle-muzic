from phenomena.particles.transformations.kinematics import DecayCalculations, InelasticCalculations, ElasticCalculations

class TransCalculation(object):

    def __init__(self, particle, type):
        if type in ['ComptonEffect', 'ElasticCollisionWithProton', 'ElasticCollisionWithElectron', 'ElasticCollisionWithNeutron']:
            self._buildElasticValues(particle)
        elif type in ['PairProduction', 'Annihilation', 'InelasticCollisionWithProton', 'InelasticCollisionWithNeutron']:
            self._buildInelasticValues(particle)
        elif type in ['Decay2']:
            self._buildDecayValues(particle)

    def _buildElasticValues(self, particle):
        self._outputValues = ElasticCalculations(particle.fourMomentum, particle.transformation.target, particle.transformation.selectedChannel).getValues()

    def _buildInelasticValues(self, particle):
        self._outputValues = InelasticCalculations(particle.fourMomentum, particle.transformation.target, particle.transformation.selectedChannel).getValues()

    def _buildDecayValues(self, particle):
        self._outputValues = DecayCalculations(particle.fourMomentum, particle.transformation.selectedChannel).getValues()

    def getOutputValues(self):
        return self._outputValues
