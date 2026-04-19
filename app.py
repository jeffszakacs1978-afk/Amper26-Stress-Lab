import streamlit as st
import unicodedata
import time
import math
from collections import deque
import re

# ------------------------------------------------------------------------------
# IES Stage 1: Canonicalization
# ------------------------------------------------------------------------------
def ies_canonicalize(text: str) -> str:
    """Normalize Unicode, strip non-A-Z, uppercase."""
    text = unicodedata.normalize('NFKC', text)
    text = text.upper()
    return ''.join(c for c in text if 'A' <= c <= 'Z')

# ------------------------------------------------------------------------------
# Bijective Base-26 Processor
# ------------------------------------------------------------------------------
def bijective_encode(s: str) -> int:
    """Convert string of A-Z to bijective base-26 integer."""
    val = 0
    for ch in s:
        digit = ord(ch) - ord('A') + 1
        val = val * 26 + digit
    return val

# ------------------------------------------------------------------------------
# Intent Gate (Simplified Structural Signals)
# ------------------------------------------------------------------------------
def intent_check(text: str, original_text: str) -> tuple:
    """Return (action, reason) based on deterministic rules."""
    # Pronoun shift: "You are now..."
    if re.search(r'\bYOU\s+ARE\s+NOW\b', text):
        return "BLOCK", "Pronoun shift detected: 'You are now...'"
    # Delimiter breakout attempt (if original had <| or </)
    if '<|' in original_text or '</' in original_text or '"""' in original_text:
        return "BLOCK", "Delimiter breakout attempt"
    # Imperative density (crude: count imperative verbs)
    imperatives = ['DELETE', 'DROP', 'EXECUTE', 'RUN', 'IGNORE', 'FORGET', 'OVERRIDE']
    words = text.split()
    imp_count = sum(1 for w in words if w in imperatives)
    if len(words) > 0 and imp_count / len(words) > 0.3:
        return "BLOCK", f"High imperative density ({imp_count}/{len(words)})"
    return "PASS", ""

# ------------------------------------------------------------------------------
# Streamlit App
# ------------------------------------------------------------------------------
st.set_page_config(page_title="Amper-26 Live Demo", layout="wide")
st.title("🔷 Amper-26 Unified Architecture — Live Demo")
st.markdown("""
**Input Envelope Sentinel (IES) + Bijective Base-26 + Flux Estimator + Hysteresis**  
*Type or paste text below. The system analyzes it in real time using deterministic rules and control theory.*
""")

# Sidebar: Configuration & Thresholds
with st.sidebar:
    st.header("⚙️ Hysteresis & Flux Tuning")
    trigger = st.slider("Trigger Unsafe (s threshold)", 1000, 1000000, 50000, step=1000,
                        help="State integer value that triggers unsafe condition.")
    reset = st.slider("Reset Safe (s threshold)", 1000, 1000000, 48000, step=1000,
                      help="State must drop below this to return to safe.")
    window_ms = st.slider("Flux Window (ms)", 50, 1000, 200, step=50,
                          help="Time window for computing rate of change (ds/dt).")
    st.markdown("---")
    st.header("📊 Current State")
    state_placeholder = st.empty()
    flux_placeholder = st.empty()
    hysteresis_placeholder = st.empty()
    verdict_placeholder = st.empty()

# Main input area
user_input = st.text_area("📝 Input Text", value="Hello world", height=100)

# Process input
if user_input:
    # 1. Canonicalize
    clean = ies_canonicalize(user_input)
    st.write(f"**Canonicalized (IES Stage 1):** `{clean}`")

    # 2. Bijective encoding
    s = bijective_encode(clean)
    st.write(f"**Bijective State (s):** `{s:,}`")

    # 3. Intent Gate (IES Stage 3)
    intent_action, intent_reason = intent_check(clean, user_input)
    if intent_action == "BLOCK":
        st.error(f"🚫 Intent Gate BLOCK: {intent_reason}")
    else:
        st.success("✅ Intent Gate PASS")

    # 4. Flux estimation with sliding window
    # We'll use session state to store history
    import streamlit as st
import unicodedata
import time
import math
from collections import deque
import re

# ------------------------------------------------------------------------------
# IES Stage 1: Canonicalization
# ------------------------------------------------------------------------------
def ies_canonicalize(text: str) -> str:
    """Normalize Unicode, strip non-A-Z, uppercase."""
    text = unicodedata.normalize('NFKC', text)
    text = text.upper()
    return ''.join(c for c in text if 'A' <= c <= 'Z')

