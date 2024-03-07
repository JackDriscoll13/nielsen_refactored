# The streamlit front end
import streamlit as st

from nielsen_daily import create_nielsen_reports

st.subheader('Upload Nielsen Data Here:', help= "These files should be able to be dragged straight from your inbox.")
col1, col2 = st.columns(2)
with col1:
    daily_15min_file = st.file_uploader("Upload raw daily 15min file here.")
with col2: 
    daily_dayparts_file = st.file_uploader("Upload raw daily dayparts file here.")

email_to = st.selectbox(
    'Who would you like to email the reports?', 
    ('jack.driscoll@charter.com', 'Keelan.Gallagher@charter.com', 'nathan.hess@charter.com')
)

st.write(' If you are ready, you can generate the report with the button. It will generate the reports and email them, should take a little less than a minute.')

if st.button('Generate Report', type='primary', use_container_width=True):
    with st.spinner('Running Report...'):
        create_nielsen_reports(daily_15min_file, daily_dayparts_file, email_to)
    st.write('Report Generated! Check your inbox (could come in the next minute or so).')