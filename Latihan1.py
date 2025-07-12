import streamlit as st

# Simple School Shuttle Schedule Chatbot
# Chatbot Jadwal Mobil Antar Jemput Sekolah

def get_schedule():
    # Contoh jadwal keberangkatan
    schedule = {
        "Senin": "07:00, 13:00",
        "Selasa": "07:00, 13:00",
        "Rabu": "07:00, 13:00",
        "Kamis": "07:00, 13:00",
        "Jumat": "07:00, 11:00",
        "Sabtu": "Libur",
        "Minggu": "Libur"
    }
    return schedule

def chatbot():
    print("Halo! Saya chatbot jadwal antar jemput sekolah.")
    print("Ketik nama hari untuk mengetahui jadwal keberangkatan (misal: Senin). Ketik 'keluar' untuk berhenti.")
    schedule = get_schedule()
    while True:
        user_input = input("Hari: ").capitalize()
        if user_input == "Keluar":
            print("Terima kasih! Sampai jumpa.")
            break
        elif user_input in schedule:
            print(f"Jadwal keberangkatan hari {user_input}: {schedule[user_input]}")
        else:
            print("Maaf, hari tidak dikenali. Silakan coba lagi.")

if __name__ == "__main__":
    chatbot()