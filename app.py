import streamlit as st
import time

# ---------------------- Page Configuration ----------------------
st.set_page_config(page_title="NextGen Wireless Network Simulator", layout="centered")

st.title("📡 NextGen Wireless Network Simulator")
st.markdown("""
Welcome to the interactive simulator for understanding core mechanisms in Next Generation Wireless Networks (3GPP/3GPP2).  
Use the sidebar to explore different modules such as **PDP Context Activation**, **IMS Signaling**, **Mobility**, **Security**, and **QoS Mapping**.
""")

# ---------------------- Module 1: PDP Context Activation ----------------------
def pdp_context_simulation():
    st.subheader("📶 PDP Context Activation")
    steps = [
        "1. MS sends Attach Request to SGSN",
        "2. SGSN authenticates and sends Authentication Request",
        "3. MS responds with Authentication Response",
        "4. SGSN sends Update Location to HLR",
        "5. HLR acknowledges with Insert Subscriber Data",
        "6. MS sends Activate PDP Context Request",
        "7. SGSN forwards to GGSN",
        "8. GGSN creates PDP context and returns PDP address",
        "9. SGSN confirms PDP context to MS",
        "10. Radio Bearer is assigned",
        "11. Mobile now has IP connectivity"
    ]
    if st.button("▶ Start PDP Context Simulation"):
        for step in steps:
            st.success(step)
            time.sleep(1.2)

# ---------------------- Module 2: IMS Signaling ----------------------
def ims_signaling_simulation():
    st.subheader("📲 IMS Signaling Flow (SIP-based)")

    signaling_steps = [
        "1. MS sends REGISTER request to P-CSCF",
        "2. P-CSCF forwards to I-CSCF → S-CSCF",
        "3. S-CSCF contacts HSS for user profile",
        "4. S-CSCF responds with 200 OK to REGISTER",
        "5. MS sends SIP INVITE to initiate session",
        "6. P-CSCF routes to remote UE via S-CSCF",
        "7. Remote UE sends 180 Ringing → 200 OK",
        "8. MS sends ACK, session established",
        "9. Media flows directly between UEs (RTP)",
        "10. Session can be modified or terminated by BYE"
    ]
    if st.button("▶ Start IMS Signaling Simulation"):
        for step in signaling_steps:
            st.info(step)
            time.sleep(1.2)

# ---------------------- Module 3: Mobility Management ----------------------
def mobility_management_simulation():
    st.subheader("🚗 Mobile IPv6 Handoff Simulation")

    mobility_steps = [
        "1. Mobile Node (MN) detects movement to new subnet",
        "2. MN configures new Care-of Address (CoA)",
        "3. MN sends Binding Update to Home Agent (HA)",
        "4. HA updates Binding Cache",
        "5. Packets now tunneled from HA to new CoA",
        "6. MN optionally updates Correspondent Node (CN)",
        "7. CN can now send packets directly to MN"
    ]
    if st.button("▶ Start Mobile IPv6 Handoff Simulation"):
        for step in mobility_steps:
            st.warning(step)
            time.sleep(1.2)

# ---------------------- Module 4: Security Flow ----------------------
def security_simulation():
    st.subheader("🔐 GSM/GPRS/3GPP Security Authentication")

    security_steps = [
        "1. MS sends Authentication Request to Network",
        "2. Network generates RAND and sends to MS",
        "3. MS computes SRES using A3 algorithm",
        "4. MS sends SRES to Network",
        "5. Network compares SRES with expected response",
        "6. If match, session proceeds",
        "7. Kc (ciphering key) derived using A8 algorithm",
        "8. Traffic encrypted using Kc",
        "9. IPsec tunnel established (for 3G/4G security)"
    ]
    if st.button("▶ Start Security Authentication Simulation"):
        for step in security_steps:
            st.error(step)
            time.sleep(1.2)

# ---------------------- Module 5: QoS Profile Mapping ----------------------
def qos_mapping_tool():
    st.subheader("🎯 QoS Profile Mapper")
    st.markdown("Select an application to view its mapped QoS class, delay, and bitrate requirement.")

    app_type = st.selectbox("Select Application Type:", [
        "Voice over IP (VoIP)",
        "Video Streaming",
        "Web Browsing",
        "Email",
        "Real-time Gaming",
        "File Transfer"
    ])

    if st.button("🔍 Show QoS Profile"):
        if app_type == "Voice over IP (VoIP)":
            st.success("**QoS Class:** Conversational\n**Delay:** < 150ms\n**Guaranteed Bitrate:** Yes")
        elif app_type == "Video Streaming":
            st.success("**QoS Class:** Streaming\n**Delay:** < 400ms\n**Guaranteed Bitrate:** Yes")
        elif app_type == "Web Browsing":
            st.success("**QoS Class:** Interactive\n**Delay:** < 1s\n**Guaranteed Bitrate:** No")
        elif app_type == "Email":
            st.success("**QoS Class:** Background\n**Delay:** Tolerant\n**Guaranteed Bitrate:** No")
        elif app_type == "Real-time Gaming":
            st.success("**QoS Class:** Conversational / Interactive\n**Delay:** < 100ms\n**Guaranteed Bitrate:** Yes")
        elif app_type == "File Transfer":
            st.success("**QoS Class:** Background\n**Delay:** Tolerant\n**Guaranteed Bitrate:** No")

# ---------------------- Sidebar Navigation ----------------------
st.sidebar.title("🧭 Navigation")
selected_module = st.sidebar.radio("Choose Module:", (
    "PDP Context Activation",
    "IMS Signaling Flow",
    "Mobile IPv6 Handoff",
    "Security Authentication",
    "QoS Profile Mapping"
))

# ---------------------- Main Dispatcher ----------------------
if selected_module == "PDP Context Activation":
    pdp_context_simulation()
elif selected_module == "IMS Signaling Flow":
    ims_signaling_simulation()
elif selected_module == "Mobile IPv6 Handoff":
    mobility_management_simulation()
elif selected_module == "Security Authentication":
    security_simulation()
elif selected_module == "QoS Profile Mapping":
    qos_mapping_tool()
