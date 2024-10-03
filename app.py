import streamlit as st

import json
from datetime import date
from urllib.request import urlopen
import time

import altair as alt
import numpy as np
import pandas as pd
import requests
import streamlit as st
import streamlit.components.v1 as components
from pandas import json_normalize
import plotly.express as px
import ast 
_ENABLE_PROFILING = False

if _ENABLE_PROFILING:
    import cProfile, pstats, io
    from pstats import SortKey
    pr = cProfile.Profile()
    pr.enable()





def plot_typology():
    # Example Data
    data = {
        'Attitude': ['government critique', 'societal critique', 'money/aid allocation', 'solutions/interventions', 
                     'harmful generalization', 'deserving/undeserving', 'personal interaction', 
                     'not in my backyard', 'media portrayal'],
        'Proportion of posts labeled with attitude': [0.31, 0.16, 0.12, 0.35, 0.23, 0.12, 0.1, 0.05, 0.02]
    }

    # Create a DataFrame
    df = pd.DataFrame(data)

    # Custom colors for each category
    custom_colors = {
        'government critique': '#5BCBFF',  
        'societal critique': '#5BCBFF',  
        'money/aid allocation': '#5BCBFF',  
        'solutions/interventions': '#FFA828',  
        'harmful generalization': '#96778A',  
        'deserving/undeserving': '#96778A',  
        'personal interaction': '#96778A',  
        'not in my backyard': '#96778A',  
        'media portrayal': '#96778A'
    }

    # Plotly Bar Chart with custom colors
    fig = px.bar(
        df,
        x='Proportion of posts labeled with attitude',
        y='Attitude',
        orientation='h',
        title="",
        color='Attitude',
        color_discrete_map=custom_colors
    )
    
    fig.update_layout(showlegend=False)
    # Update y-axis to hide labels and increase font size
    fig.update_yaxes(title_text='', tickfont=dict(size=20))  
    fig.update_xaxes(tickfont=dict(size=18), title_font=dict(size=20))

    # Create two columns for layout
    col1, col2 = st.columns(2)

    # Display the bar chart in the first column
    with col1:
        st.plotly_chart(fig)

    # Display the image in the second column
    with col2:
        st.image("typology_updated.png", width=600)  # Adjust the image path and size



def return_examples():

    data = {
        'Attitude': ['government critique', 'societal critique', 'money/aid allocation', 'solutions/interventions', 'harmful generalization', 'deserving/undeserving of resources', 'personal interaction', 'not in my backyard', 'media portrayal'],
        'Proportion of posts labeled with attitude': [0.31, 0.16, 0.12, 0.35, 0.23, 0.12, 0.1, 0.05, 0.02]
    }

    # Create a DataFrame
    df = pd.DataFrame(data)

    labeled_data = pd.read_csv('expert_annotations.csv')

    frames_mod = []
    temp = labeled_data['frames'].tolist()

    for i in temp:
        frames_mod.append(ast.literal_eval(i))
    labeled_data['Attitude'] = frames_mod

    # Initialize a variable to hold the messages
    mapping = {'deserving/undeserving':'deserving_undeserving_of_resources', 
            'government critique':'government_critique', 
            'money/aid allocation':'money_aid_resource_allocation',
            'solutions/interventions':'solutions_interventions', 
            'societal critique':'societal_critique', 
            'harmful generalization':'harmful_generalization', 
            'personal interaction':'personal_interaction_observation_of_homelessness',
            'not in my backyard':'not_in_my_backyard',
            'media portrayal':'media_portrayal'}
    
    
    # Create a multiselect for the attitudes
    selected_categories = st.multiselect('Select Attitudes', df['Attitude'])

    # Initialize a variable to hold the filtered messages
    selected_messages = []

    # Filter the DataFrame for rows where all selected attitudes are present
    if selected_categories:
        # Rename the selected attitudes using the mapping
        cats_renamed = [mapping[category] for category in selected_categories]

        # Loop through rows in the DataFrame
        for idx, row in labeled_data.iterrows():
            # Check if all selected attitudes are in the 'Attitude' list for this row
            if all(cat in row['Attitude'] for cat in cats_renamed):
                selected_messages.append('Tweet: ' +row['tweet']+'\n'+'--------------------------------------------')

    # Display the selected messages
    if selected_messages:
        st.text_area("Example post labeled with attitude", value="\n".join(selected_messages), height=200)
    else:
        st.text_area("Example post labeled with attitude", value="Select an attitude to see an example post", height=100)

