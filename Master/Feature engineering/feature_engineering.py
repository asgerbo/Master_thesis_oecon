import numpy as np
import pandas as pd
import tensorflow as tf


macrovariables = pd.read_csv('/Users/nadjos/Downloads/macrovariables (1).csv')
macrovariables['usd_eur_exchange'] = macrovariables['usd_eur_exchange'].diff()
# cut off first row
macrovariables = macrovariables[1:]


macrovariables_featured.to_csv('/Users/nadjos/Desktop/Uni/speciale/macrovariables_featured.csv', index=False)
