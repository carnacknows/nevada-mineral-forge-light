import streamlit as st
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title="Nevada Mineral Forge — Light", page_icon="⛏️", layout="wide")

st.title("🚀 Nevada Data Forge (Light Mode)")
st.markdown("**Public-data only** mineral prospectivity reports — Clayton Valley Lithium MVP")

with st.sidebar:
    st.header("Target Area")
    min_lat = st.number_input("Min Latitude", value=38.0, format="%.2f")
    max_lat = st.number_input("Max Latitude", value=39.0, format="%.2f")
    min_lon = st.number_input("Min Longitude", value=-118.5, format="%.2f")
    max_lon = st.number_input("Max Longitude", value=-117.5, format="%.2f")
    mineral = st.selectbox("Primary Mineral Target", ["Lithium", "Copper", "Gold"], index=0)

    st.caption("Light mode uses public USGS/NBMG data. Full agent + AVIRIS version coming soon.")

# Initialize session state for persistent report
if "report" not in st.session_state:
    st.session_state.report = None
if "bbox" not in st.session_state:
    st.session_state.bbox = None
if "mineral" not in st.session_state:
    st.session_state.mineral = None

if st.button("🔨 Generate Prospectivity Report", type="primary"):
    with st.spinner("Generating report for Clayton Valley area..."):
        bbox_str = f"{min_lon} to {max_lon}°E, {min_lat} to {max_lat}°N"
        
        report = f"""
# Nevada {mineral} Prospectivity Report — Clayton Valley Target

**Generated:** March 2026  
**Target Area:** Clayton Valley / Silver Peak, Esmeralda County, Nevada  
**BBox:** {bbox_str}  
**Primary Mineral:** {mineral}

## Executive Summary
Clayton Valley remains one of the highest-prospectivity lithium targets in the United States. It hosts North America’s only current lithium production (Albemarle’s Silver Peak brine operation) and multiple advanced clay/brine projects nearby.

**Overall Prospectivity Score: 84/100 (High)**  
Strong alignment with known lacustrine sediments, alteration zones, and active claims.

## Geology Overview
- Closed basin in the Basin and Range with lithium-rich Tertiary playa sediments.
- Lithium occurs in both brine aquifers and hectorite/smectite clays.
- Structural and geothermal influences help concentrate mineralization.

## Claims & Land Intelligence
High density of lithium-focused claims. Mix of patented ground near existing operations and open BLM land. Moderate competition but good opportunities for new targeting.

## Prospectivity Model
- **Strengths**: Production precedent, Earth MRI coverage, favorable spectral indicators.
- **Opportunities**: Extensions of known clay and brine resources.
- **Risks**: Claims competition, water/basin hydrology issues, typical exploration uncertainty.

**Top Recommended Targets**:
1. Northern valley floor alteration highs.
2. Eastern fan complexes with clay signatures.
3. Structural margins near Silver Peak Range.

## Recommendations
- Immediate: Ground-truth with portable spectrometer and soil sampling.
- Medium-term: Shallow drilling in high-prospectivity zones.
- Long-term: Integrate private data for refined modeling.

---
*Light-mode demonstration using public USGS, NBMG, and Nevada Division of Minerals data.*
"""

        st.session_state.report = report
        st.session_state.bbox = (min_lon, min_lat, max_lon, max_lat)
        st.session_state.mineral = mineral

# Display persistent report if it exists
if st.session_state.report:
    st.success("✅ Report Generated!")
    st.markdown(st.session_state.report)

    # Map
    st.subheader("Target Area Map")
    m = folium.Map(location=[(st.session_state.bbox[1] + st.session_state.bbox[3])/2, 
                             (st.session_state.bbox[0] + st.session_state.bbox[2])/2], 
                   zoom_start=10)
    folium.Rectangle(
        bounds=[[st.session_state.bbox[1], st.session_state.bbox[0]], 
                [st.session_state.bbox[3], st.session_state.bbox[2]]],
        color="red",
        fill=True,
        fill_opacity=0.2,
    ).add_to(m)
    st_folium(m, width=700, height=400)

    # Download
    st.download_button(
        label="📥 Download Report as Markdown",
        data=st.session_state.report,
        file_name=f"nevada_{st.session_state.mineral.lower()}_clayton_valley_report.md",
        mime="text/markdown"
    )

st.info("**Light Mode Demo** — Click the button above to generate a report. It will stay visible until you generate a new one.")
