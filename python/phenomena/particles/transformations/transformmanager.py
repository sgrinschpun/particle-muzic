from operator import itemgetter

from phenomena.particles.transformations.types import ComptonEffect, PairProduction, Annihilation, InelasticCollision, Decay2, ElasticCollision


###the model needs to define the available transformations
TRANSFORMATIONS = [ComptonEffect, PairProduction, Annihilation, InelasticCollision, Decay2, ElasticCollision]



class TransformManager(object):

    def __init__(self, particle):
        #self._transformations = particle.__class__.TRANSFORMATIONS
        self._build_allTransformations(particle)
        self._select_transformation()

    @property
    def allTransformations(self):
        return self._allTransformations

    @property
    def selectedTransformationValues(self):
        return self._selTransfValues

    @property
    def selectedTransformationType(self):
        return self._selTransfType


    def _build_allTransformations(self, particle):
        '''
        For each transformation possible for the particle, select the transformation channel and calculate the time of transformation. Store in a list
        self._allTransformations =
        [
            {
                'type': 'decay',
                'list': ['part1','part2'],
                'time': xxx
            },
            {
                'type': 'elastic',
                'list': ['part4','part5'],
                'time': xxx
            },
            ...
        ]
        '''
        allTransformations = []
        for transf in TRANSFORMATIONS:
        #for transf in self._transformations:
            item = transf(particle).values
            if item != {}:
                allTransformations.append(item)

        self._allTransformations = allTransformations

    def _select_transformation(self):
        '''
        From all the possible transformations, choose the one that happens first. For this one calculate the transformation values.
        self._selectedTransformation =
        [
            {
                'name':
                'p':
                'phi':
                'theta':
                'E':
            },
            ...
        }]
        '''
        #selTransf = sorted(self._allTransformations, key=itemgetter('time'),reverse=True)[0]
        #self._selTransfType = selTransf['type']
        #self._selTransfValues = TransformCalc.getValues(selTransf)
        self._selTransfValues = 1