def label_tweets():
    user_input = st.text_input("Enter a post:")
    if user_input == 'seriously?? he’s saying the city is spending $170 million on bike lanes, while the homeless count soars. $170m is better spent pretty much on anything else.':
        # words = user_input.split()  # Split by space, can adjust to other delimiters if needed
        st.write("OATH-Frames Attitudes")
        button_html = f"""
        <style>
        .button {{
            background-color: #5BCBFF; /* Green */
            border: none;
            color: black;
            padding: 10px 20px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
            border-radius: 12px;
        }}
        </style>
        <button class="button">money/aid allocation</button>
        """
        # Display the button with custom styling
        st.markdown(button_html, unsafe_allow_html=True)
    elif user_input == 'ukrainian refugees can get ssi, housing benefits, and free health care. meanwhile, we have a lot of homeless people who have no access to such benefits - we have the highest number of the unemployed black population.':
        st.write("OATH-Frames Attitudes")
        button_one = f"""
        <style>
        .button {{
            background-color: #5BCBFF; /* Green */
            border: none;
            color: black;
            padding: 10px 20px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
            border-radius: 12px;
        }}
        </style>
        <button class="button">government critique</button>
        """
        # Display the button with custom styling
        st.markdown(button_one, unsafe_allow_html=True)
        button_two = f"""
        <style>
        .button {{
            background-color: #5BCBFF; /* Green */
            border: none;
            color: black;
            padding: 10px 20px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
            border-radius: 12px;
        }}
        </style>
        <button class="button">money/aid allocation</button>
        """
        # Display the button with custom styling
        st.markdown(button_two, unsafe_allow_html=True)


        button_three = f"""
        <style>
        .button {{
            background-color: #96778A; /* Green */
            border: none;
            color: black;
            padding: 10px 20px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
            border-radius: 12px;
        }}
        </style>
        <button class="button">deserving/undeserving</button>
        """
        # Display the button with custom styling
        st.markdown(button_three, unsafe_allow_html=True)


    


def plot_state_time():
    states = ['All Posts', 'California', 'New York', 'Texas', 'Washington', 'Oregon', 'Florida', 'Illinois', 'Colorado', 'Arizona', 'District of Columbia']
    attitudes = ['deserving/undeserving', 'government critique', 'money/aid allocation',
                'solutions/interventions', 'societal critique', 'harmful generalization',
                'personal interaction', 'not in my backyard', 'media portrayal']

    df = pd.read_csv('state_time_attitudes.csv')
    df['date'] = pd.to_datetime(df['date'])



    # Timeline Selection
    min_date = df['date'].min().date()  # Use date() to get a date object
    max_date = df['date'].max().date()

    # Create columns for filters
    col1, col2, col3 = st.columns(3)

    # Using date objects for the slider
    with col1:
        start_date, end_date = st.slider(
            "Select Date Range",
            min_value=min_date,
            max_value=max_date,
            value=(min_date, max_date),  # Default range
            format="YYYY-MM-DD"
        )

    with col2:
        # State Selection from US Map
        selected_state = st.selectbox("Select a State", states)

    with col3:
        # Attitude Selection Buttons
        attitude_options = st.multiselect(
            "Select Attitudes",
            attitudes,
            default=attitudes  # Default to all attitudes selected
        )

    # Filter DataFrame based on user selections
    filtered_df = df[
        (df['date'] >= pd.Timestamp(start_date)) &  # Ensure conversion to datetime
        (df['date'] <= pd.Timestamp(end_date)) &
        (df['state'] == selected_state) &
        (df['attitude'].isin(attitude_options))
    ]

    # Create Line Plot
    if not filtered_df.empty:
        fig = px.line(
            filtered_df,
            x='date',
            y='frequency',
            color='attitude',
            title=f'Frequency of Attitudes in {selected_state} from {start_date} to {end_date}',
            labels={'frequency': 'Frequency', 'date': 'Date'},
            # markers=True
        )

        # Update layout for better presentation
        fig.update_layout(
            xaxis_title='Date of Post',
            yaxis_title='Frequency of Posts',
            legend_title='Attitudes',
            width=1700, 
            height=600
        )

        st.plotly_chart(fig)
    else:
        st.write("No data available for the selected filters.")



