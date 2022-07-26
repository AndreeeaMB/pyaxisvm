# -*- coding: utf-8 -*-
from PIL import ImageGrab

from .core.wrap import AxisVMModelItem, AxisVMModelItems


class IAxisVMWindow(AxisVMModelItem):
    """Wrapper for the `IAxisVMWindow` COM interface."""

    def screenshot(self, EWindowColourMode=0, maxtry=10):
        self._wrapped.SaveWindowToClipBoard(EWindowColourMode)
        c, im = 0, None
        while c < maxtry:
            try:
                c += 1
                im = ImageGrab.grabclipboard()
                break
            except Exception:
                pass
        if im is not None:
            return im
        raise RuntimeError(
            "Failed to take screenshot due to unknown system error.")


class IAxisVMWindows(AxisVMModelItems):
    """Wrapper for the `IAxisVMWindows` COM interface."""

    __itemcls__ = IAxisVMWindow
