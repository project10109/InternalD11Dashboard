import time  # to simulate a real time data, time loop

import numpy as np  # np mean, np random
import pandas as pd  # read csv, df manipulation
import plotly.express as px  # interactive charts
import streamlit as st  # 🎈 data web app development
from streamlit_option_menu import option_menu


st.set_page_config(
    page_title="Mak Potte Dream11 IPL Winnings Dashboard",
    page_icon="✅",
    layout="wide",
)

# selected = option_menu('',
# ound(
#                       ['About Project',
#                        'Project Contributors'
#                         ],
#                       icons=['activity','activity','activity'],
#                       default_index=0)

# read csv from a github repo

# prompt: Read csv file from google drive

# print(df)

# read csv from a URL
# @st.experimental_memo
# def get_data() -> pd.DataFrame:
#     import pandas as pd
#     url ='https://drive.google.com/file/d/1C1Z1r3EGH7JwE98yREz8U8B5gVppXfhM/view?usp=sharing'
#     file_id = url.split('/')[-2]
#     dwn_url = 'https://drive.google.com/uc?export=download&id=' + file_id
#     # df = pd.read_csv(dwn_url)
#     return pd.read_csv(dwn_url)
dataset_url='https://raw.githubusercontent.com/project10109/InternalD11Dashboard/main/Winnings_csv_Mak_August_final.csv'
# read csv from a URL
@st.cache_data
def get_data() -> pd.DataFrame:
    return pd.read_csv(dataset_url)



# dashboard title
st.title("Mak Potte Dream11 IPL Winnings Dashboard")

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
            label="Ajinkya ⏳",
            value=df['Ajinkya'].sum()
            # delta=df['Rohit']) - 10,
        )
        
        kpi3.metric(
            label="Aditya ⏳",
            value=df['Aditya'].sum()
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
            label="Sumit ⏳",
            value=df['Sumit'].sum()
            # delta=df['Rohit']) - 10,
        )


        # # create two columns for charts
        # fig_col1, fig_col2 = st.columns(2)
        # with fig_col1:
        #     st.markdown("### First Chart")
        #     fig = px.density_heatmap(
        #         data_frame=df, y="age_new", x="marital"
        #     )
        #     st.write(fig)
            
        # with fig_col2:
        #     st.markdown("### Second Chart")
        #     fig2 = px.histogram(data_frame=df, x="age_new")
        #     st.write(fig2)



        # import streamlit as st
        # import pandas as pd
        # import plotly.express as px

        # # Sample data (replace with your actual data if needed)
        # data = {
        #     "Rohit": [100.200],
        #     "Chaddi": [50, 300],
        #     "Kstya": [180, 400],
        #     "Gtya": [210, 400]
        # }

        # df = pd.DataFrame(data)

        # Streamlit app layout
        # st.title("Line Chart of Money Won by Friends")

        # Create the line chart with Plotly Express
        # fig = px.line(
        #     df,
        #     x=df.columns,  # Use column names as x-axis labels
        #     y=df.values.flatten(),  # Flatten the DataFrame values for plotting multiple lines
        #     title="Money Won Over Time ",
        #     labels={"x": "Friend", "y": "Money Won"}  # Set custom axis labels
        # # )


    #    -----------
        # import plotly.express as px

        # fig = px.line(df)

        # st.plotly_chart(fig, use_container_width=True)

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
            label="Ajinkya ⏳",
            value=df['Ajinkya'].sum()-840
            # delta=df['Rohit']) - 10,
        )
        
        kpi3.metric(
            label="Aditya ⏳",
            value=df['Aditya'].sum()-840
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
            label="Sumit ⏳",
            value=df['Sumit'].sum()-840
            # delta=df['Rohit']) - 10,
        )
    st.markdown("### Detailed Data View")
    st.dataframe(df)
    time.sleep(1)


