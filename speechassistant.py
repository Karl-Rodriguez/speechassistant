import streamlit as st
from google import genai
from google.genai import types

client = genai.Client(api_key=st.secrets["API_KEY"])

background_image = "data:image/jpeg;base64,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Gc49PVeUmm1xRsUAAAAAAAAAAAAAAAAAAAAAAAAZGQAGRkABkZAAZGQAGRkABkZAAZGQAGRkABkZAAZGQAGSZAoJkuQAGRkABkZAAZGQAGRkABkZAAZGQAGRkABkZAAZGQAGRkABkZAAZGQAGRkABkZAAZJkCgZGQAGRkABkZAAZGQAGRkACZLkABkZAAmRkAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEAoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEAoIUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQAUhQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABCgCFIUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQpABSFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEKQAUhQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABCkAFPkoFBCgAQoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAUEyAKCAAAyZA/9k="

code_prompt = (
    "Create and refine business japanese speeches based on user input. "
    "The user may provide instructions, topics, or feedback in English or Japanese, "
    "but you MUST ALWAYS write and output the speech entirely in natural Japanese. "
    "Output ONLY the Japanese speech text without any introductory text, explanations, or concluding remarks."
    "make sure that this is formal and heartfelt."
    "The user is a native japanese speaker so use the words that are commonly used"
    "The user is the highest ranked employee of the company"
    "The user will tell you how long he or she will be speaking in front of his employees. Make it standard for 45minutes long"
    "Do not also force or make the speech redundant. If it can't be stretched to 45minutes minimum long it is okay"
    "Company Background: Company is in Civil Engineering Industry. It caters to consulting, infrastructure and urban design, surveying, and bridge damage analysis"
)

st.set_page_config(
    page_title="日本語ビジネススピーチ支援アシスタント",
    layout="centered",
    initial_sidebar_state="collapsed",
)
_page_css = """
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Noto+Serif+JP:wght@500;700;900&family=Noto+Sans+JP:wght@400;500;700&display=swap" rel="stylesheet">

    <style>
        *{
            box-sizing:border-box;
        }
        :root{
            --ink:#1b2430;
            --ink-soft:#4a5568;
            --line:#0f2a4a;
            --line-dark:#081a30;
            --accent:#9c7a3c;
            --paper:#fbfaf8;
            --card-radius:4px;
        }

        html, body{
            margin:0;
            padding:0;
            overflow-x:hidden;
            width:100%;
            font-family:'Noto Sans JP',sans-serif;
            color:var(--ink);
        }

        /* ---------- Full-screen fixed background, always behind content ---------- */
        [data-testid="stAppViewContainer"]{
            position:relative;
            z-index:0;
            background-color:var(--paper);
        }
        [data-testid="stAppViewContainer"]::before{
            content:"";
            position:fixed;
            top:0; left:0; right:0; bottom:0;
            width:100vw;
            height:100vh;
            background-image:url("__BG_IMAGE__");
            background-repeat:no-repeat;
            background-position:center center;
            background-size:min(70vmin, 480px);
            opacity:0.06;
            z-index:0;
            pointer-events:none;
        }
        [data-testid="stAppViewContainer"] > .main{
            position:relative;
            z-index:1;
        }

        .block-container{
            position:relative;
            z-index:2;
            padding-top:2rem;
            padding-bottom:3rem;
            max-width:760px;
        }

        /* Hide default Streamlit chrome for a cleaner, branded look */
        #MainMenu {visibility:hidden;}
        footer {visibility:hidden;}
        header[data-testid="stHeader"]{background:transparent;}

        /* ---------- Header ---------- */
        .app-header{
            padding:0 0 1.75rem 0;
            margin-bottom:2rem;
            border-bottom:1px solid #dfe2e7;
        }
        .app-header .eyebrow{
            font-size:.72rem;
            font-weight:700;
            letter-spacing:.22em;
            color:var(--accent);
            text-transform:uppercase;
            margin-bottom:.6rem;
        }
        .app-header h1{
            font-family:'Noto Serif JP',serif;
            color:var(--line-dark);
            font-weight:700;
            font-size:clamp(1.35rem, 4vw, 1.9rem);
            margin:0 0 .55rem 0;
            letter-spacing:.01em;
            line-height:1.4;
        }
        .app-header p{
            color:var(--ink-soft);
            font-size:.92rem;
            margin:0;
            line-height:1.7;
        }

        /* ---------- Card sections ---------- */
        .section-card{
            background:#ffffff;
            border:1px solid #e5e7eb;
            border-left:3px solid var(--line);
            border-radius:var(--card-radius);
            padding:1.6rem 1.6rem 1.2rem 1.6rem;
            margin-bottom:1.6rem;
            position:relative;
            z-index:2;
        }
        .section-title{
            font-weight:700;
            font-size:.98rem;
            color:var(--line-dark);
            letter-spacing:.02em;
            margin-bottom:1rem;
            padding-bottom:.6rem;
            border-bottom:1px solid #eef0f3;
        }

        /* ---------- Inputs ---------- */
        .stTextInput input, .stTextArea textarea{
            border-radius:3px !important;
            border:1px solid #d5d9de !important;
            font-size:1rem !important;
            color:var(--ink) !important;
            background-color:#ffffff !important;
        }
        .stTextArea textarea{
            font-family:'Noto Sans JP',sans-serif !important;
            line-height:1.9 !important;
        }
        .stTextInput input:focus, .stTextArea textarea:focus{
            border-color:var(--accent) !important;
            box-shadow:0 0 0 1px var(--accent) !important;
        }
        label, .stTextInput label, .stTextArea label{
            color:var(--ink-soft) !important;
            font-size:.85rem !important;
            font-weight:500 !important;
        }

        /* ---------- Buttons ---------- */
        .stButton > button{
            width:100%;
            background:var(--line-dark);
            color:#ffffff;
            border:none;
            border-radius:3px;
            padding:.7rem 1rem;
            font-weight:600;
            font-size:.92rem;
            letter-spacing:.03em;
            transition:background .15s ease;
            position:relative;
            z-index:2;
        }
        .stButton > button:hover{
            background:var(--line);
        }
        .stButton > button:active{
            background:var(--line-dark);
        }

        /* ---------- Alerts ---------- */
        .stAlert{
            border-radius:3px;
            position:relative;
            z-index:2;
        }

        /* ---------- Footer note ---------- */
        .app-footer{
            text-align:center;
            color:#9aa3ae;
            font-size:.74rem;
            letter-spacing:.03em;
            margin-top:2.5rem;
            padding-top:1.25rem;
            border-top:1px solid #e5e7eb;
            position:relative;
            z-index:2;
        }

        /* =========================================================
           MOBILE RESPONSIVENESS (phones & tablets)
           ========================================================= */
        [data-testid="stAppViewContainer"], .block-container{
            max-width:100%;
        }
        img, .stTextArea textarea, .stTextInput input{
            max-width:100%;
        }

        /* Tablets */
        @media (max-width: 768px){
            .block-container{
                max-width:100%;
                padding-left:1.1rem;
                padding-right:1.1rem;
            }
        }

        /* Phones */
        @media (max-width: 640px){
            .block-container{
                padding-left:.85rem;
                padding-right:.85rem;
                padding-top:.85rem;
                padding-bottom:2rem;
            }
            .app-header{
                padding-bottom:1.25rem;
                margin-bottom:1.25rem;
            }
            .app-header .eyebrow{
                font-size:.66rem;
                letter-spacing:.16em;
            }
            .app-header p{
                font-size:.85rem;
            }
            .section-card{
                padding:1.1rem .95rem;
                margin-bottom:1.1rem;
            }
            .section-title{
                font-size:.9rem;
            }
            .stTextInput input, .stTextArea textarea{
                font-size:16px !important; /* prevents iOS zoom-on-focus */
            }
            .stTextArea textarea{
                max-height:260px;
            }
            .stButton > button{
                padding:.9rem 1rem;
                font-size:1rem;
            }
        }

        /* Small phones */
        @media (max-width: 400px){
            .app-header p{
                font-size:.8rem;
            }
            .section-card{
                padding:.95rem .8rem;
            }
        }
    </style>
    """

