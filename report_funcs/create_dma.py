import dataframe_image as dfi

from .create_table import create_table
from .create_chart import create_chart, create_chart_dallas

# Config DMA Object
def create_dma_html(dma, penetrationdict, snNamesDict, avgdayparts,dailydayparts,avg15min,daily15min):

    # Point to image folder`    `   
    image_folder = 'C:/Users/P3159331/OneDrive - Charter Communications/Documents - Audience Insights/5. Development/Nielsen Automation/nielsen_refactored/chart_images'
    # Reduce dataset to only DMA, can be used in title of section - "blank DMA with blank stations"
    if (dma not in dailydayparts['DMA'].unique()) or (dma not in daily15min['DMA'].unique()):
        return "" # '<h3 style="font-size:18px;"> ' + f'{dma} not available at this time'  + ' </h3> <hr color="black" size="2" width="100%"> </br>' 

    avgdayparts = avgdayparts[avgdayparts['DMA']==dma]
    dailydayparts = dailydayparts[dailydayparts['DMA']==dma]
    avg15min = avg15min[avg15min['DMA']==dma]
    daily15min = daily15min[daily15min['DMA']==dma]

    # Create first part of HTMl - heading for html doc and title 
    dmahtml = '<h3 style="font-size:18px;"> ' + str(dma)  + ' </h3> <b>Ratings by Quarter Hour:</b>'

    # Config chart or charts 
    sources = daily15min['Viewing Source'].unique()
    #print(sources)

    # Case dallas
    if dma == 'Dallas/Ft. Worth':
        chart = create_chart_dallas(daily15min, avg15min, snNamesDict)
        chartpath = image_folder + str('dallas_ft_wrth')+ 'chart.png'
        chart.savefig(chartpath,bbox_inches="tight")
        charthtml = '<br><img src="'+chartpath+'" width="900"></img>' 
        dmahtml+=charthtml

    else:
        for source in sources:
            print(source)
            chart = create_chart(source, daily15min, avg15min, snNamesDict)
            # Now I want to create and save a unique name for the path
            chartpath = image_folder + str(source)+ 'chart.png'
            chart.savefig(chartpath,bbox_inches="tight")
            charthtml = '<br><img src="'+chartpath+'" width="900"></img>' 
            dmahtml+=charthtml


    if dma == 'Dallas/Ft. Worth':
        table = create_table(dma,avgdayparts,dailydayparts,KAZD=True)
    else: 
        table = create_table(dma,avgdayparts,dailydayparts)
    
    tablepath = image_folder + sources[0] + 'table.png'
    dfi.export(table, tablepath, dpi = 500,  chrome_path='C:\Program Files\Google\Chrome\Application\chrome.exe')

    dmahtml += f'<br> <b>Dayparts Table ({dma}):</b> <br> <img src="'+tablepath+'" width="900"></img><br>' + penetrationdict[dma] +'<br><br><hr color="black" size="2" width="100%">' 
    
    # Now we have the charts saved
    return dmahtml