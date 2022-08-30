# -*- coding: utf-8 -*-
import awkward as ak
import pandas as pd


class AxisVMAttributes(dict):
    
    def to_pandas(self, nested=False) -> pd.DataFrame:
        return pd.DataFrame.from_dict(self)

    def to_awkward(self, nested=False) -> ak.Record:
        return ak.Record(self)
    

def squeeze_attributes(d):
    return AxisVMAttributes({i : v[0] for i,v in d.items()})