# nielsen_refactored
 a report that generates and sends html emails based on daily nielsen data

# Overview

The core of this process is the `create_nielsen_reports` function found in the [nielsen_daily.py](nielsen_daily.py) file. The function takes 4 inputs and generates the daily nielsen report in an email it sends to one recipiant.

The program works by reading in 4 raw data files; daily nielsen 15minute data, daily nielsen daypart data, (both provided by the user) benchmark nielsen 15 minute data, and benchmark nielsen daypart data (stored in the back end). The program cleans the data and maps relevant information. Then creates custom charts and tables for each dma based on daily and benchmark data. The program then  embeds these charts and tables into html using a CID for each image, and generates the relevant emails using this html. 



## Directory Structure


### Goals

- Generate the daily nielsen report in some type of HTMl or pdf that can be copy pasted into an email.

- Use a kind of drag and drop approach so whoever recieves emails can drag and drop files into this process
- Deploy on aws EC2 to
- Have it deployed and functional for use by monday. 
- streamlit


### Approach