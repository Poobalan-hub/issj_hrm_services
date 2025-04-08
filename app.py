import streamlit as st
import pandas as pd
import os
from io import BytesIO
from datetime import datetime

# ---- ページの設定 ----
st.set_page_config(
    page_title="ISSJ HRM Services",
    page_icon="��",
    layout="wide"
)

# ---- カスタムCSS ----
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #E6E6FA 0%, #D8BFD8 50%, #E6E6FA 100%);
        background-size: 400% 400%;
        animation: gradient 15s ease infinite;
    }
    @keyframes gradient {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    .main {
        padding: 2rem;
        background-color: rgba(255, 255, 255, 0.95);
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #9370DB;
        color: white;
        border: none;
    }
    .stButton>button:hover {
        background-color: #8A2BE2;
    }
    .upload-section {
        background-color: rgba(255, 255, 255, 0.9);
        padding: 2rem;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
    .info-box {
        background-color: rgba(147, 112, 219, 0.1);
        padding: 1rem;
        border-radius: 5px;
        margin: 1rem 0;
        border: 1px solid #9370DB;
    }
    /* Enhanced Tab Styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 1rem;
        padding: 0.5rem;
        background-color: rgba(255, 255, 255, 0.8);
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
    .stTabs [data-baseweb="tab"] {
        height: 60px;
        white-space: pre-wrap;
        background-color: rgba(255, 255, 255, 0.9);
        border-radius: 8px;
        gap: 1rem;
        padding: 0.5rem 1.5rem;
        margin: 0.2rem;
        transition: all 0.3s ease;
        border: 1px solid rgba(147, 112, 219, 0.5);
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
    }
    .stTabs [data-baseweb="tab"]:hover {
        background-color: rgba(147, 112, 219, 0.1);
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    .stTabs [aria-selected="true"] {
        background-color: rgba(147, 112, 219, 0.2);
        color: #8A2BE2;
        border: 2px solid #8A2BE2;
        box-shadow: 0 4px 8px rgba(138, 43, 226, 0.2);
        font-weight: bold;
    }
    .stTabs [data-baseweb="tab"]:before {
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: linear-gradient(45deg, rgba(147,112,219,0.1), rgba(138,43,226,0.1));
        border-radius: 8px;
        opacity: 0;
        transition: opacity 0.3s ease;
    }
    .stTabs [data-baseweb="tab"]:hover:before {
        opacity: 1;
    }
    .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
        color: #8A2BE2;
    }
    .stSuccess {
        background-color: rgba(144, 238, 144, 0.2);
        border: 1px solid #90ee90;
    }
    .stInfo {
        background-color: rgba(173, 216, 230, 0.2);
        border: 1px solid #add8e6;
    }
    </style>
    """, unsafe_allow_html=True)

# ---- ヘッダー ----
col1, col2 = st.columns([1, 4])
with col1:
    st.image("ISSJ image.png", width=200)
with col2:
    st.title("ISSJ HRM Services")

# ---- ナビゲーションメニュー ----
tabs = st.tabs(["🏠 ホーム", "📄 経歴書分析", "📊 データ管理", "⚙️ 設定"])

# ---- メインコンテンツ ----
with tabs[0]:  # ホーム
    # 機能紹介
    st.markdown("""
    ### 人材管理を効率化するAI支援ツール
    
    当サービスは、経歴書の自動分析と人材データの効率的な管理を実現します。
    AIを活用した高度な分析機能で、採用プロセスを最適化しましょう。
    """)

    # 機能紹介
    st.markdown("---")
    st.subheader("✨ 主な機能")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        ### 📄 経歴書分析
        - PDF/DOCXファイルの自動解析
        - スキル・経験の自動抽出
        - データのCSVエクスポート
        """)
    
    with col2:
        st.markdown("""
        ### 📊 データ管理
        - 候補者データの一元管理
        - 検索・フィルタリング機能
        - データの可視化
        """)
    
    with col3:
        st.markdown("""
        ### 🤖 AI支援
        - スキルマッチング
        - 適性分析
        - レポート生成
        """)

    # クイックスタート
    st.markdown("---")
    st.subheader("🚀 クイックスタート")
    
    with st.expander("経歴書を分析する", expanded=True):
        uploaded_file = st.file_uploader(
            "経歴書をアップロードしてください",
            type=["pdf", "docx"],
            help="PDFまたはWordファイルをドラッグ＆ドロップしてください"
        )
        
        if uploaded_file is not None:
            st.success("✅ ファイルを受け取りました！")
            st.info("📝 ファイルを分析中です...")

with tabs[1]:  # 経歴書分析
    st.header("📄 経歴書分析")
    st.info("このページは現在開発中です。")

with tabs[2]:  # データ管理
    st.header("📊 データ管理")
    st.info("このページは現在開発中です。")

with tabs[3]:  # 設定
    st.header("⚙️ 設定")
    st.info("このページは現在開発中です。")

# ---- フッター ----
st.markdown("---")
st.markdown("""
<div style='text-align: center'>
    <p>ISSJ HRM Services © 2025 | <a href='#'>プライバシーポリシー</a> | <a href='#'>利用規約</a></p>
</div>
""", unsafe_allow_html=True)
