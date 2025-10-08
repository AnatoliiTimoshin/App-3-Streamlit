import streamlit as st

st.title("🎉 Вітаємо у твоєму першому Streamlit-додатку!")

# Ввід імені користувача
name = st.text_input("Введи своє ім’я:")
age = st.slider("Скільки тобі років?", 10, 80, 25)

# Кнопка
if st.button("Привітатись"):
    st.success(f"Привіт, {name}! Тобі {age} років.")
else:
    st.info("Введи дані і натисни кнопку.")
