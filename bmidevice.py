def advice (user_weight,user_height):
    user_bmi = round(user_weight / (user_height ** 2),1)
    user_bmi_data = {
        (0,18.4): "您的身体疑似营养不良 请咨询医生",
        (18.5,24.9): "您的身体很健康",
        (25.0,29.9): "您的身体太胖了 建议减肥",
        (30.0, float('inf')): "您的身体很不健康 建议减肥并咨询医生"
    }
    for (low,up),(advice) in user_bmi_data.items():
        if low <= user_bmi <= up:
            print(f"您的bmi值为{user_bmi}")
            print(advice)
            return advice