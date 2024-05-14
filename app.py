import streamlit as st
import requests
'''
# Polclassifier frontend
'''

predict_url = "https://svm-pvutvs4yla-ew.a.run.app/predict"
random_speech_url = "https://svm-pvutvs4yla-ew.a.run.app/speech"


party_code_to_name = {
        "Con": "Conservative Party",
        "Lab": "Labour Party",
        "LibDem": "Liberal Democrats",
        "SNP": "Scottish National Party",
        "DUP": "Democratic Unionist Party",
        "UUP": "Ulster Unionist Party",
        "PlaidCymru": "Plaid Cymru"
    }
party_name_to_code = {v: k for k,v in party_code_to_name.items()}


##### Retrieving a random speech to test the app on #####
st.markdown(f"### If you don\'t have a speech ready, we can get a random one for you!")

api_form_random = st.form(key='api_form_random')
party = api_form_random.selectbox(label="Party:", options=party_name_to_code.keys())
submitted_random = api_form_random.form_submit_button(label='Give me a random speech from this party!')


def make_request_random(url, params):
    response = requests.get(url=url, params=params)
    result = response.json()
    return f"""{result["speech"]}"""

if submitted_random:
    params_random = {
        "party": party_name_to_code[party],
    }

    response = make_request_random(random_speech_url, params_random)
    st.markdown(f"#### Here's your speech:")
    st.markdown(f'{response}')
    st.balloons()


##### Guessing the party #####
st.markdown(f'\n\n\n ### Let us guess what party gave your speech!')
api_form_predict = st.form(key='api_form_predict')
speech = api_form_predict.text_input(label="Your political speech (400-600 words):", value="")
submitted_predict = api_form_predict.form_submit_button(label='Guess the party!')


# Make the API request when the button is pushed
def make_request_predict(url, params, parties):
    response = requests.get(url=url, params=params)
    result = response.json()
    return f"""{parties[result['party']]}"""

if submitted_predict:
    params_predict = {
        "speech": speech,
    }

    response = make_request_predict(predict_url, params_predict, party_code_to_name)
    st.markdown(f'### {response}!')
    st.balloons()
