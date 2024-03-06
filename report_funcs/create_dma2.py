import dataframe_image as dfi
from .create_table import create_table
from .create_chart import create_chart, create_chart_dallas

from email.utils import make_msgid

def create_dma_html2(unique_dmas, avgdayparts, dailydayparts,): 
    dmas_html_dict = {}
    table_path_dict = {}
    chart_path_dict = {}

    image_folder = 'C:/Users/P3159331/OneDrive - Charter Communications/Documents - Audience Insights/5. Development/Nielsen Automation/nielsen_refactored/chart_images2/'

    for dma in unique_dmas: 


        # Initialize the dma html 
        dmahtml = '<h3 style="font-size:18px;"> ' + str(dma)  + ' </h3> <b>Ratings by Quarter Hour:</b>'

        # Create the chart
        # if dma == 'Dallas/Ft. Worth':
        #      chart = create_chart_dallas(daily15min, avg15min, sn_names_dict)
        # else: 
        #      sources = daily15min['Viewing Source'].unique()
        #      for source in sources:
        #         chart = create_chart(source, daily15min, avg15min, sn_names_dict)
        # chartpath = image_folder + dma[0:3] + '_chart.png'
        # chart_cid = make_msgid()
        # chart.savefig(chartpath,bbox_inches="tight")
        # dmahtml = '<br><img src="cid:{chart_cid}" width="900">'.format(chart_cid=chart_cid[1:-1])  



        # Create the table
        if dma == 'Dallas/Ft. Worth':
            table = create_table(dma,avgdayparts,dailydayparts,KAZD=True)
        else: 
            table = create_table(dma,avgdayparts,dailydayparts)
        tablepath = image_folder + dma[0:3] + '_table.png'
        dfi.export(table, tablepath, dpi = 500,  chrome_path='C:\Program Files\Google\Chrome\Application\chrome.exe')
        table_cid = make_msgid()
        dmahtml += """
                        <br> <b>Dayparts Table ({dma}):</b> <br>
                        <img src="cid:{table_cid}" width="900">
                """.format(table_cid = table_cid[1:-1], dma = dma)
        
        # Save relevant information
        dmas_html_dict[dma] = dmahtml
        table_path_dict[tablepath] = table_cid
        #chart_path_dict[chartpath] = chart_cid

        
    return dmas_html_dict, table_path_dict, chart_path_dict
if __name__ == '__main__':
       unique_dmas = {'Cleveland/Akron', 'Orlando/Daytona Beach/Melbourne', 'Los Angeles', 'New York', 'Charlotte', 'Tampa/Saint Petersburg', 'Dallas/Ft. Worth'}
       create_dma_html2(unique_dmas)