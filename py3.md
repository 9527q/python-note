
# pandas


```python
import pandas as pd
import numpy as np
```


```python
df = pd.DataFrame(pd.read_csv('query.csv', header=0))
df = pd.DataFrame(pd.read_excel('query.csv'))
```


    ---------------------------------------------------------------------------

    XLRDError                                 Traceback (most recent call last)

    <ipython-input-6-58c79e843c6b> in <module>
          1 df = pd.DataFrame(pd.read_csv('query.csv', header=0))
    ----> 2 df = pd.DataFrame(pd.read_excel('query.csv'))
    

    ~/appli/anaconda3/lib/python3.6/site-packages/pandas/util/_decorators.py in wrapper(*args, **kwargs)
        176                 else:
        177                     kwargs[new_arg_name] = new_arg_value
    --> 178             return func(*args, **kwargs)
        179         return wrapper
        180     return _deprecate_kwarg


    ~/appli/anaconda3/lib/python3.6/site-packages/pandas/util/_decorators.py in wrapper(*args, **kwargs)
        176                 else:
        177                     kwargs[new_arg_name] = new_arg_value
    --> 178             return func(*args, **kwargs)
        179         return wrapper
        180     return _deprecate_kwarg


    ~/appli/anaconda3/lib/python3.6/site-packages/pandas/io/excel.py in read_excel(io, sheet_name, header, names, index_col, usecols, squeeze, dtype, engine, converters, true_values, false_values, skiprows, nrows, na_values, parse_dates, date_parser, thousands, comment, skipfooter, convert_float, **kwds)
        305 
        306     if not isinstance(io, ExcelFile):
    --> 307         io = ExcelFile(io, engine=engine)
        308 
        309     return io.parse(


    ~/appli/anaconda3/lib/python3.6/site-packages/pandas/io/excel.py in __init__(self, io, **kwds)
        392             self.book = xlrd.open_workbook(file_contents=data)
        393         elif isinstance(self._io, compat.string_types):
    --> 394             self.book = xlrd.open_workbook(self._io)
        395         else:
        396             raise ValueError('Must explicitly set engine if not passing in'


    ~/appli/anaconda3/lib/python3.6/site-packages/xlrd/__init__.py in open_workbook(filename, logfile, verbosity, use_mmap, file_contents, encoding_override, formatting_info, on_demand, ragged_rows)
        155         formatting_info=formatting_info,
        156         on_demand=on_demand,
    --> 157         ragged_rows=ragged_rows,
        158     )
        159     return bk


    ~/appli/anaconda3/lib/python3.6/site-packages/xlrd/book.py in open_workbook_xls(filename, logfile, verbosity, use_mmap, file_contents, encoding_override, formatting_info, on_demand, ragged_rows)
         90         t1 = perf_counter()
         91         bk.load_time_stage_1 = t1 - t0
    ---> 92         biff_version = bk.getbof(XL_WORKBOOK_GLOBALS)
         93         if not biff_version:
         94             raise XLRDError("Can't determine file's BIFF version")


    ~/appli/anaconda3/lib/python3.6/site-packages/xlrd/book.py in getbof(self, rqd_stream)
       1276             bof_error('Expected BOF record; met end of file')
       1277         if opcode not in bofcodes:
    -> 1278             bof_error('Expected BOF record; found %r' % self.mem[savpos:savpos+8])
       1279         length = self.get2bytes()
       1280         if length == MY_EOF:


    ~/appli/anaconda3/lib/python3.6/site-packages/xlrd/book.py in bof_error(msg)
       1270 
       1271         def bof_error(msg):
    -> 1272             raise XLRDError('Unsupported format, or corrupt file: ' + msg)
       1273         savpos = self._position
       1274         opcode = self.get2bytes()


    XLRDError: Unsupported format, or corrupt file: Expected BOF record; found b'event_da'



```python
type(pd.read_csv('query.csv', header=0))
```




    pandas.core.frame.DataFrame




```python

```
