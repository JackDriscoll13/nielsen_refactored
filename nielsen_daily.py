
import report_funcs
import shutil

def create_nielsen_reports(daily_data_15min_path:str, daily_data_dayparts_path:str): 
    
    ######################
    # Initialize benchmark data 
    benchmark_15min_path = 'data/January Benchmark/Spectrum News - 15 Mins.xlsx'
    benchmark_dayparts_path = 'data/January Benchmark/Spectrum News Dayparts.xlsx'

    # Iniliaze config, read in mappings and info from config
    config_path = 'NielsenConfigv4.xlsx'
    print('Running Nielsen Report...\nReading config file ->', end =' ')
    daypartsorderDict, chartOrderDict, geomappingDict, stationMappingDict, penetrationMappingDict, sn_names_dict = report_funcs.get_config_mappings(config_path)
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


    # # Configure DMA objects based on specific data generates chart images and table images saved in temp folder
    print('Configuring DMA image objects:\n')
    uniquedmas = {x for i in dmalists for x in i}

    dma_html_dict, chart_path_dict, table_path_dict = report_funcs.create_dma_html2(uniquedmas, benchmark_15min, benchmark_dayparts, daily_data_15min, daily_data_dayparts, sn_names_dict)
    print('\nSuccesfully created images.')
    # # # Write email 
    print('Writing emails:')
    email_dmas = list(uniquedmas)
    report_funcs.get_email_html(email_dmas, dma_html_dict, chart_path_dict, table_path_dict)

    # For effiencys sake we only want to generate each dma object once. 
    # We save the html for each dma in a dictionary with a dma name as the key and the html as the value
    # alldmas = {}
    # for dma in uniquedmas:
    #     print(f'{dma};', end= ' ')
    #     alldmas[dma] = report_funcs.create_dma_html(dma, penetrationdict = penetrationMappingDict, snNamesDict= snNamesDict,  avgdayparts=benchmark_dayparts, dailydayparts= daily_data_dayparts, avg15min = benchmark_15min, daily15min = daily_data_15min)
    #     print('Done,', end= ' ')
    # print('\nSuccess! Configured all DMA Img Objects')

    # # Now we generate distinct html files based on the dma lists in our config
    # for i in range(len(dmalists)):
    #     report_funcs.create_html_body_email(i, dmalists, alldmas, emailrecipaints, emailsubjects, emailnotes, emailattachments)

    #shutil.rmtree('chart_images/')


if __name__ == '__main__':
    create_nielsen_reports(daily_data_15min_path = 'data/Test Daily Data/Spectrum News - 15 Mins_02-26-2024.xlsx' , daily_data_dayparts_path = 'data/Test Daily Data/Spectrum News Dayparts_02-26-2024.xlsx')