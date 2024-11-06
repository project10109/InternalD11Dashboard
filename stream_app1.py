import time  # to simulate a real time data, time loop

import numpy as np  # np mean, np random
import pandas as pd  # read csv, df manipulation
import plotly.express as px  # interactive charts
import streamlit as st  # 🎈 data web app development
from streamlit_option_menu import option_menu


st.set_page_config(
    page_title="Internal Potte Dream11 IPL Winnings Dashboard",
    page_icon="✅",
    layout="wide",
)


dataset_url='https://raw.githubusercontent.com/project10109/InternalD11Dashboard/main/Winnings_csv_INTERNAL_NOV.csv'
# read csv from a URL
@st.experimental_memo
def get_data() -> pd.DataFrame:
    return pd.read_csv(dataset_url)



# dashboard title
st.title("Internal Potte Dream11 IPL Winnings Dashboard")

# top-level filters
#job_filter = st.selectbox("Select the Job", pd.unique(df["job"]))

# creating a single-element container
placeholder = st.empty()

# button = st.button("Summarize")
st.header("Click to get Latest Data")
if st.button("Update Leaderboard"):
    df = get_data()
    # print('df',df['Ajinkya'].values)
    df['Match'] = df['Team 1'] + ' vs. ' + df['Team 2']
    df=df.drop(['Team 1','Team 2'],axis=1)

    print(df)

    with placeholder.container():

        # create three columns
        kpi1, kpi2, kpi3 ,kpi4,kpi5,kpi6  = st.columns(6)

        # fill in those three columns with respective metrics or KPIs
        kpi1.metric(
            label="Rohit ⏳",
            value=df['Rohit'].sum()
            # delta=df['Rohit']) - 10,
        )
        
        kpi2.metric(
            label="Mayur ⏳",
            value=df['Mayur'].sum()
            # delta=df['Rohit']) - 10,
        )
        
        kpi3.metric(
            label="Akshay ⏳",
            value=df['Akshay'].sum()
            # delta=df['Rohit']) - 10,
        )

        kpi4.metric(
            label="Kaustubh ⏳",
            value=df['Kaustubh'].sum()
            # delta=df['Rohit']) - 10,
        )

        kpi5.metric(
            label="Chaitanya ⏳",
            value=df['Chaitanya'].sum()
            # delta=df['Rohit']) - 10,
        )

        kpi6.metric(
            label="Chintu ⏳",
            value=df['Chintu'].sum()
            # delta=df['Rohit']) - 10,
        )


        st.title("Winnings After Reducing Entry Fees After Match 61 till Finals (i.e 14*60=Rs.840)")

        placeholder = st.empty()



    with placeholder.container():
        #entryfee=3600
        #matches_over=len(df.dropna())
        #entryfee_left=1200-(matches_over*60)
        #print('entryfee_left',entryfee_left)
        # create three columns
        kpi1, kpi2, kpi3 ,kpi4,kpi5,kpi6 = st.columns(6)

        # fill in those three columns with respective metrics or KPIs
        kpi1.metric(
            label="Rohit ⏳",
            value=df['Rohit'].sum()-840
        # delta=df['Rohit']) - 10,
        )
        
        kpi2.metric(
            label="Mayur ⏳",
            value=df['Mayur'].sum()-840
            # delta=df['Rohit']) - 10,
        )
        
        kpi3.metric(
            label="Akshay ⏳",
            value=df['Akshay'].sum()-840
            # delta=df['Rohit']) - 10,
        )

        kpi4.metric(
            label="Kaustubh ⏳",
            value=df['Kaustubh'].sum()-840
            # delta=df['Rohit']) - 10,
        )

        kpi5.metric(
            label="Chaitanya ⏳",
            value=df['Chaitanya'].sum()-840
            # delta=df['Rohit']) - 10,
        )

        kpi6.metric(
            label="Chintu ⏳",
            value=df['Chintu'].sum()-840
            # delta=df['Rohit']) - 10,
        )
    st.markdown("### Detailed Data View")
    st.dataframe(df)
    time.sleep(1)


