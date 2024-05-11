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
#     url ='https://drive.google.com/file/d/1A2rktIR66_EYwwzPs78eLOFqyJohcl--/view?usp=sharing'
#     file_id = url.split('/')[-2]
#     dwn_url = 'https://drive.google.com/uc?export=download&id=' + file_id
#     # df = pd.read_csv(dwn_url)
#     return pd.read_csv(dwn_url)

dataset_url='https://raw.githubusercontent.com/project10109/InternalD11Dashboard/main/ipl_winnings_MAY.csv'
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


st.header("Click to get Latest Data")
if st.button("Update Leaderboard"):

# if button==True:
    df = get_data()
    df['Match'] = df['Team 1'] + ' vs. ' + df['Team 2']
    df=df.drop(['Team 1','Team 2'],axis=1)

    # print(df)

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

        

        st.title("Entry Fee Left")

        placeholder = st.empty()



        with placeholder.container():
            entryfee=1200
            matches_over=len(df.dropna())
            entryfee_left=1200-(matches_over*60)
            # create three columns
            kpi1, kpi2, kpi3 ,kpi4,kpi5,kpi6  = st.columns(6)

            # fill in those three columns with respective metrics or KPIs
            kpi1.metric(
                label="Rohit ⏳",
                value=entryfee_left
                # delta=df['Rohit']) - 10,
            )
            
            kpi2.metric(
                label="Mayur ⏳",
                value=entryfee_left
                # delta=df['Rohit']) - 10,
            )
            
            kpi3.metric(
                label="Akshay ⏳",
                value=1200+entryfee_left
                # delta=df['Rohit']) - 10,
            )

            kpi4.metric(
                label="Kaustubh ⏳",
                value=entryfee_left
                # delta=df['Rohit']) - 10,
            )

            kpi5.metric(
                label="Chaitanya ⏳",
                value=entryfee_left
                # delta=df['Rohit']) - 10,
            )

           

            kpi6.metric(
                label="Chintu ⏳",
                value=entryfee_left
                # delta=df['Rohit']) - 10,
            )
        st.markdown("### Detailed Data View")
        st.dataframe(df)
        time.sleep(1)

        # st.title("Line Chart of Money Won by Friends")
        # import pandas as pd
        # import plotly.express as px

        # # Create a new dataframe with the sum of values for the specified columns
        # new_df = df[['Rohit', 'Mayur', 'Akshay', 'Kaustubh', 'Chaitanya', 'Chintu']].sum(axis=0).reset_index(name='Total')

        # # Create a pie plot using Plotly Express
        # fig = px.pie(new_df, values='Total', names='index')

        # # Show the pie plot
        # fig.show()

        # df = get_data()

        # Filter the DataFrame to only include the specified columns
        # filtered_df = df[['Rohit', 'Mayur', 'Akshay', 'Kaustubh', 'Chaitanya', 'Chintu']]

        # # Sum the values for each column
        # summed_values = filtered_df.sum(axis=0)

        # # Create a pie plot using Plotly Express
        # fig = px.pie(summed_values, values=summed_values, names=summed_values.index, color_discrete_sequence=px.colors.qualitative.Plotly)

        # # Adjust the size of the plot
        # fig.update_layout(
        #     width=500,
        #     height=400
        # )

        # # Show the name in the pie
        # fig.update_traces(textposition='inside', textinfo='label+percent')

        # # Display the pie plot
        # fig.show()


