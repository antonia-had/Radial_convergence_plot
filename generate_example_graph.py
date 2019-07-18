import numpy as np
from graph import drawgraphs

# Load Sensitivity Analysis results as dictionary
SAresults = np.load('SAresults.npy').item()
drawgraphs(SAresults)