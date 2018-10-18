from operator import itemgetter

###the model needs to define the available transformations

class TransformManager(object):

    def __init__(self, particle):
        _build_allTransformations(particle)
        _select_transformation()

    @property
    def selectedTransformationValues(self):
        return self._selTransfValues

    @property
    def selectedTransformationType(self):
        return self._selTransfType


    def _build_allTransformations():
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
        for transf in LISTOFTRANSFORMATIONS:
            allTransformations.append(transf(particle))

        self._allTransformations = allTransformations

    def _select_transformation():
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
        selTransf = sorted(self._allTransformations, key=itemgetter('time'),reverse=True)[0]
        self._selTransfType = selTransf['type']
        self._selTransfValues = TransformCalc.getValues(selTransf)
