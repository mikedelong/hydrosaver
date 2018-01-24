import logging

import pandas as pd

# set up logging
formatter = logging.Formatter('%(asctime)s : %(name)s :: %(levelname)s : %(message)s')
logger = logging.getLogger('main')
logger.setLevel(logging.DEBUG)
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)
console_handler.setLevel(logging.DEBUG)
logger.debug('started')

input_folder = './input/'

# load the data into a dataframe
input_file = input_folder + 'train.csv'
data = pd.read_csv(input_file, encoding='ISO-8859-1')
logger.debug('we have %s columns' % data.columns)
print (data.describe())

print (data.head())
logger.debug('done.')
