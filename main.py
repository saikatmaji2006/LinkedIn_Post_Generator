import streamlit as st
from fewshot import FewShotPosts
from post_generator import generate_post

# ── Page Config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="LinkedIn Post Generator",
    page_icon="💼",
    layout="centered",
)

# ── Custom CSS ───────────────────────────────────────────────────────────────
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

    /* Global */
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    /* Header */
    .hero-title {
        font-size: 2.4rem;
        font-weight: 700;
        background: linear-gradient(135deg, #0A66C2 0%, #004182 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 0.2rem;
    }
    .hero-subtitle {
        text-align: center;
        color: #666;
        font-size: 1.05rem;
        margin-bottom: 2rem;
    }

    /* Post output card */
    .post-card {
        background: linear-gradient(145deg, #f8faff 0%, #eef3ff 100%);
        border-left: 4px solid #0A66C2;
        border-radius: 12px;
        padding: 1.5rem 1.8rem;
        margin-top: 1rem;
        font-size: 0.97rem;
        line-height: 1.7;
        color: #1a1a1a;
        box-shadow: 0 2px 12px rgba(10, 102, 194, 0.08);
        white-space: pre-wrap;
    }

    /* Button */
    .stButton > button {
        background: linear-gradient(135deg, #0A66C2 0%, #004182 100%);
        color: white !important;
        border: none;
        border-radius: 8px;
        padding: 0.6rem 2rem;
        font-weight: 600;
        font-size: 1rem;
        width: 100%;
        transition: all 0.3s ease;
    }
    .stButton > button:hover {
        transform: translateY(-1px);
        box-shadow: 0 4px 15px rgba(10, 102, 194, 0.35);
    }

    /* Footer */
    .footer {
        text-align: center;
        color: #999;
        font-size: 0.82rem;
        margin-top: 3rem;
        padding-top: 1.5rem;
        border-top: 1px solid #eee;
    }
    .footer a { color: #0A66C2; text-decoration: none; }
    </style>
    """,
    unsafe_allow_html=True,
)


# ── App ──────────────────────────────────────────────────────────────────────
def main():
    st.markdown('<p class="hero-title">💼 LinkedIn Post Generator</p>', unsafe_allow_html=True)
    st.markdown(
        '<p class="hero-subtitle">Generate engaging LinkedIn posts powered by AI — '
        'choose your topic, language &amp; length.</p>',
        unsafe_allow_html=True,
    )

    fs = FewShotPosts()

    col1, col2, col3 = st.columns(3)

    with col1:
        selected_tag = st.selectbox("📌 Topic", options=fs.get_tags())
    with col2:
        selected_language = st.selectbox("🌐 Language", options=["English", "Hinglish"])
    with col3:
        selected_length = st.selectbox("📏 Length", options=["Short", "Medium", "Long"])

    st.markdown("")  # spacing

    if st.button("✨ Generate Post"):
        with st.spinner("Crafting your LinkedIn post..."):
            post = generate_post(selected_length.lower(), selected_language, selected_tag)
        st.markdown(f'<div class="post-card">{post}</div>', unsafe_allow_html=True)

        st.markdown("")
        col_a, col_b = st.columns(2)
        with col_a:
            st.download_button(
                label="📥 Download Post",
                data=post,
                file_name="linkedin_post.txt",
                mime="text/plain",
            )
        with col_b:
            if st.button("📋 Copy to Clipboard"):
                st.code(post, language=None)

    st.markdown(
        '<div class="footer">Built with ❤️ using '
        '<a href="https://streamlit.io" target="_blank">Streamlit</a> &amp; '
        '<a href="https://groq.com" target="_blank">Groq LLM</a></div>',
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    main()