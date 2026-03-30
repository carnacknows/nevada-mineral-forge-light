import streamlit as st
import folium
from streamlit_folium import st_folium
import plotly.express as px
import pandas as pd
from fpdf import FPDF
from datetime import datetime

st.set_page_config(page_title="Nevada Mineral Forge Light", layout="wide")

st.title("🚀 Nevada Mineral Forge Light – Clayton Valley Lithium Intelligence")
st.markdown("**March 2026 Demo** — Populated Claims, Land Intelligence, HSI Samples, Bibliography & All Killer Features")

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
    **Clayton Valley, Nevada** — Closed-basin playa with lithium in brine aquifers and Esmeralda Formation claystone (Li grades commonly >600 ppm).
    
    **2026 Highlights:**
    - Albemarle Silver Peak: Only U.S. producing lithium mine. BLM expansion approved **Feb 27, 2026** — now 8,058 acres with new tech for up to **100% higher recovery**.
    - Century Lithium (Angel Island): Feasibility Study released Feb 2026 with **$4.01 billion** after-tax NPV(8%).
    """)
    data = pd.DataFrame({'Metric': ['Prospectivity', 'Infrastructure', 'Competition'], 'Score': [88, 92, 60]})
    fig = px.bar(data, x='Metric', y='Score', color='Score', title="Key Scores")
    st.plotly_chart(fig, use_container_width=True)

elif page == "Claims & Land Intelligence":
    st.header("Claims & Land Intelligence")
    st.write("""
    Major players in Clayton Valley (as of March 2026):
    - Albemarle (producing operation + recent expansion)
    - Century Lithium (advanced claystone project)
    - Pure Energy Minerals (~950 placer claims, DLE pilot with SLB)
    - Others: Noram Lithium (Zeus), US Critical Metals, etc.
    
    Data from Nevada Division of Minerals ArcGIS Hub and BLM announcements.
    """)
    st.info("High exploration density + strong infrastructure near Silver Peak, but competitive landscape and permitting considerations apply.")

elif page == "Interactive GIS Map":
    st.header("Interactive GIS Map – Clayton Valley")
    m = folium.Map(location=[37.85, -117.65], zoom_start=11, tiles="OpenStreetMap")
    folium.Marker(
        [37.85, -117.65],
        popup="Clayton Valley Lithium Zone<br>Albemarle Silver Peak nearby<br>Century Lithium Angel Island area",
        icon=folium.Icon(color="red", icon="info-sign")
    ).add_to(m)
    st_folium(m, width=800, height=500)
    st.caption("Centered on Clayton Valley / Silver Peak. Toggle base layers in full version (claims, geology, HSI overlays).")

elif page == "HSI Explorer":
    st.header("Hyperspectral Imaging (HSI) Explorer")
    st.write("Canned samples inspired by USGS lithium-rich playa spectral database (ver. 2.0, 2025) — smectite/illite clays, evaporites, alteration minerals.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.image("https://via.placeholder.com/800x450/003300/66FF99?text=False-Color+HSI+Composite+(Clayton+Valley+Alteration+Zones)", caption="False-Color Composite (USGS/AVIRIS-style)")
    with col2:
        st.image("https://via.placeholder.com/800x450/330000/FF9966?text=Li-Clay+Probability+Heatmap+(Smectite/Illite+High)", caption="Mineral Probability Heatmap (Lithium-associated clays)")
    
    if st.button("🧪 Simulate Live HSI Upload & Process"):
        st.success("✅ HSI file processed! Map and report would now update with new mineral probability layers.")

elif page == "Data Fusion Dashboard":
    st.header("Data Fusion Dashboard")
    col1, col2, col3 = st.columns(3)
    with col1: st.metric("Prospectivity", "High (88/100)", "Proximity to producer")
    with col2: st.metric("Risk", "Medium", "Permitting / water")
    with col3: st.metric("Catalyst", "Strong", "Albemarle Feb 2026 expansion")

elif page == "AI Chat":
    st.header("AI Chat for This Site")
    prompt = st.chat_input("Ask about the claims, HSI, or recent expansions...")
    if prompt:
        st.write("**Assistant:** " + prompt + " — The Feb 2026 Albemarle expansion and Century Lithium FS strengthen the entire Clayton Valley basin's lithium potential. USGS HSI data shows strong clay signatures across the playa.")

elif page == "Generate PDF Report":
    st.header("One-Click Deep Dive Report")
    if st.button("Generate PDF (with Bibliography)"):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 10, txt="Nevada Mineral Forge – Clayton Valley Lithium Report\n\nDate: " + datetime.now().strftime("%B %d, %Y") +
                       "\n\nKey Sections:\n• Expanded Report with 2026 data\n• Claims & Land Intelligence\n• HSI Samples from USGS database\n\nBibliography:\n1. BLM Silver Peak Expansion Approval (Feb 27, 2026)\n2. Century Lithium Feasibility Study (Feb/Mar 2026)\n3. USGS Lithium Playa Spectral Database v2.0 (2025)\n4. Nevada Division of Minerals Lithium Claims Open Data")
        pdf.output("Clayton_Valley_Lithium_Report.pdf")
        with open("Clayton_Valley_Lithium_Report.pdf", "rb") as f:
            st.download_button("⬇️ Download Full Report PDF", f, file_name="Clayton_Valley_Lithium_Report.pdf")
        st.success("PDF generated with bibliography!")

st.sidebar.success("✅ All killer features loaded — Claims, Land Intel, HSI (upgraded imagery), Map, Dashboard, Chat, PDF Export")
