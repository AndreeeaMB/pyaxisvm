# -*- coding: utf-8 -*-
from .core.wrap import AxisVMModelItem, AxisVMModelItems
from .core.utils import mtype2str

class IAxisVMMaterial(AxisVMModelItem):
    """Wrapper for the `IAxisVMMaterial` COM interface."""

    def _get_attrs(self):
        """Return the representation methods (internal helper)."""
        attrs = []
        NDN = self.NationalDesignName
        attrs.append(("Name", self.Name, "{}"))
        attrs.append(("NationalDesignName", self.NationalDesignName, "{}"))
        attrs.append(("MaterialDesignName", self.MaterialDesignName, "{}"))
        attrs.append(("MaterialType", mtype2str[self.MaterialType], "{}"))
        attrs.append(("UID", self._wrapped.UID, "{}"))
        
        mtype = self.MaterialType
        if mtype == 1:
            # steel
            if NDN == 'Eurcode':
                attrs.append(("Fu", self._wrapped.Fu, "{}"))
                attrs.append(("Fu40", self._wrapped.Fu40, "{}"))
                attrs.append(("Fy", self._wrapped.Fy, "{}"))
                attrs.append(("Fy40", self._wrapped.Fy40, "{}"))        
        return attrs


class IAxisVMMaterials(AxisVMModelItems):
    """Wrapper for the `IAxisVMMaterials` COM interface."""

    __itemcls__ = IAxisVMMaterial
    
    def _get_attrs(self):
        """Return the representation methods (internal helper)."""
        attrs = []
        attrs.append(("N Materials", self.Count, "{}"))
        return attrs