today = date.today()

st.set_page_config(
    page_title="OATH-Frames",
    layout='wide',
    initial_sidebar_state='auto',
)

# Header panel
st.markdown("""
<style>
.header-panel {
    background-color: #f0f2f5; /* Light gray background */
    border: 1px solid #d3d3d3; /* Light gray border */
    padding: 20px; /* Padding around the content */
    border-radius: 8px; /* Rounded corners */
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Subtle shadow */
}
.header-title {
    font-size: 36px; /* Large font size for the title */
    font-weight: bold; /* Bold title */
}
.header-subtitle {
    font-size: 24px; /* Medium font size for the subtitle */
}
</style>

<div class="header-panel">
    <div class="header-title">Online Attitudes Towards Homelessness Dashboard</div>
    <div class="header-subtitle">OATH-Frames Dashboard</div>
</div>
""", unsafe_allow_html=True)

st.write("")
st.markdown(""" Public attitudes towards key societal issues, expressed on online media, are of immense value in policy and reform efforts, yet challenging to understand at scale. We study one such social issue: homelessness in the U.S., by leveraging the remarkable capabilities of large language models to assist social work experts in analyzing millions of posts from Twitter. We introduce a framing typology: Online Attitudes Towards Homelessness (OATH) Frames: nine hierarchical frames capturing critiques, responses and perceptions. We release annotations with varying degrees of assistance from language models, with immense benefits in scaling: 6.5x speedup in annotation time while only incurring a 3 point F1 reduction in performance with respect to the domain experts. Our experiments demonstrate the value of modeling OATH-Frames over existing sentiment and toxicity classifiers. Our large-scale analysis with predicted OATH-Frames on 2.4M posts on homelessness reveal key trends in attitudes across states, time periods and vulnerable populations, enabling new insights on the issue. Our work provides a general framework to understand nuanced public attitudes at scale, on issues beyond homelessness.""")




# Custom CSS for styling buttons
st.markdown("""
    <style>
    .button {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        padding: 10px 20px;
        margin-right: 10px;  /* Space between buttons */
        font-size: 16px;
        font-weight: bold;
        color: white;
        background-color: white;
        border: 2px solid #888;  /* Border color */
        border-radius: 30px;
        text-decoration: none;
        cursor: pointer;
    }
    .button img {
        margin-right: 10px;
        filter: brightness(0);  /* Make icons black */
    }
    .button:hover {
        background-color: #555;
    }
    </style>
    """, unsafe_allow_html=True)

# Create buttons directly in one markdown section
st.markdown("""
    <a href="https://arxiv.org/abs/2406.14883" target="_blank" class="button">
        <img src="https://img.icons8.com/material-outlined/24/000000/document--v1.png"/> Paper
    </a>
    <a href="https://github.com/dill-lab/oath-frames" target="_blank" class="button">
        <img src="https://img.icons8.com/material-outlined/24/000000/github.png"/> Code
    </a>
    <a href="#https://dill-lab.github.io/oath-frames/" target="_blank" class="button">
        <img src="https://img.icons8.com/material-outlined/24/000000/image.png"/> Blog
    </a>
""", unsafe_allow_html=True)




# today = date.today()

# st.set_page_config(
#     page_title="OATH-Frames",
#     layout='wide',
#     initial_sidebar_state='auto',
# )

# t1, t2 = st.columns(2)
# with t1:
#     st.markdown('# Online Attitudes Towards Homelessness Dashboard')
#     st.subheader('OATH-Frames Dashboard')

# st.write("")
# st.markdown("""##### We introduce a framing typology: Online Attitudes Towards Homelessness (OATH) Frames: nine hierarchical frames capturing critiques, responses and perceptions. We analyze attitudes across states and time at a large scale on 2.4M posts. 
# """)


