from wellcad.com._log import Log
import numpy as np


class LogData(np.ndarray):
    def __new__(cls, data_table: Log.data_table):
        obj = np.asarray(data_table[1:][1:]).view(cls)
        obj.column_labels = np.array(data_table[0][1:], dtype=str)
        obj.depth_or_time = np.array(data_table[1:][0], dtype=float)
        return obj

    def __array_finalize__(self, obj):
        if obj is None: return
        self.column_labels = getattr(obj, 'column_labels', None)
        self.depth_or_time = getattr(obj, 'depth_or_time', None)
