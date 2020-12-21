"""
*Very* simple/opinionated plotter
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
# pylint: disable=unsubscriptable-object
from typing import Dict, List, Union

import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import numpy as np

plt.style.use('ggplot')

class Plotter:
    
    """
    lines = [
        ["Train-loss", "Dev-loss"],
        ["Precission", "Recall", "F-score"]
    ]
    """
    def __init__(
            self, 
            plots: Union[List[str], Dict[str, List[str]]],
            title: str = None, 
            iterations: int = 1, 
            **kwargs):
        if isinstance(plots, list):
            plots = {plot: [''] for plot in plots}
        self.plots = plots 
        self.ylabels = list(plots.keys())
        self.nplots = len(self.plots)
        
        self.iterations = iterations
        fig, axs = plt.subplots(nrows=self.nplots, ncols=1, sharex=True, **kwargs)
        fig.suptitle(title)
        self.fig = fig
        self.axs = np.atleast_2d(axs)
        
        self.x = []
        
        self.y = {plot: [] for plot in self.plots}
        for plot in self.plots:
            self.y[plot].extend(([] for _ in self.plots[plot]))
        
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

            ylabel = self.ylabels[i]
            plot = self.plots[ylabel]
            for j, label in enumerate(plot):
                ax.plot(self.x, self.y[ylabel][j], label=label)
           
            ax.legend()
            ax.set_ylabel(self.ylabels[i])

        self.fig.axes[-1].set_xlabel('Iterations')
        self.fig.canvas.draw()
        plt.pause(0.1)
        
    def update(self, y: Union[List[float], Dict[str, List[float]]] = None, x: int = None):
        """Update the plot."""
        if x is not None:
            self.x.append(x)
        else:
            if self.x:
                self.x.append(self.x[-1] + 1)
            else:
                self.x = [1]
        if y is not None:
            
            if isinstance(y, list):
                y = {self.ylabels[i]: y[i] for i in range(len(y))}

            for i, ylabel in enumerate(self.ylabels):
                for j in range(len(self.plots[ylabel])):
                    self.y[ylabel][j].append(y[ylabel][j])
            
        self.plot()

    def keep(self):
        """Keep the plot window open until it is closed."""
        while self.open:
            plt.pause(1.0)