# ------------------------------------------------------------------------------
# Bijective Base-26 Processor
# ------------------------------------------------------------------------------
def bijective_encode(s: str) -> int:
    """Convert string of A-Z to bijective base-26 integer."""
    val = 0
    for ch in s:
        digit = ord(ch) - ord('A') + 1
        val = val * 26 + digit
    return val

# ------------------------------------------------------------------------------
# Intent Gate (Simplified Structural Signals)
# ------------------------------------------------------------------------------
def intent_check(text: str, original_text: str) -> tuple:
    """Return (action, reason) based on deterministic rules."""
    # Pronoun shift: "You are now..."
    if re.search(r'\bYOU\s+ARE\s+NOW\b', text):
        return "BLOCK", "Pronoun shift detected: 'You are now...'"
    # Delimiter breakout attempt (if original had <| or </)
    if '<|' in original_text or '</' in original_text or '"""' in original_text:
        return "BLOCK", "Delimiter breakout attempt"
    # Imperative density (crude: count imperative verbs)
    imperatives = ['DELETE', 'DROP', 'EXECUTE', 'RUN', 'IGNORE', 'FORGET', 'OVERRIDE']
    words = text.split()
    imp_count = sum(1 for w in words if w in imperatives)
    if len(words) > 0 and imp_count / len(words) > 0.3:
        return "BLOCK", f"High imperative density ({imp_count}/{len(words)})"
    return "PASS", ""

# ------------------------------------------------------------------------------
# Streamlit App
# ------------------------------------------------------------------------------
st.set_page_config(page_title="Amper-26 Live Demo", layout="wide")
st.title("🔷 Amper-26 Unified Architecture — Live Demo")
st.markdown("""
**Input Envelope Sentinel (IES) + Bijective Base-26 + Flux Estimator + Hysteresis**  
*Type or paste text below. The system analyzes it in real time using deterministic rules and control theory.*
""")

# Sidebar: Configuration & Thresholds
with st.sidebar:
    st.header("⚙️ Hysteresis & Flux Tuning")
    trigger = st.slider("Trigger Unsafe (s threshold)", 1000, 1000000, 50000, step=1000,
                        help="State integer value that triggers unsafe condition.")
    reset = st.slider("Reset Safe (s threshold)", 1000, 1000000, 48000, step=1000,
                      help="State must drop below this to return to safe.")
    window_ms = st.slider("Flux Window (ms)", 50, 1000, 200, step=50,
                          help="Time window for computing rate of change (ds/dt).")
    st.markdown("---")
    st.header("📊 Current State")
    state_placeholder = st.empty()
    flux_placeholder = st.empty()
    hysteresis_placeholder = st.empty()
    verdict_placeholder = st.empty()

# Main input area
user_input = st.text_area("📝 Input Text", value="Hello world", height=100)

# Process input
if user_input:
    # 1. Canonicalize
    clean = ies_canonicalize(user_input)
    st.write(f"**Canonicalized (IES Stage 1):** `{clean}`")

    # 2. Bijective encoding
    s = bijective_encode(clean)
    st.write(f"**Bijective State (s):** `{s:,}`")

    # 3. Intent Gate (IES Stage 3)
    intent_action, intent_reason = intent_check(clean, user_input)
    if intent_action == "BLOCK":
        st.error(f"🚫 Intent Gate BLOCK: {intent_reason}")
    else:
        st.success("✅ Intent Gate PASS")

    # 4. Flux estimation with sliding window
    # We'll use session state to store history
    if 'history' not in st.session_state:
        st.session_state.history = deque(maxlen=100)  # (timestamp, s)

    now = time.time()
    st.session_state.history.append((now, s))

    # Compute ds/dt over window
    if len(st.session_state.history) >= 2:
        # Filter points within window
        window_start = now - (window_ms / 1000.0)
        recent = [(t, val) for t, val in st.session_state.history if t >= window_start]
        if len(recent) >= 2:
            t_first, s_first = recent[0]
            t_last, s_last = recent[-1]
            dt = t_last - t_first
            ds = s_last - s_first
            flux = ds / dt if dt > 0 else 0.0
        else:
            flux = 0.0
    else:
        flux = 0.0

    st.write(f"**Flux (ds/dt):** `{flux:,.0f} chars/sec` (window {window_ms}ms)")

    # 5. Hysteresis logic
    if 'unsafe' not in st.session_state:
        st.session_state.unsafe = False

    prev_unsafe = st.session_state.unsafe
    if not st.session_state.unsafe and s > trigger:
        st.session_state.unsafe = True
    elif st.session_state.unsafe and s < reset:
        st.session_state.unsafe = False

    hysteresis_state = "🔴 UNSAFE" if st.session_state.unsafe else "🟢 SAFE"
    st.write(f"**Hysteresis State:** {hysteresis_state} (trigger={trigger:,}, reset={reset:,})")

    # 6. Overall Verdict
    if intent_action == "BLOCK" or st.session_state.unsafe:
        verdict = "BLOCK"
        reason = intent_reason if intent_action == "BLOCK" else "State integer exceeds safe envelope (or flux anomaly)"
        st.error(f"🛑 **Final Verdict: {verdict}** — {reason}")
    else:
        st.success("✅ **Final Verdict: ALLOW** — Input within safety envelope and passes intent gate.")

    # Update sidebar metrics
    state_placeholder.metric("State Integer (s)", f"{s:,}")
    flux_placeholder.metric("Flux (ds/dt)", f"{flux:,.0f} /s")
    hysteresis_placeholder.metric("Hysteresis", hysteresis_state)
    verdict_placeholder.metric("Verdict", verdict if 'verdict' in locals() else "ALLOW")

    # Optional: Show state graph
    if st.checkbox("Show state history"):
        import pandas as pd
        df = pd.DataFrame(st.session_state.history, columns=['timestamp', 's'])
        df['elapsed'] = df['timestamp'] - df['timestamp'].iloc[0]
        st.line_chart(df.set_index('elapsed')['s'])
