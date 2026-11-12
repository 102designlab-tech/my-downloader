import streamlit as st
import yt_dlp
import os

# 웹페이지 제목과 설명
st.set_page_config(page_title="초강력 영상 다운로더", page_icon="🎬")
st.title("🎬 초강력 영상 다운로더")
st.write("쿠키 정보를 이용해 더 강력하게 영상을 찾아냅니다!")

# 입력창 만들기
url = st.text_input("영상 주소(URL)를 입력하세요", placeholder="https://www.instagram.com/reels/...")

if st.button("링크 추출하기"):
    if url:
        with st.spinner('쿠키를 사용하여 분석 중입니다... 잠시만 기다려주세요!'):
            try:
                # [핵심 수정] cookies.txt 파일을 사용하여 인증 정보 제공
                ydl_opts = {
                    'format': 'best', 
                    'quiet': True,
                    'cookiefile': 'cookies.txt', # 업로드한 쿠키 파일 경로 지정
                }
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    info = ydl.extract_info(url, download=False)
                    video_url = info.get('url')
                
                st.success("🎉 성공! 링크를 찾았습니다!")
                st.markdown(f"[📥 여기를 클릭해서 영상 다운로드]({video_url})")
                st.balloons() 

            except Exception as e:
                st.error(f"❌ 에러가 발생했습니다: {e}")
    else:
        st.warning("주소를 입력해 주세요!")
