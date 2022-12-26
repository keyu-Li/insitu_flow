PACKAGE_NAME = 'InsituPackage'

from collections import OrderedDict
from PyFlow.UI.UIInterfaces import IPackage

# Pins
from PyFlow.Packages.InsituPackage.Pins.DemoPin import DemoPin
from PyFlow.Packages.InsituPackage.Pins.DemoPin import NumpyDataPin

# Function based nodes
from PyFlow.Packages.InsituPackage.FunctionLibraries.DemoLib import DemoLib

# Class based nodes
from PyFlow.Packages.InsituPackage.Nodes.DemoNode import DemoNode
from PyFlow.Packages.InsituPackage.Nodes.DemoNode import VertifyNode
from PyFlow.Packages.InsituPackage.Nodes.DemoNode import SourceNode
from PyFlow.Packages.InsituPackage.Nodes.DemoNode import OutPutNode
# Tools
from PyFlow.Packages.InsituPackage.Tools.DemoShelfTool import DemoShelfTool
from PyFlow.Packages.InsituPackage.Tools.DemoDockTool import DemoDockTool

# Exporters
from PyFlow.Packages.InsituPackage.Exporters.DemoExporter import DemoExporter

# Factories
from PyFlow.Packages.InsituPackage.Factories.UIPinFactory import createUIPin
from PyFlow.Packages.InsituPackage.Factories.UINodeFactory import createUINode
from PyFlow.Packages.InsituPackage.Factories.PinInputWidgetFactory import getInputWidget
# Prefs widgets
from PyFlow.Packages.InsituPackage.PrefsWidgets.DemoPrefs import DemoPrefs

_FOO_LIBS = {}
_NODES = {}
_PINS = {}
_TOOLS = OrderedDict()
_PREFS_WIDGETS = OrderedDict()
_EXPORTERS = OrderedDict()

_FOO_LIBS[DemoLib.__name__] = DemoLib(PACKAGE_NAME)

#_NODES[DemoNode.__name__] = DemoNode
_NODES = {
	DemoNode.__name__: DemoNode,
	VertifyNode.__name__: VertifyNode,
	SourceNode.__name__: SourceNode,
	OutPutNode.__name__: OutPutNode,
}
#
# _PINS[DemoPin.__name__] = DemoPin
#
_PINS = {
    DemoPin.__name__: DemoPin,
	NumpyDataPin.__name__: NumpyDataPin
}

_TOOLS[DemoShelfTool.__name__] = DemoShelfTool
_TOOLS[DemoDockTool.__name__] = DemoDockTool

_EXPORTERS[DemoExporter.__name__] = DemoExporter

_PREFS_WIDGETS["Demo"] = DemoPrefs


class InsituPackage(IPackage):
	def __init__(self):
		super(InsituPackage, self).__init__()

	@staticmethod
	def GetExporters():
		return _EXPORTERS

	@staticmethod
	def GetFunctionLibraries():
		return _FOO_LIBS

	@staticmethod
	def GetNodeClasses():
		return _NODES

	@staticmethod
	def GetPinClasses():
		return _PINS

	@staticmethod
	def GetToolClasses():
		return _TOOLS

	@staticmethod
	def UIPinsFactory():
		return createUIPin

	@staticmethod
	def UINodesFactory():
		return createUINode

	@staticmethod
	def PinsInputWidgetFactory():
		return getInputWidget

	@staticmethod
	def PrefsWidgets():
		return _PREFS_WIDGETS