else:
    st.info("Enter some text to begin analysis.")

    # Compute ds/dt over window
    if len(st.session_state.history) >= 2:
        # Filter points within window
        window_start = now - (window_ms / 1000.0)
        recent = [(t, val) for t, val in st.session_state.history if t >= window_start]
        if len(recent) >= 2:
            t_first, s_first = recent[0]
            t_last, s_last = recent[-1]
            dt = t_last - t_first
            ds = s_last - s_first
            flux = ds / dt if dt > 0 else 0.0
        else:
            flux = 0.0
    else:
        flux = 0.0

    st.write(f"**Flux (ds/dt):** `{flux:,.0f} chars/sec` (window {window_ms}ms)")

    # 5. Hysteresis logic
    if 'unsafe' not in st.session_state:
        st.session_state.unsafe = False

    prev_unsafe = st.session_state.unsafe
    if not st.session_state.unsafe and s > trigger:
        st.session_state.unsafe = True
    elif st.session_state.unsafe and s < reset:
        st.session_state.unsafe = False

    hysteresis_state = "🔴 UNSAFE" if st.session_state.unsafe else "🟢 SAFE"
    st.write(f"**Hysteresis State:** {hysteresis_state} (trigger={trigger:,}, reset={reset:,})")

    # 6. Overall Verdict
    if intent_action == "BLOCK" or st.session_state.unsafe:
        verdict = "BLOCK"
        reason = intent_reason if intent_action == "BLOCK" else "State integer exceeds safe envelope (or flux anomaly)"
        st.error(f"🛑 **Final Verdict: {verdict}** — {reason}")
    else:
        st.success("✅ **Final Verdict: ALLOW** — Input within safety envelope and passes intent gate.")

    # Update sidebar metrics
    state_placeholder.metric("State Integer (s)", f"{s:,}")
    flux_placeholder.metric("Flux (ds/dt)", f"{flux:,.0f} /s")
    hysteresis_placeholder.metric("Hysteresis", hysteresis_state)
    verdict_placeholder.metric("Verdict", verdict if 'verdict' in locals() else "ALLOW")

    # Optional: Show state graph
    if st.checkbox("Show state history"):
        import pandas as pd
        df = pd.DataFrame(st.session_state.history, columns=['timestamp', 's'])
        df['elapsed'] = df['timestamp'] - df['timestamp'].iloc[0]
        st.line_chart(df.set_index('elapsed')['s'])

   # Optional: Show state history
    if st.checkbox("Show state history"):
        import pandas as pd
        if len(st.session_state.history) > 1:
            df = pd.DataFrame(list(st.session_state.history), columns=['timestamp', 's'])
            df['elapsed'] = df['timestamp'] - df['timestamp'].iloc[0]
            st.line_chart(df.set_index('elapsed')['s'])
        else:
            st.info("Gathering data points...")
else:
    st.info("Enter some text to begin analysis.")")   st.info("Enter some text to begin analysis.")
