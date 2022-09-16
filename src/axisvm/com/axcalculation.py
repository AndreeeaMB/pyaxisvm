# -*- coding: utf-8 -*-
from .core.wrap import AxisVMModelItems


__all__ = ['IAxisVMCalculation']


class IAxisVMCalculation(AxisVMModelItems):
    """Wrapper for the `IAxisVMCalculation` COM interface."""

    def LinearAnalysis(self, *args, interact=False, show=False, autocorrect=True):
        if len(args) > 0 and isinstance(args[0], int):
            itype = args[0]
        else:
            import axisvm.com.tlb as axtlb
            if interact:
                itype = axtlb.cuiUserInteraction
            else:
                if show and autocorrect:
                    itype = axtlb.cuiNoUserInteractionWithAutoCorrect
                elif not show and autocorrect:
                    itype = axtlb.cuiNoUserInteractionWithoutAutoCorrect
                elif not show and autocorrect:
                    itype = axtlb.cuiNoUserInteractionWithAutoCorrectNoShow
                elif not show and not autocorrect:
                    itype = axtlb.cuiNoUserInteractionWithoutAutoCorrectNoShow
                else:
                    raise NotImplementedError
        return self._wrapped.LinearAnalysis(itype)