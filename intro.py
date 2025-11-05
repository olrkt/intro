# app.py
import streamlit as st

# 1. 페이지 설정: 제목과 레이아웃을 설정합니다.
st.set_page_config(
    page_title="개인 웹사이트 소개 및 포트폴리오",
    layout="wide", # 넓은 레이아웃 사용
    initial_sidebar_state="collapsed" # 사이드바는 접은 상태로 시작
)

# --- 2. 연락처 정보 섹션 ---
# 마크다운을 사용하여 연락처 정보를 제목보다 위에 배치하고 시각적으로 구분합니다.
st.markdown("### Contact")
st.markdown("ig: **olrkt**")
st.markdown("e-mail: **gyusunleekr@gmail.com**")
st.markdown("---")

# --- 3. Works (프로젝트) 섹션 ---
st.header("🛠️ Works")
# 오류가 있던 'st.' 부분을 수정하여 섹션 소개 문구를 추가했습니다.
st.markdown("---")

# 3-1. mappinz 프로젝트
st.subheader("🎵 mappinz")
st.markdown("music on the map")
# mappinz 링크를 수정했습니다.
st.markdown("🔗 [**mappinz 사이트 바로가기**](https://mappinz.web.app)")

st.markdown("---") # 프로젝트 간 구분선

# 3-2. US Stock Manager 프로젝트
st.subheader("yfinance data downloader")
st.markdown("**yfinance statistics, annual/quarterly financials항목 추출, 엑셀다운**")
# US Stock Manager 링크를 유지합니다.
st.markdown("🔗 [**web 바로가기**](https://yfinancedatadownloader.streamlit.app/)")
st.markdown("---") # 프로젝트 간 구분선



# --- 4. 마무리 문구 ---
st.caption("MIT License Copyright (c) 2025 olrkt")
