import streamlit as st
import random
import datetime
import io

st.set_page_config(page_title="NextGen Wireless Network Simulator", layout="wide")

# Title
st.title("📡 NextGen Wireless Network Simulator")
st.markdown("An interactive tool to simulate 4G/5G wireless networks.")

# Sidebar - Configuration
st.sidebar.header("🛠️ Network Configuration")

network_type = st.sidebar.selectbox("Select Network Type", ["4G LTE", "5G NR"])
num_devices = st.sidebar.slider("Number of Connected Devices", 1, 200, 50)
environment = st.sidebar.selectbox("Deployment Environment", ["Urban", "Suburban", "Rural"])
traffic_type = st.sidebar.selectbox("Traffic Profile", ["VoIP", "Video", "Web", "IoT"])

# Function to simulate performance metrics
def simulate_metrics(devices, net_type, traffic, env):
    if net_type == "4G LTE":
        base_throughput = random.uniform(30, 70)
        base_latency = random.uniform(20, 60)
    else:  # 5G NR
        base_throughput = random.uniform(150, 1000)
        base_latency = random.uniform(1, 20)

    # Traffic impact
    traffic_modifiers = {
        "VoIP": (1.1, 0.9),
        "Video": (0.85, 1.2),
        "Web": (1.0, 1.0),
        "IoT": (1.2, 0.8),
    }
    t_mult, l_mult = traffic_modifiers[traffic]

    # Device impact
    scale_factor = max(1.0, devices / 50.0)
    throughput = base_throughput * t_mult / scale_factor
    latency = base_latency * l_mult * scale_factor

    return round(throughput, 2), round(latency, 2)

# Function to generate coverage range
def get_coverage(env, net_type):
    base_ranges = {
        "Urban": 1,
        "Suburban": 2.5,
        "Rural": 5,
    }
    multiplier = 1.0 if net_type == "4G LTE" else 0.8
    return round(base_ranges[env] * multiplier, 2)

# Simulate button
if st.button("🚀 Run Simulation"):
    throughput, latency = simulate_metrics(num_devices, network_type, traffic_type, environment)
    coverage = get_coverage(environment, network_type)

    st.success("✅ Simulation Complete")
    
    col1, col2, col3 = st.columns(3)
    col1.metric("📶 Network Type", network_type)
    col2.metric("⚙️ Devices", num_devices)
    col3.metric("🌍 Environment", environment)

    st.subheader("📊 Performance Metrics")
    st.metric("Throughput (Mbps)", f"{throughput}")
    st.metric("Latency (ms)", f"{latency}")
    st.metric("Estimated Cell Coverage (km)", f"{coverage}")

    st.subheader("📡 Network Topology Summary")
    st.code(f"""
Network Type: {network_type}
Traffic Type: {traffic_type}
Devices: {num_devices}
Environment: {environment}
Throughput: {throughput} Mbps
Latency: {latency} ms
Coverage Radius: {coverage} km
    """, language="text")

    # Generate downloadable report
    def generate_report():
        report = f"""
===== NextGen Wireless Network Report =====
Timestamp: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

Network Type     : {network_type}
Traffic Profile  : {traffic_type}
Environment      : {environment}
Devices Connected: {num_devices}

--- Simulation Results ---
Throughput        : {throughput} Mbps
Latency           : {latency} ms
Coverage Estimate : {coverage} km

Thank you for using NextGen Simulator!
        """
        return report

    report_text = generate_report()
    st.download_button(
        label="📥 Download Report as .txt",
        data=report_text,
        file_name="network_report.txt",
        mime="text/plain"
    )

else:
    st.info("Click 'Run Simulation' to begin.")
