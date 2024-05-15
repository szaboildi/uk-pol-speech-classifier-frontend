import streamlit as st
import requests

st.markdown("<h1 style='color:#235857'>\"Spoken like a true LibDem!\"</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='color:#235857; margin-top:-1.5rem'><i>Classifying UK Parliamentary Speeches along Party Lines<i></h3>", unsafe_allow_html=True)

predict_url = "https://svm7-pvutvs4yla-ew.a.run.app/predict"
random_speech_url = "https://svm7-pvutvs4yla-ew.a.run.app/speech"


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
party_desc = {
    "Con": "The Conservative Party, or Tories, are one of the UK's two primary political forces. With a core attachment to economic liberalism, they have tended to embrace free-market policies. The party of Churchill, Thatcher and British unionism, their voters are historically conservative on social issues, with strong support among homeowners, farmers and landlords in rural constituencies.",
    "Lab": "The Labour Party are of the UK's two main political entities, second only to the Conservatives in their historical success. Emerging from trade unions and socialism, it has tended to embrace public investment, spending more on health and education than its counterpart, as well as maintaining more socially inclusive ideologies.",
    "LibDem": "Often considered the more \"progressive\" of the major parties, the Lib Dems tend to support socially liberal approaches to cultural issues such as education, criminal rights, LGBT rights and drug liberalisation. Their support tends to come from younger voters, especially in metropolitan constituencies.",
    "SNP": "The Scottish National Party supports and campaigns for Scottish Independence from the United Kingdom, as well as Scottish membership to the European Union. Politically they sit centre-left, with socially progressive policies, and receive the largest share of Scottish support.",
    "DUP": "The Democratic Unionist Party is a Northern Irish political party that supports the union of Northern Ireland with the United Kingdom. They tend to embrace right-wing economic policy, campaigning along socially conservative lines against issues such as abortion and same-sex marriage.",
    "UUP": "The Ulster Unionist Party is the second biggest Unionist party in Northern Ireland, having been overtaken by the DUP in 2003. They were the governing body of Northern Ireland for much of the twentieth century, most notably representing unionist views during the Troubles, and ultimately helping to negotiate the Good Friday Agreement that ended the conflict.",
    "PlaidCymru": "The official party of Wales, Plaid Cymru (pronounced \"plyde KUM-ree\") supports and campaigns for Welsh independence from the United Kingdom. They tend to campaign on centre-left, progressive social policies such as lowering the voting age and free school meals."
}

##### Retrieving a random speech to test the app on #####
st.markdown(f"#### If you don\'t have a speech ready, we can get a random one for you!")

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
    st.markdown(f"##### Here's your speech:")
    st.markdown(f'{response}')
    st.balloons()


##### Guessing the party #####
st.markdown(f'\n\n\n #### Let us guess what party gave your speech!')
api_form_predict = st.form(key='api_form_predict')
speech = api_form_predict.text_input(label="Your parliamentary speech (at least 400 words):", value="")
submitted_predict = api_form_predict.form_submit_button(label='Guess the party!')


# Make the API request when the button is pushed
def make_request_predict(url, params):
    response = requests.get(url=url, params=params)
    result = response.json()
    return f"""{result['party']}"""

if submitted_predict:
    params_predict = {
        "speech": speech,
    }

    response = make_request_predict(predict_url, params_predict)
    st.markdown(f'#### {party_code_to_name[response]}!')
    st.markdown(f'{party_desc[response]}')
    st.balloons()
