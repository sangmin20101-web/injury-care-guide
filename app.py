import streamlit as st

# 1. 데이터 구조 (리스트 & 딕셔너리): 다친 부위별 금기 운동 및 위험도 정의
forbidden_exercises = {
    "어깨": [
        {"운동명": "야구", "위험도": "상"},
        {"운동명": "배드민턴", "위험도": "중"}
    ],
    "발목": [
        {"운동명": "축구", "위험도": "상"},
        {"운동명": "달리기", "위험도": "중"}
    ],
    "허리": [
        {"운동명": "데드리프트", "위험도": "상"},
        {"운동명": "골프", "위험도": "중"}
    ]
}

# 2. 함수 (def): 부위, 다친 정도, 부상 후 한 운동을 매개변수로 받아 분석하는 함수
def analyze_injury(part, level, done_exercise):
    # 기본 회복 기간 계산 (if-elif-else 조건문)
    if level >= 20:
        days = 30
    elif level >= 15:
        days = 15
    else:
        days = 7

    # 해당 부위의 피해야 할 운동 리스트 가져오기
    exercises = forbidden_exercises[part]
    
    # 부상 후 한 운동이 금기 운동에 포함되는지 확인 (for 반복문 + if 조건문)
    extra_days = 0
    matched_risk = None
    
    for item in exercises:
        # 입력한 운동이 금기 운동 목록에 있을 때만 위험도 확인 후 기간 추가
        if done_exercise.strip() == item["운동명"]:
            matched_risk = item["위험도"]
            if matched_risk == "상":
                extra_days = 14  # 위험도 '상'이면 14일 추가
            elif matched_risk == "중":
                extra_days = 7   # 위험도 '중'이면 7일 추가
            break  # 일치하는 운동을 찾았으므로 반복 종료
    # 피해야 할 운동이 아닌 다른 운동을 했거나 입력하지 않았으면 extra_days는 0 그대로 넘어감

    total_days = days + extra_days

    # 경고 안내문 생성
    exercise_names = [item["운동명"] for item in exercises]
    warning_msg = f"{part} 부상 시 {', '.join(exercise_names)} 등의 운동은 삼가해야 합니다."

    # 테이블(표) 출력을 위한 데이터 변환 (for 반복문 활용)
    table_data = []
    for item in exercises:
        table_data.append({
            "운동명": item["운동명"],
            "위험도": item["위험도"]
        })

    return warning_msg, table_data, total_days, extra_days, matched_risk


# --- 3. 화면 구성 (UI) ---
st.title("🏥 다친 부위에 따른 금기 사항 및 기간")
st.write("부상 부위와 정도를 체크하여 피해야 할 운동과 권장 회복 기간을 안내합니다.")

# 입력 UI
part = st.selectbox("1) 다친 부위 선택", ["어깨", "발목", "허리"])
level = st.slider("2) 다친 정도", min_value=1, max_value=25, value=10)
done_exercise = st
