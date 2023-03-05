import streamlit as st
import pickle

st.header('Проверь свое здоровье:')

def load():
    with open('./model.pcl', 'rb') as fid:
        return pickle.load(fid)

def add_bmi(height, weight):
    return (weight / (height/100) ** 2)

def add_gender(gen):
    if gen == "М":
        return 2
    return 1

age = st.slider('Укажите возраст, лет', 30, 100, key='age')
gen = st.radio('Выберите пол', ('М', 'Ж'), key='gen')
height = st.slider('Введите рост в сантиметрах', 90, 240, key='height')
weight = st.slider('Введите вес в килограммах', 40, 200, key='weight')
ap_hi = st.slider('Укажите верхнее давление (систолическоe)', 70, 280, None, 10,  key='ap_hi')
ap_lo = st.slider('Укажите нижнее давление (диастолическое)', 20, 200, None, 10, key='ap_lo')
cholesterol = st.radio('Выберите уровень холестерина', (1, 2, 3), key='cholesterol')
gluc = st.radio('Выберите уровень сахара', (1, 2, 3), key='gluc')
smoke = st.checkbox('Вы курите?', key='smoke')
alco = st.checkbox('Вы употребляете алкоголь?', key='alco')
active = st.checkbox('Вы занимаетесь спортом?', key='active')


bmi = add_bmi(height, weight)
sum_ap = ap_hi + ap_lo
gender = add_gender(gen)

model = load()
y_pr = model.predict_proba([[age, gender, height, weight, ap_hi, ap_lo, 
cholesterol, gluc, smoke, alco, active, sum_ap, bmi]])[:,1]
ur = (y_pr[0] * 100).round(2)
st.write('Риск сердечно-сосудистых заболеваний:', ur, '%')