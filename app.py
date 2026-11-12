import streamlit as st
import yt_dlp

# 웹페이지 제목과 설명
st.set_page_config(page_title="초간단 영상 다운로더", page_icon="🎬")
st.title("🎬 초간단 영상 다운로더")
st.write("인스타그램이나 유튜브 주소를 넣으면 다운로드 링크를 찾아드려요!")

# 입력창 만들기
url = st.text_input("영상 주소(URL)를 입력하세요", placeholder="https://www.instagram.com/reels/...")

if st.button("링크 추출하기"):
    if url:
        with st.spinner('분석 중입니다... 잠시만 기다려주세요!'):
            try:
                # yt-dlp 설정
                ydl_opts = {'format': 'best', 'quiet': True}
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    info = ydl.extract_info(url, download=False)
                    video_url = info.get('url')
                
                # 결과 화면에 표시
                st.success("🎉 링크를 찾았습니다!")
                st.markdown(f"[📥 여기를 클릭해서 영상 다운로드]({video_url})")
                st.balloons() 

            except Exception as e:
                st.error(f"❌ 에러가 발생했습니다: {e}")
    else:
        st.warning("주소를 입력해 주세요!")
