from PyFlow.Core import NodeBase
from PyFlow.Core.NodeBase import NodePinsSuggestionsHelper
from PyFlow.Core.Common import *
import numpy as np
import logging


class DemoNode(NodeBase):
    def __init__(self, name):
        super(DemoNode, self).__init__(name)
        self.inp = self.createInputPin('inp', 'BoolPin')
        self.out = self.createOutputPin('out', 'BoolPin')

    @staticmethod
    def pinTypeHints():
        helper = NodePinsSuggestionsHelper()
        helper.addInputDataType('BoolPin')
        helper.addOutputDataType('BoolPin')
        helper.addInputStruct(StructureType.Single)
        helper.addOutputStruct(StructureType.Single)
        return helper

    @staticmethod
    def category():
        return 'demo1'

    @staticmethod
    def keywords():
        return []

    @staticmethod
    def description():
        return "Description in rst format."

    def compute(self, *args, **kwargs):
        inputData = self.inp.getData()
        self.out.setData(not inputData)

class VertifyNode(NodeBase):
    def __init__(self, name):
        super(VertifyNode, self).__init__(name)
        # self.inp = self.createInputPin('inp', 'BoolPin')
        # self.out = self.createOutputPin('out', 'BoolPin')
        self.inp = self.createInputPin('inp', 'NumpyDataPin')
        self.out = self.createOutputPin('out', 'NumpyDataPin')

    @staticmethod
    def category():
        return 'Vertify'

    @staticmethod
    def keywords():
        return []

    @staticmethod
    def description():
        return "Insitu vertify Node"
    
    def compute(self, *args, **kwargs):
        inputData = self.inp.getData()
        self.out.setData(inputData)

class NumpyExampleNode(NodeBase):
    def __init__(self, name):
        super(NumpyExampleNode, self).__init__(name)


class ConduitExampleNode(NodeBase):
    def __init__(self, name):
        super(ConduitExampleNode, self).__init__(name)

class SourceNode(NodeBase):
    def __init__(self, name):
        super(SourceNode, self).__init__(name)
        # self.inp = self.createInputPin('inp', 'BoolPin')
        # self.out = self.createOutputPin('out', 'BoolPin')
        # self.inp1 = self.createInputPin('inp1', 'NumpyDataPin')
        self.out = self.createOutputPin('out', 'NumpyDataPin')

    @staticmethod
    def category():
        return 'Source'

    @staticmethod
    def keywords():
        return []

    @staticmethod
    def description():
        return "Insitu Source Node"
    
    def compute(self, *args, **kwargs):
        self.out.setData(np.array([1,2,3]))

class OutPutNode(NodeBase):
    def __init__(self, name):
        super(OutPutNode, self).__init__(name)
        self.inExec = self.createInputPin(DEFAULT_IN_EXEC_NAME, 'ExecPin', None, self.compute)
        self.inp = self.createInputPin('inp', 'NumpyDataPin')

    @staticmethod
    def category():
        return 'Output'

    @staticmethod
    def keywords():
        return []

    @staticmethod
    def description():
        return "Insitu Source Node"
    
    def compute(self, *args, **kwargs):
        print(self.inp.getData().data)

class NumpyExampleNode(NodeBase):
    def __init__(self, name):
        super(NumpyExampleNode, self).__init__(name)


class ConduitExampleNode(NodeBase):
    def __init__(self, name):
        super(ConduitExampleNode, self).__init__(name)
