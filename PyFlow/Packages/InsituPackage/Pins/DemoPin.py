from PyFlow.Core import PinBase
from PyFlow.Core.Common import *
import numpy as np
import json

class FakeTypeZPKEI(object):
    """docstring for FakeTypeZPKEI"""
    def __init__(self, value=None):
        super(FakeTypeZPKEI, self).__init__()
        self.value = value

class NoneDecoder(json.JSONDecoder):
    def __init__(self, *args, **kwargs):
        super(NoneDecoder, self).__init__(object_hook=self.object_hook, *args, **kwargs)

    def object_hook(self, vec3Dict):
        return None

class NoneEncoder(json.JSONEncoder):
    def default(self, vec3):
        return None

class DemoPin(PinBase):
    """doc string for DemoPin"""
    def __init__(self, name, parent, direction, **kwargs):
        super(DemoPin, self).__init__(name, parent, direction, **kwargs)
        self.setDefaultValue(False)

    @staticmethod
    def IsValuePin():
        return True

    @staticmethod
    def supportedDataTypes():
        return ('DemoPin',)

    @staticmethod
    def pinDataTypeHint():
        return 'DemoPin', False

    @staticmethod
    def color():
        return (200, 200, 50, 255)

    @staticmethod
    def internalDataStructure():
        return FakeTypeZPKEI

    @staticmethod
    def processData(data):
        return DemoPin.internalDataStructure()(data)



class NumpyData():
    def __init__(self, data=None):
        if isinstance(data, NumpyData):
            self.data=data.data
        elif isinstance(data, np.ndarray):
            self.data= data
        elif data:
            self.data= data
        else:
            self.data= None


class NumpyDataPin(PinBase):
    """doc string for NumpyDataPin"""

    def __init__(self, name, parent, direction, **kwargs):
        super(NumpyDataPin, self).__init__(name, parent, direction, **kwargs)
        self.setDefaultValue(NumpyData())
        self.disableOptions(PinOptions.Storable)

    @staticmethod
    def jsonEncoderClass():
        return NoneEncoder

    @staticmethod
    def jsonDecoderClass():
        return NoneDecoder

    @staticmethod
    def IsValuePin():
        return True

    @staticmethod
    def supportedDataTypes():
        return ('NumpyDataPin',)

    @staticmethod
    def pinDataTypeHint():
        return 'NumpyDataPin', NumpyData()

    @staticmethod
    def color():
        return (200, 200, 50, 255)

    @staticmethod
    def internalDataStructure():
        return NumpyData

    @staticmethod
    def processData(data):
        return NumpyDataPin.internalDataStructure()(data)