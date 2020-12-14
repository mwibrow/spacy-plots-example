"""
*Very* simple/opinionated plotter
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
from typing import List

import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import numpy as np

plt.style.use('ggplot')

class Plotter:
    
    def __init__(self, ylabels: List[str] = None, title=None, iterations: int = 1, **kwargs):
        self.ylabels = ylabels or ['']
        self.iterations = iterations
        self.nplots = len(self.ylabels)

        fig, axs = plt.subplots(nrows=self.nplots, ncols=1, sharex=True, **kwargs)
        fig.suptitle(title)
        self.fig = fig
        self.axs = np.atleast_2d(axs)
        
        self.x = []
        self.y = [[] for _ in range(self.nplots)]
        
        plt.subplots_adjust(hspace=0.1)
        plt.ion()
        plt.show()

        self.open = True
        fig.canvas.mpl_connect("close_event", self._handle_close)

        self.plot()
        plt.pause(0.1)
    
    def _handle_close(self, _evt):
        self.open = False

    def plot(self):
        """Draw the plot."""
        for i, ax in enumerate(self.fig.axes):
            ax.clear()
            ax.set_xlim(1, self.iterations)
            ax.xaxis.set_major_locator(MaxNLocator(integer=True))
            ax.plot(self.x, self.y[i])
            ax.set_ylabel(self.ylabels[i])
        
        self.fig.axes[-1].set_xlabel('Iterations')
        self.fig.canvas.draw()
        plt.pause(0.1)
        
    def update(self, y: List[float] = None, x: int = None):
        """Update the plot."""
        if x is not None:
            self.x.append(x)
        else:
            if self.x:
                self.x.append(self.x[-1] + 1)
            else:
                self.x = [1]
        if y is not None:
            y = np.atleast_1d(y)
            for i, val in enumerate(y):
                self.y[i].append(val)
            
        self.plot()

    def keep(self):
        """Keep the plot window open until it is closed."""
        while self.open:
            plt.pause(1.0)

