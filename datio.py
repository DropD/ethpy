def read(filename, delimiter = ' '):
    '''
    reads space separated data files into a 2D numpy array.
    takes filename and optionally a delimiter.
    '''
    import csv
    import numpy as np
    with open(filename) as dat:
        rdr = csv.reader(dat, delimiter = ' ')
        data = []
        for row in rdr:
            data.append([float(i.strip()) for i in row])
        return np.array(data)
