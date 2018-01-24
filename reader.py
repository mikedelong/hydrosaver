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

logger.debug('we have columns: %s ' % data.columns)

# 	PI Tag	            Tag Unit	Tag Description
# 01    WQI8100XCL1.CPV	TPH	        Flotation Circuit Feed (tons per hour)
# 02    XI84201.PV	    micro-m	    Con 2 Cycle Overflow 80 % passing Size
# 03    XI84202.PV	    %	        Con 2 Cycle Overflow  % Passing 106 mic
# 04    XI84123.PV	    %	        Flotation Tails  - % Cu
# 05    XI84124.PV	    %	        Flotation Tails - % Fe
# 06    XI84125.PV	    %	        Flotation Tails -%Solid
# 07    FX87211.CPV1	TPH	        TH602 Solids Feedrate
# 08    FIC87211.PV	    L/hr	    TH602 Flocculant Addition Flow PV
# 09    FIC87211.SV	    L/hr	    TH602 Flocculant Flow Setpoint
# 10	FX87211.P01	    G/T	        TH602 Flocculant Addition G/T Setpoint
# 11	FI87208.PV	    m^3/hr	    Flocculant Addition Process Water Dilution
# 12	AIC88049.PV	    pH	        TH602 Tailings Thickener pH Cntrl PV
# 13	ZI88001.PV	    %	        TH602 Tail Thickener Rake Height
# 14	NIC88002.PV	    %	        TH602 Rake Torque Ctrl PV
# 15	PIC88007.PV	    %	        TH602 Bed Pressure Ctrl PV
# 16	LIC88006.PV	    %	        TH602 Bed Level Ctrl PV
# 17	AIC88055.PV	    S	        TH602 Tails Thickener Settling Rate Controller PV
# 18	FIC88022.PV	    m^3/hr	    PU664/665 Discharge Flow Ctrl PV
# 19	DIC88023.PV	    %	        PU664/665 Discharge %Sol PV
# 20	II88151.PV	    A	        PU664 Motor Current
# 21	II88152.PV	    A	        PU665 Motor Current
# 22	SI88033.PV	    %	        TH602 U/F Pmp 664 Speed PV
# 23	SI88034.PV	    %	        TH602 U/F Pmp 665 Speed PV
# 24	MQI88024.CPV	TPH	        TH602 U/F Mass Calc CPV
# 25	FV88156.PV		PU664/665   Discharge Process Water Addition Valve Position
# 26	FV88043.PV		PU664       Suction  Process Water Addition Valve Position
# 27	FV88044.PV		PU665       Suction  Process Water Addition Valve Position
# 28	Target	%	 = DIC88023.PV +3h

print (data.describe())

print (data.head())
logger.debug('done.')
