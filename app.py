import streamlit as st
import requests
'''
# Polclassifier frontend
'''

predict_url = "https://polclassifier-g4mow3fhiq-ew.a.run.app/predict"
random_speech_url = "https://polclassifier-g4mow3fhiq-ew.a.run.app/predict_speech"

##### Guessing the party #####
api_form = st.form(key='api_form')
speech = api_form.text_input(label="Political speech (400-600 words):", value="")
submitted = api_form.form_submit_button(label='Guess the party!')


# Make the API request when the button is pushed
def make_request(url, params):
    party_key = {
        "Con": "Conservative Party",
        "Lab": "Labour Party",
        "LibDem": "Liberal Democrats",
        "SNP": "Scottish National Party",
        "DUP": "Democratic Unionist Party",
        "UUP": "Ulster Unionist Party",
        "PlaidCymru": "Plaid Cymru"
    }

    response = requests.get(url=url, params=params)
    result = response.json()
    return f"""{party_key[result['party']]}"""

if submitted:
    params = {
        "speech": speech,
    }

    response = make_request(predict_url, params)
    st.markdown(f'### {response}!')
    st.balloons()


##### Retrieving a random speech to test the app on #####
