import streamlit as st
import yt_dlp
import requests
from io import BytesIO

# 웹페이지 제목 및 설정
st.set_page_config(page_title="진짜 저장 다운로더", page_icon="🎬")
st.title("🎬 진짜 저장 다운로더")
st.write("이제는 링크가 아니라 '진짜 파일'을 보내드립니다!")

url = st.text_input("영상 주소(URL)를 입력하세요", placeholder="https://www.instagram.com/reels/...")

if st.button("영상 다운로드 시작"):
    if url:
        with st.spinner('서버가 영상을 가져오는 중입니다... 잠시만 기다려주세요!'):
            try:
                # 1. 영상 주소 추출
                ydl_opts = {
                    'format': 'best', 
                    'quiet': True,
                    'cookiefile': 'cookies.txt', 
                }
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    info = ydl.extract_info(url, download=False)
                    video_url = info.get('url')

                # 2. [핵심] 서버가 직접 영상 데이터를 다운로드함
                response = requests.get(video_url)
                video_data = response.content # 영상의 실제 바이트 데이터

                # 3. 스트림릿의 download_button 기능을 사용하여 파일로 전송
                st.success("🎉 영상 준비 완료! 아래 버튼을 누르면 즉시 저장됩니다.")
                st.download_button(
                    label="📥 내 기기에 즉시 저장하기",
                    data=video_data, 
                    file_name="instagram_video.mp4", 
                    mime="video/mp4"
                )
                st.balloons()

            except Exception as e:
                st.error(f"❌ 에러 발생: {e}")
    else:
        st.warning("주소를 입력해 주세요!")
