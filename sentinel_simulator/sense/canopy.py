"""
Specification of canopies
"""

class Canopy(object):
    def __init__(self, **kwargs):
        self.d = kwargs.get('d', None)
        self._check()

    def _check(self):
        assert self.d is not None, 'Vegetation height needs to be given'



class OneLayer(Canopy):
    """Define a homogeneous one layer canopy
    """
    def __init__(self, **kwargs):
        """Initiate with chosen key word arguments.

        :param kwargs: extinction coefficient, canopy height, specular reflectivity, etc.
        :return: Instance of OneLayer Canopy sub-class.
        :rtype: object
        """
        super(OneLayer, self).__init__(**kwargs)
        self.ke_h = kwargs.get('ke_h', None)
        self.ke_v = kwargs.get('ke_v', None)
        assert self.ke_h is not None
        assert self.ke_v is not None
        self.ks_h = kwargs.get('ks_h', None)
        self.ks_v = kwargs.get('ks_v', None)
        assert self.ks_h is not None
        assert self.ks_v is not None
