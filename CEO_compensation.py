import numpy as np
from datascience import *

# These lines set up graphing capabilities.
import matplotlib
%matplotlib inline
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
import warnings
warnings.simplefilter('ignore', FutureWarning)

from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets



raw_compensation = Table.read_table('raw_compensation.csv')
raw_compensation


c = compensation
compensation = compensation.with_column("Total Pay C ($)",(raw_compensation.apply(convert_pay_string_to_number,"Cash Pay")))
compensation = compensation.with_column("Total Pay E ($)",(compensation.apply(convert_pay_string_to_number,"Equity Pay")))
compensation = compensation.with_column("Total Pay O ($)",(compensation.apply(convert_pay_string_to_number,"Other Pay")))

per = compensation.column("Total Pay C ($)")/sum(compensation.column("Total Pay C ($)"),compensation.column("Total Pay E ($)"),compensation.column("Total Pay O ($)"))
#compensation_f = compensation.with_column("Percent Cash",())