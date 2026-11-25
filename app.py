import streamlit as st

data = {
    "어깨": [
        {"운동명": "야구", "위험도": "상"},
        {"운동명": "테니스", "위험도": "상"},
        {"운동명": "벤치프레스", "위험도": "상"},
        {"운동명": "배드민턴", "위험도": "중"},
        {"운동명": "수영", "위험도": "중"}
    ],
    "발목": [
        {"운동명": "축구", "위험도": "상"},
        {"운동명": "농구", "위험도": "상"},
        {"운동명": "줄넘기", "위험도": "상"},
        {"운동명": "달리기", "위험도": "중"},
        {"운동명": "등산", "위험도": "중"}
    ],
    "허리": [
        {"운동명": "데드리프트", "위험도": "상"},
        {"운동명": "스쿼트", "위험도": "상"},
        {"운동명": "골프", "위험도": "상"},
        {"운동명": "윗몸일으키기", "위험도": "중"},
        {"운동명": "볼링", "위험도": "중"}
    ],
    "무릎": [
        {"운동명": "스쿼트", "위험도": "상"},
        {"운동명": "축구", "위험도": "상"},
        {"운동명": "줄넘기", "위험도": "상"},
        {"운동명": "계단오르기", "위험도": "중"},
        {"운동명": "달리기", "위험도": "중"}
    ],
    "손목": [
        {"운동명": "팔굽혀펴기", "위험도": "상"},
        {"운동명": "테니스", "위험도": "상"},
        {"운동명": "철봉", "위험도": "중"},
        {"운동명": "탁구", "위험도": "중"},
        {"운동명": "볼링", "위험도": "중"}
    ]
}

def check_injury(part, level, done):
    if level >= 20:
        days = 30
    elif level >= 15:
        days = 15
    else:
        days = 7

    items = data[part]
    extra = 0
    user_ex = done.strip()

    for x in items:
        if user_ex == x["운동명"]:
            if x["위험도"] == "상":
                extra = 14
            elif x["위험도"] == "중":
                extra = 7
            break

    total = days + extra
    ex_list = [x["운동명"] for x in items[:3]]
    msg = part + " 부상 시 " + ", ".join(ex_list) + " 등은 삼가야 합니다."

    table = []
    for x in items:
        table.append({
            "운동명": x["운동명"],
            "위험도": x["위험도"]
        })

    return msg, table, total, extra

st.title("다친 부위별 금기 운동 안내")
st.write("부위와 정도를 입력하면 피해야 할 운동과 기간을 알려줍니다.")

part = st.selectbox("1) 다친 부위", list(data.keys()))
level = st.slider("2) 다친 정도", 1, 25, 10)
done = st.text_input("3) 부상 후 한 운동 (없으면 빈칸)", "")

if st.button("분석하기"):
    msg, table, total, extra = check_injury(part, level, done)
    st.warning(msg)
    st.write("피해야 할 운동 목록")
    st.table(table)
    st.write("다친 정도:", level)
    if extra > 0:
        st.write("권장 휴식 기간:", total, "일 (금기 운동 추가로 +", extra, "일)")
    else:
        st.write("권장 휴식 기간:", total, "일")
