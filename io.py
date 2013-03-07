def read(filename, delimiter = ' '):
    import csv
    import numpy as np
    with open(filename) as dat:
        rdr = csv.reader(dat, delimiter = ' ')
        data = []
        for row in rdr:
            data.append([float(i.strip()) for i in row])
        return np.array(data)
