# -*- coding: utf-8 -*-
from collections import OrderedDict
import numpy as np

from .core.wrap import AxisVMModelItem, AxisVMModelItems
from .axsurface import SurfaceMixin


__all__ = ['IAxisVMNode', 'IAxisVMNodes']


class IAxisVMNode(AxisVMModelItem, SurfaceMixin):
    """Wrapper for the `IAxisVMNode` COM interface."""
    ...


class IAxisVMNodes(AxisVMModelItems, SurfaceMixin):
    """Wrapper for the `IAxisVMNodes` COM interface."""

    __itemcls__ = IAxisVMNode

    def get(self, *args, interactive=False, **kwargs):
        """
        Returns a list of nodes, which can be specified by keyword
        arguments. It can be used to turn an arbitrary specification
        of nodes in an embedded situation into a list of nodes.
        For that reason it includes trivial keys. Individual elements
        can be specified, but the result is always a list. If there are
        no valid specifiers, then
            (1) if argument 'all' is provided, all of the nodes of the
                model are returned
            (2) if interactive == True, function either gets the selected
                nodes from AxisVM, or if there is none, a selection \
                dialog shows up in AxisVM and the function is called again \
                with valid specifiers emerging from any of these scenarios.

        Parameters
        ----------
        Possible keys and values
        node : a single domain, returns [node]
        nodes : a list of nodes, returns nodes
        ID : int, a single nodeID
        IDs : [int], a sequence of nodeIDs
        UID : int, a single nodeUID
        UIDs : [int], a sequence of nodeUIDs

        Examples
        --------
        >>> nodes = get_nodes(Model,**kwargs)
        >>> nodes = get_nodes(Model)

        """
        Model = self.model
        nodes = None
        try:
            if 'node' in kwargs:
                nodes = [kwargs.pop('node')]
            elif 'nodes' in kwargs:
                nodes = kwargs.pop('nodes')
            elif 'ID' in kwargs:
                nodes = [Model.Nodes.GetNode(kwargs.pop('ID'))[0]]
            elif 'IDs' in kwargs:
                nodes = [Model.Nodes.GetNode(ID)[0]
                         for ID in kwargs.pop('IDs')]
            elif 'UID' in kwargs:
                ID = Model.Nodes.IndexOfUID(kwargs.pop('UID'))
                nodes = [Model.Nodes.GetNode(ID)[0]]
            elif 'UIDs' in kwargs:
                IDs = [Model.Nodes.IndexOfUID(UID)
                       for UID in kwargs.pop('UIDs')]
                nodes = [Model.Nodes.GetNode(ID)[0] for ID in IDs]
        except Exception:
            raise "Ivalid specification of nodes!"
        finally:
            if nodes is None:
                nodes = self.get_selected(interactive=interactive)
                if nodes is None and 'all' in args:
                    nNode = Model.Nodes.Count
                    nodeIDs = [i for i in range(1, nNode+1)]
                    nodes = self.get(IDs=nodeIDs, interactive=False)
            return nodes

    def select(self, clear=True, msg: str = None):
        """
        Shows up a selectiondialog for nodes in AxisVM and returns the selected
        nodes if succesful.
        """
        if msg is None:
            msg = 'Select one or more nodes!'
        deletecurrent = 1 if clear else 0
        self.model.StartModalSelection(msg, deletecurrent, 'seltNode')
        return self.get_selected(interactive=False)

    def get_selected(self, interactive=False, msg: str = None):
        """
        Returns a dictionary of nodes mapping nodeIDs to Nodes.
        """
        Model = self.model._wrapped
        try:
            nIDs = Model.Nodes.GetSelectedItemIds()[0]
            return [Model.Nodes.GetNode(nID)[0] for nID in nIDs]
        except Exception:
            if interactive:
                return self.select(clear=True, msg=msg)
            else:
                return None

    def get_IDs(self, *args, interactive=False, **kwargs):
        """
        Returns a list of integers, which can be specified by keyword
        arguments. It can be used to turn an arbitrary specification
        of nodeIDs in an embedded situation into a list of nodeIDs.
        For that reason it includes trivial keys. Individual elements
        can be specified, but the result is always a list. If there are
        no valid specifiers, the function either gets the selected nodes
        from AxisVM, or if there is none, a selection dialog shows up in
        AxisVM and the function is called again with valid specifiers
        emerging from any of these scenarios.
        
        Possible keys and values
            node : a single domain, returns [node]
            nodes : a list of nodes, returns nodes
            ID : int, a single nodeID
            IDs : [int], a sequence of nodeIDs
            UID : int, a single nodeUID
            UIDs : [int], a sequence of nodeUIDs
        
        For example
            nodeIDs = get_IDs(Model,**kwargs)
        or simply
            nodeIDs = get_IDs(Model)
        to get nodeIDs from a selection in AxisVM.
        """
        nodeIDs = None
        Model = self.model
        try:
            if 'node' in kwargs:
                n = kwargs['node']
                nodeIDs = [Model.Nodes.IndexOf(n.x, n.y, n.z, 1e-8, 1)]
            elif 'nodes' in kwargs:
                nodes = kwargs['nodes']
                nodeIDs = [Model.Nodes.IndexOf(
                    n.x, n.y, n.z, 1e-8, 1) for n in nodes]
            if 'ID' in kwargs:
                nodeIDs = [kwargs['ID']]
            elif 'nodeIDs' in kwargs:
                nodeIDs = kwargs['IDs']
            elif 'UID' in kwargs:
                nodeIDs = [Model.Nodes.IndexOfUID(kwargs['UID'])]
            elif 'UIDs' in kwargs:
                nodeIDs = [Model.Nodes.IndexOfUID(
                    UID) for UID in kwargs['UIDs']]
        except Exception:
            raise "Ivalid specification of nodeIDs!"
        finally:
            if nodeIDs is None:
                nodeIDs = self.get_selected_IDs(interactive=interactive)
                if nodeIDs is None and 'all' in args:
                    nNode = Model.Nodes.Count
                    nodeIDs = [i for i in range(1, nNode+1)]
            return nodeIDs

    def select_IDs(self, clear=True, msg: str = None):
        """
        Shows up a selectiondialog for nodes in AxisVM and returns the selected
        nodeIDs if succesful.
        """
        if msg is None:
            msg = 'Select one or more nodes!'
        Model = self.model
        deletecurrent = 1 if clear else 0
        Model.StartModalSelection(msg, deletecurrent, 'seltNode')
        return self.get_selected_IDs(interactive=False)

    def get_selected_IDs(self, interactive=False):
        """
        Returns a list of nodeIDs. The result is always iterable,
        even if it contains only one item.
        """
        Model = self.model
        try:
            return Model.Nodes.GetSelectedItemIds()[0]
        except Exception:
            if interactive:
                return self.select_IDs(msg='Select one or more nodes!')
            else:
                return None

    def get_connected_surfaceIDs(self, flatten=False, as_dict=False, **kwargs):
        """
        Returns surfaces connected by the specified nodes. For the details of
        specification of nodes see the documentation of function : get_IDs.
        If as_dict == True, result is a dictionary that maps nodeIDs to lists
        of surfaceIDs.
        """
        Model = self.model
        nodeIDs = self.get_IDs(**kwargs)
        assert nodeIDs is not None, "Invalid specification of nodes!"
        if as_dict:
            return OrderedDict({nID: Model.Nodes.GetConnectedSurfaces(nID)[0]
                                for nID in nodeIDs})
        if flatten:
            surfaces = set()
            for nID in nodeIDs:
                surfaces.update(Model.Nodes.GetConnectedSurfaces(nID)[0])
            return list(surfaces)
        return [Model.Nodes.GetConnectedSurfaces(nID)[0] for nID in nodeIDs]
