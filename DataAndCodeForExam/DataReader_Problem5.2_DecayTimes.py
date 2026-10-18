# --------------------------------------------------------------------------------------------------------
# Script for reading data for Problem 5.2 (data_DecayTimes.csv) in Applied Statistics 2023-24 exam:
# --------------------------------------------------------------------------------------------------------
#
# The data file contains 1000 entries with measured decay times in seconds.
#
# The script was distributed along with the exam and the data file itself on the 18th of January 2024.
#
#   Author: Troels Petersen (Niels Bohr Institute, petersen@nbi.dk)
#   Date:   17th of January 2023 (latest version)
#
# --------------------------------------------------------------------------------------------------------

import numpy as np

data = np.genfromtxt('data_DecayTimes.csv')
print(data.shape)

# Print the first ten entries to get a feel for the data:
print(data[0:10])
