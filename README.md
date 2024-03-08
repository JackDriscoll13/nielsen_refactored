# nielsen_refactored
 link to app: [http://3.147.67.55:8501](http://3.147.67.55:8501)

# Overview

The core of this process is the `create_nielsen_reports` function found in the [nielsen_daily.py](nielsen_daily.py) file. The function takes 4 inputs and generates the daily nielsen report in an email it sends to one recipiant.

The program works by reading in 4 raw data files; daily nielsen 15minute data, daily nielsen daypart data, (both provided by the user) benchmark nielsen 15 minute data, and benchmark nielsen daypart data (pre - stored in the back end). The program cleans the data and maps relevant information. Then creates custom charts and tables for each dma based on daily and benchmark data. The program then  embeds these charts and tables into html using a CID for each image, and generates the relevant emails using this html. Finally, it connects to a gmail server and email address and sends the emails to the user. Who can then forward them to people at charter.


## Directory Structure
- [report_funcs/](report_funcs/)  
  All code relating to the main function of this process lives here.  
- [resouces/](resouces/)  
  stores non code but critical files. Most important is [config file](resources\NielsenConfigv4.xlsx), which is an excel file that stores relevant mappings, as well as report details such as email subject lines, dmas to include in each email, and email notes.  
  You will [data/](data/) here, which stores benchmark data files, and [image_dir/](image_dir/) which is where images for the report are temporarily stored.

  
