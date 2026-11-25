import streamlit as st

# 1. 데이터 구조: 다친 부위별 금기 운동 및 위험도 정의
forbidden_exercises = {
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

# 2. 함수: 부위, 다친 정도, 부상 후 한 운동 분석
def analyze_injury(part, level, done_exercise):
    # 기본 회복 기간 계산 (if-elif-else)
    if level >= 20:
        days = 30
    elif level >= 15:
        days = 15
    else:
        days = 7

    exercises = forbidden_exercises[part]
    extra_days = 0
    clean_input = done_exercise.strip()

    # 부상 후 한 운동이 금기 운동인지 확인 (for + if)
    for item in exercises:
        name = item["운동명"]
        risk = item["위험도"]
        if clean_input == name:
            if risk == "상":
                extra_days = 14
            elif risk == "중":
                extra_days = 7
            break

    total_days = days + extra_days

    # 경고 안내문 생성
    names = [item["운동명"] for item in exercises[:3]]
    joined_names = ", ".join(names)
    warning_msg = f"{part} 부상 시 {joined_names} 등의 운동은 삼가해야 합니다."

    # 테이블 출력용 데이터 변환 (for)
    table_data = []
    for item in exercises:
        table_data.append({
            "운동명": item["운동명"],
            "위험도": item["위험도"]
        })

    return warning_msg, table_data, total_days, extra_days


# 3. 화면 구성 (UI)
st.title("🏥 다친 부위에 따른 금기 사항 및 기간")
st.write("부상 부
