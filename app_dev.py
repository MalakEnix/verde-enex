import streamlit as st
from huggingface_hub import InferenceClient

client = InferenceClient(
    token=st.secrets["HF_TOKEN"]
)
import pandas as pd
import shap
import streamlit.components.v1 as components
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
import numpy as np


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="verde·ENEX",
    page_icon="🌿",
    layout="wide"
)


# =========================================================
# VERDE·ENEX — LIVING ENVIRONMENTAL INTELLIGENCE
# =========================================================

import base64
import streamlit.components.v1 as components


# =========================================================
# ENIX ASSETS
# =========================================================

with open("enix_voice.mp3", "rb") as audio_file:
    audio_base64 = base64.b64encode(
        audio_file.read()
    ).decode()

with open("enix.png", "rb") as image_file:
    image_base64 = base64.b64encode(
        image_file.read()
    ).decode()

# =========================================================
# VERDE·ENEX — LIVING ENVIRONMENTAL INTELLIGENCE
# =========================================================

import base64
import streamlit.components.v1 as components


# =========================================================
# ENIX ASSETS
# =========================================================

with open("enix_voice.mp3", "rb") as audio_file:
    audio_base64 = base64.b64encode(
        audio_file.read()
    ).decode()

with open("enix.png", "rb") as image_file:
    image_base64 = base64.b64encode(
        image_file.read()
    ).decode()


# =========================================================
# LIVING ENVIRONMENTAL UI
# =========================================================

