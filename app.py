import streamlit as st
import numpy as np
import pandas as pd

# --- CORE AMPER 26 LOGIC ---
def get_signal_energy(text):
    values = [(ord(c.upper()) - 64) for c in text if c.isalpha()]
    return values if values else [0]

def lyapunov_check(signal, decay=1.0):
    threshold = 30.0
    energy_path = []
    current_energy = 0
    neutralized = False
    for s in signal:
        current_energy += abs(s)
        if current_energy > threshold:
            neutralized = True
            current_energy = 0 
        current_energy *= np.exp(-decay * 1.0)
        energy_path.append(current_energy)
    return energy_path, neutralized

# --- UI ---
st.title("🛡️ Amper 26: Boundary Integrity Lab")
user_input = st.text_area("Attack Vector Input:", placeholder="Try to crash the state space...")

if st.button("Execute Stress Test") and user_input:
    signal = get_signal_energy(user_input)
    energy_path, was_neutralized = lyapunov_check(signal)
    if was_neutralized:
        st.error("🚨 SIGNAL NEUTRALIZED: Boundary Violation")
    else:
        st.success("✅ SIGNAL ADMITTED: Stable State")
    st.line_chart(pd.DataFrame(energy_path, columns=["System Energy (V)"]))
