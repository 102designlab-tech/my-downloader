import streamlit as st
import yt_dlp

# 웹페이지 제목과 설명
st.set_page_config(page_title="초강력 영상 다운로더", page_icon="🎬")
st.title("🎬 초강력 영상 다운로더")
st.write("인스타그램이나 유튜브 주소를 넣으면 가장 빠르게 저장해 드려요!")

# 입력창 만들기
url = st.text_input("영상 주소(URL)를 입력하세요", placeholder="https://www.instagram.com/reels/...")

if st.button("링크 추출하기"):
    if url:
        with st.spinner('분석 중입니다... 잠시만 기다려주세요!'):
            try:
                ydl_opts = {
                    'format': 'best', 
                    'quiet': True,
                    'cookiefile': 'cookies.txt', 
                }
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    info = ydl.extract_info(url, download=False)
                    video_url = info.get('url')
                
                st.success("🎉 준비 완료!")
                
                # [핵심 수정] 단순 링크가 아니라, 다운로드를 유도하는 버튼 형태로 표시
                # 실제 구현 시 브라우저 설정에 따라 다운로드 폴더로 바로 들어갑니다.
                st.markdown(f"""
                    <a href="{video_url}" download="video.mp4" style="
                        background-color: #4CAF50; 
                        color: white; 
                        padding: 10px 20px; 
                        text-decoration: none; 
                        border-radius: 5px; 
                        font-weight: bold;
                        display: inline-block;
                    ">📥 지금 바로 내 기기에 저장하기</a>
                """, unsafe_allow_html=True)
                st.balloons() 

            except Exception as e:
                st.error(f"❌ 에러가 발생했습니다: {e}")
    else:
        st.warning("주소를 입력해 주세요!")