st.markdown(
    """
    <style>

    /* ---------- GLOBAL ---------- */

    .stApp {
        background:
            radial-gradient(
                circle at 50% 5%,
                rgba(0, 201, 151, 0.18),
                transparent 35%
            ),
            linear-gradient(
                180deg,
                #03120e 0%,
                #061c17 55%,
                #020b08 100%
            );
    }

    .block-container {
        padding-top: 1.2rem;
        padding-bottom: 5rem;
    }


    /* ---------- MAIN GLASS ---------- */

    .enix-panel {
        max-width: 1100px;
        margin: 0 auto;
        padding: 30px 30px 24px 30px;

        border-radius: 30px;

        background:
            linear-gradient(
                145deg,
                rgba(17, 61, 51, 0.72),
                rgba(3, 22, 17, 0.78)
            );

        border: 1px solid rgba(0, 201, 151, 0.22);

        box-shadow:
            0 25px 70px rgba(0, 0, 0, 0.45),
            inset 0 1px 0 rgba(255,255,255,0.06);

        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);

        text-align: center;
    }


    /* ---------- BRAND ---------- */

    .enix-brand {
        color: #00c997;
        font-size: 43px;
        font-weight: 800;
        letter-spacing: 1px;

        text-shadow:
            0 0 25px rgba(0,201,151,0.25);

        margin: 0;
    }


    .enix-intelligence {
        color: #c8eee5;
        font-size: 12px;
        font-weight: 500;

        letter-spacing: 4px;
        text-transform: uppercase;

        margin-top: 5px;
    }


    /* ---------- ENIX ---------- */

    .enix-name {
        color: #f0fff9;
        font-size: 26px;
        font-weight: 700;

        margin-top: 18px;
    }


    .enix-role {
        color: #86cbbd;
        font-size: 13px;

        letter-spacing: 1px;

        margin-top: 2px;
    }


    /* ---------- SPEAKING ---------- */

    .enix-speaking {
        text-align: center;

        color: #ecfff9;

        font-size: 18px;
        font-weight: 600;

        margin-top: 12px;

        text-shadow:
            0 0 15px rgba(0,201,151,0.25);
    }


    .enix-line {
        width: 95px;
        height: 2px;

        margin: 9px auto;

        background:
            linear-gradient(
                90deg,
                transparent,
                #00c997,
                transparent
            );

        box-shadow:
            0 0 14px rgba(0,201,151,0.7);
    }


    .enix-prompt {
        text-align: center;

        color: #78aea3;

        font-size: 13px;

        margin-bottom: 12px;
    }


    /* ---------- CHAT ---------- */

div[data-testid="stChatInput"],
div[data-testid="stBottom"] > div,
div[data-testid="stBottomBlockContainer"] {
    background: rgba(5, 29, 24, 0.94) !important;
}

div[data-testid="stChatInput"] {
    border: 1px solid rgba(0, 201, 151, 0.38) !important;
    border-radius: 18px !important;
    box-shadow: 0 0 28px rgba(0, 201, 151, 0.10) !important;
}

div[data-testid="stChatInput"] textarea {
    color: #eafff9 !important;
    background: transparent !important;
}

div[data-testid="stChatInput"] textarea::placeholder {
    color: #72a99d !important;
}

    /* ---------- SELECTBOX ---------- */

    div[data-testid="stSelectbox"] > div {
        border-radius: 14px;
    }


    /* ---------- FOOTER ---------- */

    .enix-footer {
        text-align: center;

        margin-top: 22px;

        color: #4f8d80;

        font-size: 10px;

        letter-spacing: 4px;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# ENIX BRAND

st.markdown(
    """
    <h1 style="
        color:#00E5A8;
        text-align:center;
        font-size:44px;
        font-weight:900;
        letter-spacing:2px;
        margin-bottom:0px;
    ">
        verde·ENEX
    </h1>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <p style="
        color:#45B7FF;
        text-align:center;
        font-size:17px;
        font-weight:600;
        letter-spacing:4px;
        margin-top:0px;
        margin-bottom:8px;
    ">
        ENVIRONMENTAL INTELLIGENCE
    </p>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <h2 style="
        color:#B56CFF;
        text-align:center;
        font-size:38px;
        font-weight:900;
        margin-top:8px;
        margin-bottom:0px;
    ">
        Enix
    </h2>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <p style="
        color:#FFD166;
        text-align:center;
        font-size:15px;
        font-weight:500;
        margin-top:2px;
    ">
        Your Intelligent Environmental Assistant
    </p>
    """,
    unsafe_allow_html=True
)

# =========================================================
# ENIX ROBOT
# =========================================================

components.html(
    f"""
    <html>

    <head>

        <style>

            html, body {{
                margin: 0;
                padding: 0;

                background: transparent;

                overflow: hidden;
            }}

            .robot-zone {{

                height: 260px;

                display: flex;

                justify-content: center;

                align-items: center;

                position: relative;
            }}

            .robot-zone::before {{

                content: "";

                position: absolute;

                width: 210px;
                height: 210px;

                border-radius: 50%;

                background:
                    radial-gradient(
                        circle,
                        rgba(0,201,151,0.20),
                        rgba(0,201,151,0.05) 45%,
                        transparent 70%
                    );

                animation:
                    pulse 4s ease-in-out infinite;
            }}

            @keyframes pulse {{

                0%,100% {{
                    transform: scale(0.90);
                    opacity: 0.55;
                }}

                50% {{
                    transform: scale(1.08);
                    opacity: 1;
                }}

            }}

            .robot {{

                width: 205px;

                position: relative;

                z-index: 2;

                cursor: pointer;

                transition:
                    transform 0.25s ease,
                    filter 0.25s ease;
            }}

            .robot:hover {{

                transform: scale(1.07);

                filter:
                    drop-shadow(
                        0 0 22px
                        rgba(0,201,151,0.9)
                    );
            }}

        </style>

    </head>

    <body>

        <div class="robot-zone">

            <img
                id="robot"
                class="robot"
                src="data:image/png;base64,{image_base64}"
            >

            <audio id="voice">

                <source
                    src="data:audio/mpeg;base64,{audio_base64}"
                    type="audio/mpeg"
                >

            </audio>

        </div>

        <script>

            const robot =
                document.getElementById("robot");

            const voice =
                document.getElementById("voice");

            robot.onclick = function() {{

                voice.currentTime = 0;

                voice.play();

                robot.style.transform =
                    "scale(0.94)";

                setTimeout(function() {{

                    robot.style.transform =
                        "scale(1.04)";

                }}, 150);

            }};

        </script>

    </body>

    </html>
    """,
    height=265
)


# =========================================================
# ENIX LIVING MESSAGE
# =========================================================

st.markdown(
    """
    <div class="enix-speaking">
        The environment is speaking.
    </div>

    <div class="enix-line"></div>

    <div class="enix-prompt">
        Ask Enix anything.
    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# EXPLORATION MENU
# =========================================================

mode = st.selectbox(
    "🔎 Explore verde·ENEX",
    [
        "🏠 Home",
        "🔮 Predict Pollution",
        "🌍 Analyze Air Quality",
        "🧠 Explain AI Prediction",
        "📈 Explore Trends",
        "🚨 Detect Anomalies",
        "🔬 Model Intelligence"
    ]
)


# =========================================================
# ENIX CONVERSATION
# =========================================================

if "enix_messages" not in st.session_state:

    st.session_state.enix_messages = []


for message in st.session_state.enix_messages:

    with st.chat_message(message["role"]):

        st.markdown(
            message["content"]
        )
st.markdown(
    """
    <style>

    div.stButton > button {
        background: radial-gradient(
            circle,
            #00E5A8 0%,
            #00A67E 55%,
            #063D32 100%
        ) !important;
        color: white !important;
        border: 2px solid #7FFFD4 !important;
        border-radius: 50% !important;
        width: 72px !important;
        height: 72px !important;
        font-size: 28px !important;
        box-shadow:
            0 0 18px rgba(0,229,168,0.65),
            0 0 40px rgba(0,229,168,0.25) !important;
        margin: 10px auto !important;
        display: block !important;
        transition: all 0.25s ease !important;
    }

    div.stButton > button:hover {
        transform: scale(1.08);
        box-shadow:
            0 0 25px rgba(0,229,168,0.85),
            0 0 55px rgba(0,229,168,0.35) !important;
    }

    </style>
    """,
    unsafe_allow_html=True
)

if "show_enix_input" not in st.session_state:
    st.session_state.show_enix_input = False

user_question = None

if not st.session_state.show_enix_input:

    if st.button("💬", key="open_enix_chat"):
        st.session_state.show_enix_input = True
        st.rerun()

if st.session_state.show_enix_input:

    st.markdown(
        """
        <style>
        div[data-testid="stTextInput"] {
            background: rgba(3, 45, 38, 0.96) !important;
            border: 1px solid #00E5A8 !important;
            border-radius: 16px !important;
            box-shadow:
                0 0 15px rgba(0,229,168,0.20),
                inset 0 0 12px rgba(0,229,168,0.05) !important;
        }
        div[data-testid="stTextInput"] * {
            background: transparent !important;
        }
        div[data-testid="stTextInput"] input {
            color: #EFFFFA !important;
            -webkit-text-fill-color: #EFFFFA !important;
            caret-color: #00E5A8 !important;
        }
        div[data-testid="stTextInput"] input::placeholder {
            color: #78CDBA !important;
            -webkit-text-fill-color: #78CDBA !important;
            opacity: 1 !important;
        }
        div.stFormSubmitButton > button {
            background: radial-gradient(circle, #00E5A8 0%, #00A67E 60%, #063D32 100%) !important;
            color: #032B24 !important;
            border: 1px solid #7FFFD4 !important;
            border-radius: 50% !important;
            width: 44px !important;
            height: 44px !important;
            font-size: 18px !important;
            font-weight: 900 !important;
            box-shadow: 0 0 12px rgba(0,229,168,0.5) !important;
            padding: 0 !important;
        }
        div.stFormSubmitButton > button:hover {
            box-shadow: 0 0 20px rgba(0,229,168,0.8) !important;
        }
        div[data-testid="stMarkdownContainer"] p,
        div[data-testid="stMarkdownContainer"] li,
        div[data-testid="stMarkdownContainer"] span,
        div[data-testid="stMarkdownContainer"] strong {
            color: #EFFFFA !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    with st.form("enix_conversation_form", clear_on_submit=True):

        col1, col2 = st.columns([10, 1])

        with col1:
            user_question = st.text_input(
                "Ask Enix anything",
                placeholder="Ask about air quality, pollution, ozone, trends...",
                label_visibility="collapsed"
            )

        with col2:
            send = st.form_submit_button("➤")

        if not send:
            user_question = None

# =========================================================
# ENIX AI
# =========================================================

if user_question:

    st.session_state.enix_messages.append(
        {"role": "user", "content": user_question}
    )

    with st.chat_message("user", avatar="enix_star.png"):
        st.markdown(
            f'<div dir="auto" style="color:#EFFFFA;">{user_question}</div>',
            unsafe_allow_html=True
        )

    system_prompt = """
IDENTITY AND PERSONALITY

You are Enix, the intelligent environmental assistant of
verde·ENEX, developed by Aouabdi Malak.

You have a distinct, recognizable, confident, warm, and professional
personality. Your presence should be clear from your very first sentence.
You are not a generic chatbot.

Introduce yourself naturally when someone asks who you are.
Explain that you are the environmental intelligence assistant of
verde·ENEX, designed to help people understand environmental data,
air pollution, atmospheric conditions, and AI-based predictions.

Speak with confidence, clarity, composure, and purpose.
Be friendly without being childish, professional without being cold,
and engaging without exaggerating your abilities.

RELIGIOUS AND CULTURAL COURTESY

When a user asks how you are, respond entirely in ONE language
matching their message:
- If in Arabic: "الحمد لله، أنا بخير وجاهز لمساعدتك!"
- If in English: "Alhamdulillah, I'm doing great and ready to help!"
- If in French: "Alhamdulillah, je vais bien et prêt à vous aider !"

Never mix Arabic script with English or French in the same sentence.
Use this expression respectfully, not in every single answer.
Respect the beliefs and cultural preferences of every user.

MULTILINGUAL INTELLIGENCE

Communicate fluently and naturally in Arabic, English, and French.
You may also respond in another language when you can do so reliably.

Always answer in the language the user is currently using.
If the user switches languages, switch with them.
If the user mixes Arabic, French, and English, understand the meaning
and respond naturally in the most appropriate language.

Do not unnecessarily translate everything into multiple languages.
Provide translations when the user asks for them or when they help.

ENVIRONMENTAL EXPERTISE

Your main domain is environmental intelligence, especially:
- Air quality and air pollution.
- Ozone (O3), nitrogen dioxide (NO2), sulfur dioxide (SO2), and CO.
- Meteorological variables and atmospheric chemistry.
- Environmental data analysis and visualization.
- Monthly and seasonal trends.
- Anomaly detection and unusual environmental patterns.
- Satellite observations, environmental maps, and wildfire data.
- Machine learning, model evaluation, and explainable AI.
- Environmental risk communication and early-warning concepts.

Help users understand not only what the data shows, but also
what it may mean scientifically.

SCIENTIFIC INTEGRITY

Never invent measurements, observations, model predictions,
calculations, citations, or results from verde·ENEX.

Clearly distinguish:
1. Observed data.
2. Model predictions.
3. Scientific interpretations.
4. Hypotheses that require further investigation.

When project data is unavailable, say so clearly and explain
what information would be needed.

Never describe R-squared as prediction accuracy.
Explain it as the proportion of variance explained by a model
on the evaluated dataset.

Do not claim that correlation proves causation.
Do not guarantee future environmental outcomes.
Explain uncertainty confidently and clearly, without sounding evasive.

RESPONSE STYLE

Start with a direct answer rather than a generic introduction.
Use strong, natural sentences and meaningful explanations.
Avoid repetitive greetings, empty phrases, and unnecessary disclaimers.
Adapt the level of detail to the question being asked.

For simple questions, answer concisely.
For scientific questions, explain the mechanisms and evidence.
For complex questions, organize the response into clear steps.
When useful, give a practical example or a short summary.

Do not repeat the same answer several times.
Do not claim to have analyzed live data, maps, or files unless
those results are actually available to you.

RELATIONSHIP WITH THE USER

Treat the user with respect, patience, and intellectual honesty.
Help them understand the reasoning instead of merely giving conclusions.
When correcting a misunderstanding, be clear and constructive.
Never pretend to be human or claim personal experiences.

CORE MISSION

You are Enix: the environmental intelligence voice of verde·ENEX.

Your mission is to help people sense environmental changes,
understand the evidence, interpret predictions, and make
better-informed environmental decisions.

Your guiding motto is:
"SENSE. PREDICT. PROTECT."
"""

    messages = [{"role": "system", "content": system_prompt}]
    messages.extend(st.session_state.enix_messages)

    try:
        response = client.chat.completions.create(
            model="meta-llama/Llama-3.1-8B-Instruct",
            messages=messages,
            temperature=0.4
        )
        answer = response.choices[0].message.content
    except Exception:
        answer = (
            "I'm temporarily unable to connect "
            "to my environmental intelligence service."
        )

    st.session_state.enix_messages.append(
        {"role": "assistant", "content": answer}
    )

    with st.chat_message("assistant", avatar="enix_star.png"):
        st.markdown(
            f'<div dir="auto" style="color:#EFFFFA;">{answer}</div>',
            unsafe_allow_html=True
        )

# =========================================================
# FOOTER
# =========================================================

st.markdown(
    """
    <div class="enix-footer">
        SENSE * PREDICT * PROTECT
    </div>
    """,
    unsafe_allow_html=True
)

# =========================================================
# AI PREDICTION
# =========================================================

if mode == "🔮 Predict Pollution":

    st.header("🧠 AI Prediction")

    st.write(
        "Predict ozone concentration using environmental "
        "and atmospheric conditions."
    )

    col1, col2 = st.columns(2)

    with col1:

        Year = st.number_input(
            "Year",
            min_value=2019,
            max_value=2100,
            value=2026
        )

        Month = st.number_input(
            "Month",
            min_value=1,
            max_value=12,
            value=1
        )

        NO2 = st.number_input(
            "NO₂",
            value=0.0
        )

        SO2 = st.number_input(
            "SO₂",
            value=0.0
        )

        CO = st.number_input(
            "CO",
            value=0.0
        )

    with col2:

        Temp_C = st.number_input(
            "Temperature (°C)",
            value=20.0
        )

        RH = st.number_input(
            "Humidity (%)",
            value=50.0
        )

        Solar_Rad = st.number_input(
            "Solar Radiation",
            value=0.0
        )

        WindSpeed = st.number_input(
            "Wind Speed",
            value=0.0
        )

        Pressure_hPa = st.number_input(
            "Pressure (hPa)",
            value=1013.0
        )

    st.write("")

    if st.button(
        "🔮 Predict O₃",
        use_container_width=True
    ):

        input_data = pd.DataFrame(
            [[
                Year,
                Month,
                NO2,
                SO2,
                CO,
                Temp_C,
                RH,
                Solar_Rad,
                WindSpeed,
                Pressure_hPa
            ]],
            columns=features
        )

        prediction = model.predict(
            input_data
        )[0]

        # Save prediction
        st.session_state.last_prediction = prediction

        st.session_state.last_input = input_data

        # Risk
        if prediction < 0.05:

            risk = "Low"

        elif prediction < 0.10:

            risk = "Moderate"

        elif prediction < 0.15:

            risk = "High"

        else:

            risk = "Very High"

        st.session_state.last_risk = risk

        st.success(
            f"Predicted O₃ Value: {prediction:.6g}"
        )

        st.metric(
            "Environmental Risk",
            risk
        )

        # =================================================
        # SHAP
        # =================================================

        st.subheader(
            "🧠 AI Prediction Explanation"
        )

        st.write(
            "These factors explain how the AI model "
            "arrived at this specific prediction."
        )

        explainer = shap.TreeExplainer(
            model
        )

        shap_values = explainer.shap_values(
            input_data
        )

        shap_values = np.asarray(
            shap_values
        )

        if shap_values.ndim == 3:

            shap_values = shap_values[0]

        if shap_values.ndim == 2:

            shap_values = shap_values[0]

        explanation = pd.DataFrame(
            {
                "Variable": features,
                "SHAP Impact": shap_values
            }
        )

        explanation["Absolute Impact"] = (
            explanation["SHAP Impact"].abs()
        )

        explanation = explanation.sort_values(
            by="Absolute Impact",
            ascending=False
        )

        st.dataframe(
            explanation[
                [
                    "Variable",
                    "SHAP Impact"
                ]
            ],
            use_container_width=True
        )

        st.subheader(
            "📊 Factors Influencing This Prediction"
        )

        st.bar_chart(
            explanation.set_index(
                "Variable"
            )["SHAP Impact"]
        )

        strongest_factor = explanation.iloc[0]

        factor_name = strongest_factor[
            "Variable"
        ]

        factor_impact = strongest_factor[
            "SHAP Impact"
        ]

        if factor_impact > 0:

            direction = "increased"

        elif factor_impact < 0:

            direction = "decreased"

        else:

            direction = "had almost no effect on"

        st.info(
            f"🤖 AI Insight: **{factor_name}** was the "
            f"strongest factor affecting this prediction "
            f"and {direction} the predicted O₃ level."
        )


# =========================================================
# EXPLAIN AI PREDICTION
# =========================================================

if mode == "🧠 Explain AI Prediction":

    st.header(
        "🧠 Explainable AI"
    )

    if (
        st.session_state.last_prediction
        is None
        or st.session_state.last_input
        is None
    ):

        st.info(
            "First make an O₃ prediction from "
            "'🔮 Predict Pollution'."
        )

    else:

        prediction = (
            st.session_state.last_prediction
        )

        input_data = (
            st.session_state.last_input
        )

        risk = (
            st.session_state.last_risk
        )

        st.success(
            f"Last Predicted O₃: {prediction:.6g}"
        )

        st.metric(
            "Risk Level",
            risk
        )

        explainer = shap.TreeExplainer(
            model
        )

        shap_values = explainer.shap_values(
            input_data
        )

        shap_values = np.asarray(
            shap_values
        )

        if shap_values.ndim == 3:

            shap_values = shap_values[0]

        if shap_values.ndim == 2:

            shap_values = shap_values[0]

        explanation = pd.DataFrame(
            {
                "Variable": features,
                "SHAP Impact": shap_values
            }
        )

        explanation["Absolute Impact"] = (
            explanation["SHAP Impact"].abs()
        )

        explanation = explanation.sort_values(
            by="Absolute Impact",
            ascending=False
        )

        st.subheader(
            "Factors Influencing This Prediction"
        )

        st.bar_chart(
            explanation.set_index(
                "Variable"
            )["SHAP Impact"]
        )

        strongest_factor = explanation.iloc[0]

        if strongest_factor["SHAP Impact"] > 0:

            direction = "increased"

        else:

            direction = "decreased"

        st.info(
            f"🤖 Enix Insight: "
            f"**{strongest_factor['Variable']}** "
            f"was the strongest factor and "
            f"{direction} the predicted O₃ level."
        )


# =========================================================
# AIR QUALITY ANALYSIS
# =========================================================

if mode == "🌍 Analyze Air Quality":

    st.header(
        "🌍 Air Quality Intelligence"
    )

    pollutants = {
        "O₃": "O3",
        "NO₂": "NO2",
        "SO₂": "SO2",
        "CO": "CO"
    }

    selected_pollutant = st.selectbox(
        "Select pollutant",
        list(pollutants.keys())
    )

    pollutant = pollutants[
        selected_pollutant
    ]

    analysis = df[
        [
            "Year",
            "Month",
            pollutant
        ]
    ].dropna()

    if len(analysis) > 0:

        years = sorted(
            analysis["Year"]
            .astype(int)
            .unique()
        )

        selected_year = st.selectbox(
            "Select year",
            years
        )

        year_data = analysis[
            analysis["Year"]
            == selected_year
        ]

        st.subheader(
            f"📅 {selected_pollutant} — "
            f"{selected_year}"
        )

        yearly_mean = (
            year_data[pollutant].mean()
        )

        yearly_max = (
            year_data[pollutant].max()
        )

        yearly_min = (
            year_data[pollutant].min()
        )

        col1, col2, col3 = st.columns(3)

        with col1:

            st.metric(
                "Yearly Average",
                f"{yearly_mean:.6g}"
            )

        with col2:

            st.metric(
                "Highest Value",
                f"{yearly_max:.6g}"
            )

        with col3:

            st.metric(
                "Lowest Value",
                f"{yearly_min:.6g}"
            )

        st.subheader(
            "📈 Monthly Change"
        )

        monthly_year = (
            year_data
            .sort_values("Month")
            .set_index("Month")[
                [pollutant]
            ]
        )

        st.line_chart(
            monthly_year
        )

        # Automatic analysis

        st.subheader(
            "🤖 Automatic Analysis"
        )

        highest_month_row = year_data.loc[
            year_data[pollutant].idxmax()
        ]

        lowest_month_row = year_data.loc[
            year_data[pollutant].idxmin()
        ]

        highest_month = int(
            highest_month_row["Month"]
        )

        lowest_month = int(
            lowest_month_row["Month"]
        )

        highest_value = (
            highest_month_row[pollutant]
        )

        lowest_value = (
            lowest_month_row[pollutant]
        )

        difference_value = (
            highest_value
            - lowest_value
        )

        if lowest_value != 0:

            change_percent = (
                difference_value
                / abs(lowest_value)
            ) * 100

        else:

            change_percent = 0

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "Highest Month",
                f"Month {highest_month}"
            )

            st.metric(
                "Highest Value",
                f"{highest_value:.6g}"
            )

        with col2:

            st.metric(
                "Lowest Month",
                f"Month {lowest_month}"
            )

            st.metric(
                "Lowest Value",
                f"{lowest_value:.6g}"
            )

        st.write(
            f"Difference between highest and lowest "
            f"monthly values: "
            f"**{change_percent:.2f}%**"
        )

        st.info(
            f"🤖 Enix Insight: During {selected_year}, "
            f"{selected_pollutant} reached its highest "
            f"level in month {highest_month} and its "
            f"lowest level in month {lowest_month}."
        )

        # Yearly average

        st.subheader(
            "📊 Yearly Average Comparison"
        )

        yearly_average = (
            analysis
            .groupby("Year")[pollutant]
            .mean()
        )

        st.bar_chart(
            yearly_average
        )

        # Year comparison

        study_average = (
            analysis[pollutant].mean()
        )

        if study_average != 0:

            difference_percent = (
                (yearly_mean - study_average)
                / abs(study_average)
            ) * 100

        else:

            difference_percent = 0

        year_rank = (
            yearly_average
            .rank(
                ascending=False,
                method="min"
            )[selected_year]
        )

        st.subheader(
            "🔎 Year Comparison"
        )

        col1, col2, col3 = st.columns(3)

        with col1:

            st.metric(
                "Selected Year Average",
                f"{yearly_mean:.6g}"
            )

        with col2:

            st.metric(
                "Study Period Average",
                f"{study_average:.6g}"
            )

        with col3:

            st.metric(
                "Difference",
                f"{difference_percent:+.2f}%"
            )

        if difference_percent > 0:

            st.warning(
                f"In {selected_year}, "
                f"{selected_pollutant} was "
                f"{difference_percent:.2f}% higher "
                f"than the study-period average."
            )

        elif difference_percent < 0:

            st.success(
                f"In {selected_year}, "
                f"{selected_pollutant} was "
                f"{abs(difference_percent):.2f}% lower "
                f"than the study-period average."
            )

        else:

            st.info(
                f"In {selected_year}, "
                f"{selected_pollutant} was approximately "
                f"equal to the study-period average."
            )

        st.write(
            f"🏆 Rank of {selected_year}: "
            f"**#{int(year_rank)}**"
        )

        # Monthly average

        st.subheader(
            "📅 Average by Month"
        )

        monthly_average = (
            analysis
            .groupby("Month")[pollutant]
            .mean()
        )

        st.bar_chart(
            monthly_average
        )

    else:

        st.warning(
            "No data available for this pollutant."
        )


# =========================================================
# TRENDS
# =========================================================

if mode == "📈 Explore Trends":

    st.header(
        "📈 Environmental Trends"
    )

    pollutants = {
        "O₃": "O3",
        "NO₂": "NO2",
        "SO₂": "SO2",
        "CO": "CO"
    }

    selected_pollutant = st.selectbox(
        "Select pollutant",
        list(pollutants.keys())
    )

    pollutant = pollutants[
        selected_pollutant
    ]

    trend_data = df[
        [
            "Year",
            "Month",
            pollutant
        ]
    ].dropna()

    yearly_average = (
        trend_data
        .groupby("Year")[pollutant]
        .mean()
    )

    monthly_average = (
        trend_data
        .groupby("Month")[pollutant]
        .mean()
    )

    st.subheader(
        "📊 Yearly Trend"
    )

    st.bar_chart(
        yearly_average
    )

    st.subheader(
        "📅 Monthly Trend"
    )

    st.line_chart(
        monthly_average
    )


# =========================================================
# ANOMALY DETECTION
# =========================================================

if mode == "🚨 Detect Anomalies":

    st.header(
        "🚨 Environmental Anomaly Detection"
    )

    pollutants = {
        "O₃": "O3",
        "NO₂": "NO2",
        "SO₂": "SO2",
        "CO": "CO"
    }

    selected_pollutant = st.selectbox(
        "Select pollutant",
        list(pollutants.keys())
    )

    pollutant = pollutants[selected_pollutant]

    analysis = df[
        [
            "Year",
            "Month",
            pollutant
        ]
    ].dropna()

    years = sorted(
        analysis["Year"]
        .astype(int)
        .unique()
    )

    if len(years) > 0:

        selected_year = st.selectbox(
            "Select year",
            years
        )

        selected_year_data = analysis[
            analysis["Year"] == selected_year
        ].copy()

        # -------------------------------------------------
        # ANOMALY CALCULATION
        # -------------------------------------------------

        if len(selected_year_data) >= 3:

            mean_value = (
                selected_year_data[pollutant]
                .mean()
            )

            std_value = (
                selected_year_data[pollutant]
                .std()
            )

            if std_value > 0:

                selected_year_data["Deviation"] = (
                    selected_year_data[pollutant]
                    - mean_value
                ) / std_value

                selected_year_data["Anomaly"] = (
                    selected_year_data["Deviation"].abs() >= 2
                )

                anomalies = selected_year_data[
                    selected_year_data["Anomaly"]
                ]

                normal_count = (
                    len(selected_year_data)
                    - len(anomalies)
                )

                # -------------------------------------------------
                # SUMMARY
                # -------------------------------------------------

                col1, col2, col3 = st.columns(3)

                with col1:
                    st.metric(
                        "Total Observations",
                        len(selected_year_data)
                    )

                with col2:
                    st.metric(
                        "Anomalies Detected",
                        len(anomalies)
                    )

                with col3:
                    st.metric(
                        "Normal Observations",
                        normal_count
                    )

                # -------------------------------------------------
                # CHART
                # -------------------------------------------------

                st.subheader(
                    "📈 Monthly Anomaly Analysis"
                )

                chart_data = selected_year_data.set_index(
                    "Month"
                )[[pollutant]]

                st.line_chart(chart_data)

                # -------------------------------------------------
                # ANOMALIES
                # -------------------------------------------------

                if len(anomalies) > 0:

                    st.warning(
                        f"⚠️ {len(anomalies)} unusual environmental "
                        f"observation(s) detected for "
                        f"{selected_pollutant} in {selected_year}."
                    )

                    st.subheader(
                        "🚨 Detected Anomalies"
                    )

                    st.dataframe(
                        anomalies[
                            [
                                "Month",
                                pollutant,
                                "Deviation"
                            ]
                        ],
                        use_container_width=True
                    )

                else:

                    st.success(
                        f"✅ No significant anomalies were detected "
                        f"for {selected_pollutant} in {selected_year}."
                    )

            else:

                st.warning(
                    "No variation was detected in the selected data."
                )

        else:

            st.warning(
                "Not enough data available for anomaly detection."
            )

    else:

        st.warning(
            "No valid data available for anomaly detection."
        )


# =========================================================
# MODEL INTELLIGENCE
# =========================================================

if mode == "🔬 Model Intelligence":

    st.header("🔬 Model Intelligence")

    st.write(
        "Explore the performance and key drivers of the "
        "environmental prediction model."
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "R² Score",
            f"{r2:.3f}"
        )

    with col2:
        st.metric(
            "RMSE",
            f"{rmse:.6g}"
        )

    with col3:
        st.metric(
            "MAE",
            f"{mae:.6g}"
        )

    st.divider()

    st.subheader("📊 Model Performance")

    performance_data = pd.DataFrame(
        {
            "Metric": [
                "R² Score",
                "RMSE",
                "MAE"
            ],
            "Value": [
                r2,
                rmse,
                mae
            ]
        }
    )

    st.dataframe(
        performance_data,
        use_container_width=True,
        hide_index=True
    )

    st.divider()

    st.subheader("🧠 Feature Importance")

    importance = pd.DataFrame(
        {
            "Variable": features,
            "Importance": model.feature_importances_
        }
    )

    importance = importance.sort_values(
        by="Importance",
        ascending=False
    )

    st.bar_chart(
        importance.set_index(
            "Variable"
        )["Importance"]
    )

    strongest_variable = importance.iloc[0]

    st.info(
        f"🤖 Enix Insight: **{strongest_variable['Variable']}** "
        f"is currently the most influential variable in "
        f"the prediction model."
    )