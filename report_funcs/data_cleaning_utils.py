# These functions are used in data cleaning and mapping. 

# Functions to be used in Cleaning/Reference Lambda Functions
def getorder(time, daypartsorderDict):
    if time in daypartsorderDict:
        return daypartsorderDict[time]
    else:
        return 99

# Get DMA from Nielsen Geography 
def getCity(geography, geomappingDict):
    if geography in geomappingDict:
        return geomappingDict[geography]
    else:
        return 'DMA not recognized'

# Rename to full day 
def renameFullDay(time):
    if time in ['03:00 am - 02:00 am','03:00 am - 03:00 am']:
        return 'Full Day'
    else: 
        return time