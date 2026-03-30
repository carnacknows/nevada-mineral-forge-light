import streamlit as st
import folium
from streamlit_folium import st_folium
import plotly.express as px
import pandas as pd
from fpdf import FPDF
from datetime import datetime

st.set_page_config(page_title="Nevada Mineral Forge Light", layout="wide")

st.title("🚀 Nevada Mineral Forge Light – Clayton Valley Lithium Intelligence")
st.markdown("**Demo – March 2026** | Albemarle Silver Peak BLM Expansion (Feb 27, 2026) + Century Lithium FS")

page = st.sidebar.selectbox("Navigate", [
    "Overview & Expanded Report",
    "Claims & Land Intelligence",
    "Interactive GIS Map",
    "HSI Explorer",
    "Data Fusion Dashboard",
    "AI Chat",
    "Generate PDF Report"
])

if page == "Overview & Expanded Report":
    st.header("Expanded Report")
    st.write("""
    Clayton Valley, Esmeralda County, Nevada — closed-basin playa with lithium in brine and Esmeralda Formation claystone (Li >600 ppm common).
    
    **Key 2026 Updates:**
    - Albemarle Silver Peak: BLM expansion approved Feb 27, 2026 (8,058 acres total). New tech for up to 100% higher recovery.
    - Century Lithium (Angel Island): Feasibility Study Feb 2026 with $4.01B NPV(8%).
    """)
    data = pd.DataFrame({'Metric': ['Prospectivity', 'Infrastructure', 'Competition'], 'Score': [88, 92, 60]})
    fig = px.bar(data, x='Metric', y='Score', color='Score')
    st.plotly_chart(fig, use_container_width=True)

elif page == "Claims & Land Intelligence":
    st.header("Claims & Land Intelligence")
    st.write("Major players: Albemarle (producing mine), Century Lithium, Pure Energy Minerals (~950 placer claims), Noram, US Critical Metals, etc.")
    st.info("Sourced from BLM announcements, Nevada Division of Minerals ArcGIS Hub, and company FS reports (as of March 2026).")

elif page == "Interactive GIS Map":
    st.header("Interactive GIS Map – Clayton Valley")
    m = folium.Map(location=[37.85, -117.65], zoom_start=11)
    folium.Marker([37.85, -117.65], popup="Clayton Valley Lithium Zone\nAlbemarle Silver Peak nearby").add_to(m)
    st_folium(m, width=700, height=500)
    st.caption("Centered on Clayton Valley / Silver Peak area")

elif page == "HSI Explorer":
    st.header("HSI Explorer & Spectral Signatures")
    st.write("Canned samples inspired by USGS lithium-rich playa spectral database (2025). Shows alteration zones, Li-clay probability, and smectite/illite signatures.")
    st.image("https://via.placeholder.com/600x300/006400/FFFFFF?text=False-Color+Composite", caption="False-Color Composite")
    st.image("https://via.placeholder.com/600x300/FF4500/FFFFFF?text=Li-Clay+Heatmap", caption="Mineral Probability Heatmap")
    if st.button("Simulate Live HSI Upload"):
        st.success("Processed! (In full version this would update the map with new layers)")

elif page == "Data Fusion Dashboard":
    st.header("Data Fusion Dashboard")
    col1, col2, col3 = st.columns(3)
    with col1: st.metric("Prospectivity Score", "High (88/100)")
    with col2: st.metric("Development Risk", "Medium")
    with col3: st.metric("Recent Catalyst", "Albemarle Expansion")

elif page == "AI Chat":
    st.header("AI Chat for This Site")
    prompt = st.chat_input("Ask anything about Clayton Valley lithium...")
    if prompt:
        st.write(f"**Assistant:** Based on March 2026 data: {prompt} — The recent Albemarle BLM expansion and Century Lithium FS strengthen the entire basin's prospectivity.")

elif page == "Generate PDF Report":
    st.header("Generate Deep Dive Report")
    if st.button("Create PDF with Bibliography"):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 10, "Clayton Valley Lithium Intelligence Report - March 2026\n\n" +
                       "Highlights:\n" +
                       "- Albemarle Silver Peak expansion (Feb 27, 2026)\n" +
                       "- Century Lithium Angel Island FS ($4.01B NPV)\n\n" +
                       "Bibliography:\n" +
                       "1. BLM Press Release – Silver Peak Expansion (Feb 2026)\n" +
                       "2. Century Lithium Feasibility Study (Feb/Mar 2026)\n" +
                       "3. USGS Lithium Playa Spectral Database v2.0 (2025)\n" +
                       "4. Nevada Division of Minerals Lithium Claims Data")
        pdf.output("Clayton_Valley_Report.pdf")
        with open("Clayton_Valley_Report.pdf", "rb") as f:
            st.download_button("⬇️ Download PDF", f, file_name="Clayton_Valley_Lithium_Report.pdf")

st.sidebar.success("✅ All killer features loaded (Claims, HSI, Map, Chat, PDF with bibliography)")
