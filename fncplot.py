import matplotlib.pyplot as plt

class fncplot(object):
    '''
    plotting utilities for generating FNC style plots.
     - xlabel: (static) alias to pyplot.xlabel
     - ylabel: (static) places the y label on top of the y axis 
               in horizontal rotation using pyplot.text
    '''
    @staticmethod
    def xlabel(*args, **kwargs):
        plt.xlabel(*args, **kwargs)

    @staticmethod
    def ylabel(*args, **kwargs):
        subplot = plt.gcf().get_axes()
        kwargs['transform'] = subplot[0].transAxes
        plt.text(0, 1.04, *args, **kwargs)
