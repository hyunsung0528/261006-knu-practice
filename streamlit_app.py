import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Streamlit 요소 체험하기",
    page_icon="🧪",
    layout="wide",
)

st.title("🧪 Streamlit 요소 체험하기")
st.write("화면의 위젯을 직접 바꿔 보며 Streamlit 앱의 기본 구성 요소를 익혀 보세요.")
st.caption("위젯을 조작하면 앱이 다시 실행되어 변경된 값이 화면에 반영됩니다.")

st.header("1. 텍스트와 알림")
st.markdown("`st.title`, `st.header`, `st.write`는 제목과 설명을 표시합니다.")
st.info("안내 메시지: 중요한 정보를 파란색 상자로 보여줍니다.")
st.success("성공 메시지: 작업이 잘 끝났을 때 사용합니다.")
st.warning("주의 메시지: 확인이 필요한 내용을 알립니다.")
st.code('st.write("안녕하세요, Streamlit!")', language="python")

st.header("2. 버튼과 입력 위젯")
left, right = st.columns(2)

with left:
    st.subheader("문장 만들기")
    user_name = st.text_input("이름을 입력하세요", placeholder="예: 민지")
    user_message = st.text_area("하고 싶은 말을 적어 보세요", "Streamlit을 배우는 중입니다!")
    if st.button("인사 문장 만들기", type="primary"):
        name = user_name.strip() or "방문자"
        st.success(f"{name}님, {user_message}")

with right:
    st.subheader("선택 및 숫자 입력")
    favorite_color = st.selectbox("좋아하는 색을 선택하세요", ["파랑", "초록", "주황", "분홍"])
    learning_level = st.radio("학습 단계", ["처음이에요", "조금 써 봤어요", "익숙해요"], horizontal=True)
    item_count = st.number_input("항목 수", min_value=1, max_value=20, value=5)
    st.write(f"선택 결과: **{favorite_color}**, **{learning_level}**, 항목 **{item_count}개**")

st.header("3. 슬라이더와 체크박스")
st.write("슬라이더와 체크박스를 바꾸면 아래 결과가 바로 업데이트됩니다.")
score = st.slider("오늘의 기분 점수", min_value=0, max_value=100, value=65, step=5)
show_detail = st.checkbox("상세 설명 보기", value=True)
if show_detail:
    st.progress(score / 100, text=f"기분 점수: {score}점")
    st.write("슬라이더의 현재 값을 `st.progress`에 연결한 예시입니다.")
else:
    st.write(f"현재 점수는 **{score}점**입니다.")

topics = st.multiselect(
    "더 알아보고 싶은 요소를 선택하세요",
    ["레이아웃", "차트", "데이터 표", "파일 업로드"],
    default=["차트", "데이터 표"],
)
st.write("선택한 주제:", ", ".join(topics) if topics else "아직 없어요")

st.header("4. 탭과 접기 영역")
overview_tab, tips_tab = st.tabs(["탭 예시", "사용 팁"])
with overview_tab:
    st.write("탭을 사용하면 관련 내용을 한 화면 안에서 나누어 보여줄 수 있습니다.")
with tips_tab:
    with st.expander("코드에서 어떻게 쓰나요?", expanded=False):
        st.code('with st.expander("자세히 보기"):\n    st.write("숨겨진 내용")', language="python")

st.header("5. 데이터 표와 차트")
st.write("아래 데이터는 이 앱 안에서 만든 예제입니다. 행 수를 바꾸어 표와 차트의 변화를 확인해 보세요.")
row_count = st.slider("표와 차트에 표시할 데이터 개수", min_value=3, max_value=12, value=7)
sample_df = pd.DataFrame(
    {
        "일자": pd.date_range("2026-01-01", periods=row_count, freq="D"),
        "방문자 수": [12 + (index * 7) % 19 for index in range(row_count)],
        "만족도": [3.2 + (index * 3 % 8) / 10 for index in range(row_count)],
    }
)

table_col, chart_col = st.columns([1, 1])
with table_col:
    st.subheader("데이터 표")
    st.dataframe(sample_df, width="stretch", hide_index=True)
with chart_col:
    st.subheader("선형 차트")
    st.line_chart(sample_df, x="일자", y=["방문자 수", "만족도"])

st.subheader("요약 지표와 막대 차트")
metric_col, bar_col = st.columns([1, 2])
with metric_col:
    st.metric("평균 방문자", f"{sample_df['방문자 수'].mean():.1f}명", delta="예제 데이터")
with bar_col:
    st.bar_chart(sample_df, x="일자", y="방문자 수")

st.header("6. 폼으로 한 번에 제출하기")
st.write("폼 안의 값은 제출 버튼을 누를 때 한 번에 전달됩니다.")
with st.form("feedback_form"):
    feedback = st.text_input("이 페이지에서 가장 유용한 요소는 무엇인가요?")
    rating = st.select_slider("이해하기 쉬웠나요?", options=["어려워요", "보통이에요", "쉬워요"])
    submitted = st.form_submit_button("의견 제출")
if submitted:
    st.toast("의견이 제출되었습니다.")
    st.write(f"의견: {feedback or '(작성한 의견 없음)'} / 난이도: {rating}")

st.divider()
st.caption("여기까지가 기본 체험입니다. 각 요소는 `st.`로 시작하는 Streamlit 명령으로 화면에 표시할 수 있습니다.")