# st.markdown('## Labeling Attitudes with Large Language Models 🤖')
# label_tweets()
st.markdown('## OATH-Frames Typology')
plot_typology()
return_examples()
st.markdown('## Attitudes by State Mentions 🌎 and Time 📈')
plot_state_time()


# st.markdown("## About Us")

# st.markdown("This project was led by a team of researchers in the [Dill Lab](https://dill-lab.github.io/) in the USC NLP Department and the USC Dworak-Peck School of Social Work")

# import streamlit as st

# # Define the number of people and their details
# people = [
#     {
#         "name": "Jaspreet Ranjit",
#         "image": st.image("jaspreet.png", width=100),
#         "profile_link": "https://jr4fs.github.io/"
#     },
#     {
#         "name": "Brihi Joshi",
#         "image": "https://via.placeholder.com/100",
#         "profile_link": "https://brihijoshi.github.io/"
#     },
#     {
#         "name": "Rebecca Dorn",
#         "image": "https://via.placeholder.com/100",
#         "profile_link": "https://rebedorn.github.io/"
#     },
#     {
#         "name": "Laura Petry",
#         "image": "https://via.placeholder.com/100",
#         "profile_link": "https://scholar.google.com/citations?user=fd1Pq94AAAAJ&hl=en"
#     },
#     {
#         "name": "Olga Koumoundouros",
#         "image": "https://via.placeholder.com/100",
#         "profile_link": "https://dworakpeck.usc.edu/academic-programs/doctor-of-philosophy/phd-current-student-bios"
#     },
#     {
#         "name": "Jayne Bottarini",
#         "image": "https://via.placeholder.com/100",
#         "profile_link": "https://www.linkedin.com/in/jayne-bottarini/"
#     },
#     {
#         "name": "Peichen Liu",
#         "image": "https://via.placeholder.com/100",
#         "profile_link": "https://dworakpeck.usc.edu/academic-programs/doctor-of-philosophy/phd-current-student-bios"
#     },
#     {
#         "name": "Eric Rice",
#         "image": "https://via.placeholder.com/100",
#         "profile_link": "https://dworakpeck.usc.edu/academics/faculty-directory/eric-rice"
#     },
#     {
#         "name": "Swabha Swayamdipta",
#         "image": "https://via.placeholder.com/100",
#         "profile_link": "https://swabhs.com/"
#     }
# ]

# cols = st.columns(len(people))


# for col, person in zip(cols, people):
#     with col:
#         # Create a panel for each person with a paper link icon
#         st.markdown(f"""
#             <div style="padding: 10px; border: 1px solid #ccc; border-radius: 8px; text-align: center; box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);">
#                 <img src="{person['image']}" alt="{person['name']}" style="width: 100px; height: auto; border-radius: 50%; margin-bottom: 10px;"/>
#                 <h4>{person['name']}</h4>
#                 <a href="{person['profile_link']}" target="_blank">
#                     <img src="https://img.icons8.com/material-outlined/24/000000/link.png" alt="Link" style="width: 24px; height: 24px;"/>
#                 </a>
#             </div>
#         """, unsafe_allow_html=True)


# Citation header
st.markdown("## Citation")

# Displaying the citation in a formatted box
bibtex = """
@article{ranjit2024oath,
  title={OATH-Frames: Characterizing Online Attitudes Towards Homelessness with LLM Assistants},
  author={Ranjit, Jaspreet and Joshi, Brihi and Dorn, Rebecca and Petry, Laura and Koumoundouros, Olga and Bottarini, Jayne and Liu, Peichen and Rice, Eric and Swayamdipta, Swabha},
  journal={arXiv preprint arXiv:2406.14883},
  year={2024}
}
"""

st.code(bibtex, language='bibtex')

# Create a horizontal layout with columns for logos
col1, col2 = st.columns([1, 1])

with col1:
    st.image("usc.png", width=200)  # University logo 1
# with col2:
#     st.image("social_work.png", width=200)  # University logo 2 (if needed)




if _ENABLE_PROFILING:
    pr.disable()
    s = io.StringIO()
    sortby = SortKey.CUMULATIVE
    ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
    ps.print_stats()
    ts = int(time.time())
    with open(f"perf_{ts}.txt", "w") as f:
        f.write(s.getvalue())