st.markdown(
    _page_css.replace("__BG_IMAGE__", background_image),
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="app-header">
        <h1>日本語ビジネススピーチ支援アシスタント</h1>
    </div>
    """,
    unsafe_allow_html=True,
)

if "current_speech" not in st.session_state:
    st.session_state.current_speech = ""

st.markdown(
    '<div class="section-card"><div class="section-title">スピーチテーマ</div>',
    unsafe_allow_html=True,
)
topic = st.text_input("スピーチテーマ", label_visibility="collapsed", placeholder="スピーチのテーマを入力してください")

if st.button("スピーチを生成する"):
    if topic.strip() == "":
        st.warning("トピックを入力してください。")
    else:
        with st.spinner("スピーチを生成しています…"):
            initial_prompt = f"Topic:\n{topic}"
            try:
                response = client.models.generate_content(
                    model='gemini-3.6-flash',
                    contents=initial_prompt,
                    config=types.GenerateContentConfig(
                        system_instruction=code_prompt,
                        temperature=0.7,
                    )
                )
                st.session_state.current_speech = response.text
            except Exception as e:
                st.error(f"エラーが発生しました: {e}")
st.markdown("</div>", unsafe_allow_html=True)

if st.session_state.current_speech:
    st.markdown(
        '<div class="section-card"><div class="section-title">現在の音声出力</div>',
        unsafe_allow_html=True,
    )
    st.text_area("スピーチ本文", st.session_state.current_speech, height=400, label_visibility="collapsed")

    feedback = st.text_area("フィードバックを入力する", label_visibility="collapsed", placeholder="修正してほしい点を入力してください")

    if st.button("スピーチの更新"):
        if feedback.strip() == "":
            st.warning("フィードバックを入力してください。")
        else:
            with st.spinner("フィードバックに基づき、スピーチを修正しています."):
                clear_prompt = f"""
                現在のスピーチ:
                {st.session_state.current_speech}

                Feedback / Comments:
                {feedback}
                """

                try:
                    response = client.models.generate_content(
                        model='gemini-3.6-flash',
                        contents=clear_prompt,
                        config=types.GenerateContentConfig(
                            system_instruction=code_prompt,
                            temperature=0.7,
                        )
                    )

                    st.session_state.current_speech = response.text
                except Exception as e:
                    st.error(f"エラーが発生しました: {e}")

    if st.button("完成"):
        st.success("最終スピーチが作成されました。")
        st.write(st.session_state.current_speech)
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown('<div class="app-footer">社内専用スピーチ作成ツール</div>', unsafe_allow_html=True)