import report_funcs

def create_nielsen_reports(daily_data_15min_path:str, daily_data_dayparts_path:str): 
    
    ######################
    # Initialize benchmark data 
    benchmark_15min_path = 'data/January Benchmark/Spectrum News - 15 Mins.xlsx'
    benchmark_dayparts_path = 'data/January Benchmark/Spectrum News Dayparts.xlsx'

    # Iniliaze config, read in mappings and info from config
    config_path = 'NielsenConfigv4.xlsx'
    print('Running Nielsen Report...\nReading config file ->', end =' ')
    daypartsorderDict, chartOrderDict, geomappingDict, stationMappingDict, penetration_dict, sn_names_dict = report_funcs.get_config_mappings(config_path)
    dmalists, emailrecipaints, emailsubjects, emailnotes, emailattachments = report_funcs.get_config_report_info(config_path)
    print('Done.')

    # Clean data

    print('Reading in and cleaning data ->',end = ' ')
    benchmark_15min = report_funcs.clean_15min_data(benchmark_15min_path, stationMappingDict, chartOrderDict, geomappingDict)
    benchmark_dayparts = report_funcs.clean_daypart_data(benchmark_dayparts_path, stationMappingDict,geomappingDict,daypartsorderDict)

    daily_data_15min = report_funcs.clean_15min_data(daily_data_15min_path, stationMappingDict, chartOrderDict, geomappingDict)
    daily_data_dayparts = report_funcs.clean_daypart_data(daily_data_dayparts_path, stationMappingDict,geomappingDict,daypartsorderDict)
    print('Done.')
    ##############################################################################################


    # Configure DMA objects based on specific data generates chart images and table images saved in temp folder
    print('Configuring DMA image objects:\n')
    uniquedmas = {x for i in dmalists for x in i}

    dma_html_dict, chart_path_dict, table_path_dict = report_funcs.create_dma_html2(uniquedmas, benchmark_15min, benchmark_dayparts, daily_data_15min, daily_data_dayparts, sn_names_dict, penetration_dict)
    print('\nSuccesfully created images.')
    # Write email 
    print('Writing emails:')
    email_to = 'jack.driscoll@charter.com'
    emails = report_funcs.get_email_html(dmalists, email_to, daily_data_15min,
                                emailrecipaints, emailsubjects, emailnotes,
                                 dma_html_dict, chart_path_dict, table_path_dict)
    

    msg = emails[0]
    report_funcs.send_email(msg, email_to)
    


if __name__ == '__main__':
    create_nielsen_reports(daily_data_15min_path = 'data/Test Daily Data/Spectrum News - 15 Mins_02-26-2024.xlsx' , daily_data_dayparts_path = 'data/Test Daily Data/Spectrum News Dayparts_02-26-2024.xlsx')