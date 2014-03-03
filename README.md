ETHPy
=====

Python package with utilities I often used at ETHZ.

modules:
    * datio: read space separated data files
    * fncplot: create plots conforming to standards of the course "How to Write Fast Numerical Code".
    
# usage

## datio
By giving datio.read a delimiter char you can also make it read data files with other delimiters than space.

myarray = datio.read( <filename> [, delimiter = <delimiter> ] )

Examples:

```python
from ethpy import datio

my_array = datio.read('my_space_delim_data.dat') # reads space delimited floats
my_other_array = datio.read('my_tab_delim_data.dat', delimiter = '\t') # reads tab delimited floats
```

## fncplot

The functions xlabel, ylabel and title behave the same as the pyplot equivalents in terms of inputs, except the ylabel takes an optional offset parameter to tune the output.
This might be necessary if you have fractions in the y label which you want to pretty print matplotlib style.

Examples:

```python
import matplotlib.pyplot as plt
from ethpy import datio as dio
from ethpy import fncplot as fpl

data = dio.read('results.dat') # read your data (optional)

x = data[:,0]
y = data[:,1]

# plot for the fnc course
plt.plot(x, y, ...) # plot your data using pyplot
...
fpl.xlabel('x Axis [units]') # use exactly as you would plt.xlabel
fpl.ylabel('y Axis [units]') # optionally give keyword argument 'offset' if the label is too close to the axis system.
fpl.title('Amazing Speedup :P')
...
plt.save(...)
```
