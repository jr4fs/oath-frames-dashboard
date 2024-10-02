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

_ENABLE_PROFILING = False

if _ENABLE_PROFILING:
    import cProfile, pstats, io
    from pstats import SortKey
    pr = cProfile.Profile()
    pr.enable()




def plot_typology():
    # Example Data
    data = {
        'Attitude': ['government critique', 'societal critique', 'money/aid allocation', 'solutions/interventions', 'harmful generalization', 'deserving/undeserving of resources', 'personal interaction', 'not in my backyard', 'media portrayal'],
        'Proportion of posts labeled with attitude': [0.31, 0.16, 0.12, 0.35, 0.23, 0.12, 0.1, 0.05, 0.02],
        'Messages': [
            "these people are already housed possibly over crowded but at least housed .there are up to 130000 homeless living rough on our streets every night women and children in the back of vans and cars and the gov gives billions away to help third world countries.? time he looked here",
            "i really hate people who have mango trees but don’t eat mangos so they just let them go to waste. i be walking by peoples yards and see hella mangos just laying there for days. give them to the homeless, don’t just let the mangos sit there and rot.",
            "you propose atlanta/fulton county fund a homeless city. i’m asking what return are we getting for our tax dollars? police officers and firefighters provide a service which can justify us building a training for them. what justification do you have for your city for the homeless?",
            "Ever think that instead of jail, A MENTALLY ILL HOMELESS PERSON needs actual help? Yes, I have compassion for his victims. But I also have compassion for this guy. He needs help. He doesn’t need to be thrown in jail where he’ll rot and probably be left to die. You pointed out",
            "@mention you’re more confused than a homeless man in a house arrest. you can’t even put your words together. please get out.",
            "Look at the illegals 500$ a night hotel rooms , destroying them, wasting food instead of giving to the homeless",
            "i’m legit sad af. i saw a homeless woman and her daughter. i really wanted to help but i had no cash. i hope they are still there when i circle back around.",
            "just found out the head of the opposition to a local affordable housing for the homeless project is a senior planner in the neighboring county",
            "is the national news reporting on the homeless on the streets and encampments as well as random crime exaggerated? beautiful city and location.",
        ]
    }

    # Create a DataFrame
    df = pd.DataFrame(data)

    # Custom colors for each category
    custom_colors = {
        'government critique': '#5BCBFF',  # Tomato Red
        'societal critique': '#5BCBFF',  # Dodger Blue
        'money/aid allocation': '#5BCBFF',  # Lime Green
        'solutions/interventions': '#FFA828',  # Gold
        'harmful generalization': '#96778A',   # Orange Red
        'deserving/undeserving of resources': '#96778A',  # Tomato Red
        'personal interaction': '#96778A',  # Dodger Blue
        'not in my backyard': '#96778A',  # Lime Green
        'media portrayal': '#96778A' # Gold
    }


    # Plotly Bar Chart with custom colors
    fig = px.bar(
        df,
        x='Proportion of posts labeled with attitude',
        y='Attitude',
        orientation='h',
        title="",
        color='Attitude',
        color_discrete_map=custom_colors  # Map each category to a specific color
    )
    fig.update_layout(showlegend=False)
    # Update y-axis to hide labels and increase font size
    fig.update_yaxes(title_text='', tickfont=dict(size=20))  # Remove y-axis title and increase font size
    fig.update_xaxes(tickfont=dict(size=18), title_font=dict(size=20))

    # Display the Plotly chart in Streamlit
    st.plotly_chart(fig)

    # Create a checkbox list for the categories
    selected_categories = st.multiselect('Select Attitudes', df['Attitude'])

    # Initialize a variable to hold the messages
    selected_messages = []

    # Retrieve messages for the selected categories
    for category in selected_categories:
        message = df.loc[df['Attitude'] == category, 'Messages'].values[0]
        selected_messages.append(message)

    # Show the corresponding messages in a textbox if any categories are selected
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
    states = ['California', 'New York', 'Texas', 'Washington', 'Oregon', 'Florida', 'Illinois', 'Colorado', 'Arizona', 'District of Columbia', 'All Posts']
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
            markers=True
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

t1, t2 = st.columns(2)
with t1:
    st.markdown('# Online Attitudes Towards Homelessness Dashboard')
    st.subheader('OATH-Frames Dashboard')

st.write("")
st.markdown("""##### We introduce a framing typology: Online Attitudes Towards Homelessness (OATH) Frames: nine hierarchical frames capturing critiques, responses and perceptions. We analyze attitudes across states and time at a large scale on 2.4M posts. 
""")


# st.markdown('## Labeling Attitudes with Large Language Models 🤖')
# label_tweets()
st.markdown('## OATH-Frames Typology')
plot_typology()
st.markdown('## Attitudes by State Mentions 🌎 and Time 📈')
plot_state_time()




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
