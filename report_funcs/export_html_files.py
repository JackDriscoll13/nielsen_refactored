

def save_html_files(html_strings, emails, chart_path_dict, table_path_dict): 
    for i in range(len(html_strings)): 
        # Get email details
        subject = emails[i]['subject']
        html = html_strings[i]

        for path in chart_path_dict:
            chart_cid = 'cid:'+ ((chart_path_dict[path])[1:-1])
            newpath = 'C:/Users/P3159331/OneDrive - Charter Communications/Documents - Audience Insights/5. Development/Nielsen Automation/nielsen_refactored/' + path
            html = html.replace(chart_cid, newpath)

        for path in table_path_dict:
            table_cid = 'cid:'+ ((table_path_dict[path])[1:-1])
            newpath = 'C:/Users/P3159331/OneDrive - Charter Communications/Documents - Audience Insights/5. Development/Nielsen Automation/nielsen_refactored/' + path
            html = html.replace(table_cid, newpath)



        with open(f'resources/html_exports/file{i+1}.html', 'w') as file: 
            file.write(f'<p>{subject}</p>' + '<br><hr color="black" size="2" width="100%"><br>' + html)




