import streamlit as st
from datetime import datetime

# Contoh data jadwal mobil antar jemput
jadwal = {
    "Senin": "07:00 - 15:00",
    "Selasa": "07:00 - 15:00",
    "Rabu": "07:00 - 15:00",
    "Kamis": "07:00 - 15:00",
    "Jumat": "07:00 - 12:00",
}

def chatbot_response(user_input):
    user_input = user_input.lower()
    hari_ini = datetime.now().strftime("%A")
    hari_indo = {
        "Monday": "Senin",
        "Tuesday": "Selasa",
        "Wednesday": "Rabu",
        "Thursday": "Kamis",
        "Friday": "Jumat",
        "Saturday": "Sabtu",
        "Sunday": "Minggu"
    }
    if "jadwal" in user_input or "jam" in user_input:
        for hari in jadwal:
            if hari.lower() in user_input:
                return f"Jadwal mobil antar jemput hari {hari}: {jadwal[hari]}"
        return "Jadwal mobil antar jemput:\n" + "\n".join([f"{h}: {j}" for h, j in jadwal.items()])
    elif "hari ini" in user_input:
        hari = hari_indo[hari_ini]
        if hari in jadwal:
            return f"Jadwal mobil antar jemput hari ini ({hari}): {jadwal[hari]}"
        else:
            return "Hari ini tidak ada jadwal mobil antar jemput."
    else:
        return "Maaf, saya hanya bisa membantu terkait jadwal mobil antar jemput siswa."

st.title("Chatbot Jadwal Mobil Antar Jemput Siswa")

if "history" not in st.session_state:
    st.session_state.history = []

user_input = st.text_input("Tulis pertanyaan Anda:")

if st.button("Kirim") and user_input:
    response = chatbot_response(user_input)
    st.session_state.history.append(("Anda", user_input))
    st.session_state.history.append(("Bot", response))

for sender, message in st.session_state.history:
    st.write(f"**{sender}:** {message}")