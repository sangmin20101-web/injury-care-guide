import streamlit as st
import pandas as pd

st.set_page_config(page_title="다친 부위에 따른 주의 사항 및 기간", page_icon="🩹")
st.title("🩹 다친 부위에 따른 주의 사항 및 기간")
st.write("진료 및 간호학과 연계 프로젝트: 환자의 다친 부위와 정도를 체크하여 피해야 할 운동과 회복 기간을 안내합니다.")

st.divider()

avoid_exercises = {
    "어깨": [
        ["야구", "상"],
        ["배드민턴", "중"],
        ["수영(자유형/접영)", "상"],
        ["턱걸이", "상"]
    ],
    "발목": [
        ["축구", "상"],
        ["농구", "상"],
        ["줄넘기", "중"],
        ["등산", "중"]
    ],
    "허리": [
        ["골프", "상"],
        ["데드리프트(무거운 물건 들기)", "상"],
        ["윗몸일으키기", "중"],
        ["볼링", "중"]
    ]
}

st.subheader("📋 상태 입력")
body_part = st.selectbox("1) 다친 부위 선택", ["어깨", "발목", "허리"])
injury_level = st.slider("2) 다친 정도 (통증 및 손상 지수)", min_value=1, max_value=25, value=10)

def analyze_injury(part, level):
    period = 0
    if level >= 20:
        period += 30
    elif level >= 15:
        period += 15
    else:
        period += 7

    raw_list = avoid_exercises[part]
    table_data = []
    for item in raw_list:
        table_data.append({
            "운동명": item[0],
            "위험도": item[1]
        })

    return period, table_data

if st.button("분석하기", type="primary"):
    recovery_days, exercise_table = analyze_injury(body_part, injury_level)

    st.divider()
    st.subheader("📊 분석 결과")

    exercise_names = [row["운동명"] for row in exercise_table]
    st.warning(f"⚠️ **{body_part}** 부상 시 **{', '.join(exercise_names[:2])}** 등의 운동은 삼가해야 합니다.")

    st.write("**🚫 피해야 할 운동 목록**")
    df = pd.DataFrame(exercise_table)
    st.table(df)

    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="다친 정도", value=f"{injury_level} / 25")
    with col2:
        st.metric(label="권장 회복 기간", value=f"{recovery_days}일")
