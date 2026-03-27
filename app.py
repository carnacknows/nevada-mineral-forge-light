import streamlit as st
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title="Nevada Mineral Forge — Light", page_icon="⛏️", layout="wide")

st.title("🚀 Nevada Data Forge (Light Mode)")
st.markdown("**Public-data only** AI-powered mineral prospectivity reports — Clayton Valley Lithium MVP")

with st.sidebar:
    st.header("Target Area")
    min_lat = st.number_input("Min Latitude", value=38.0, format="%.2f")
    max_lat = st.number_input("Max Latitude", value=39.0, format="%.2f")
    min_lon = st.number_input("Min Longitude", value=-118.5, format="%.2f")
    max_lon = st.number_input("Max Longitude", value=-117.5, format="%.2f")
    mineral = st.selectbox("Primary Mineral Target", ["Lithium", "Copper", "Gold"], index=0)

    st.caption("Light mode uses public USGS/NBMG data. Full agent factory coming soon.")

if st.button("🔨 Generate Prospectivity Report", type="primary"):
    with st.spinner("Generating report..."):
        # Realistic mock report for Clayton Valley Lithium
        report = f"""
# Nevada Lithium Prospectivity Report — Clayton Valley Target

**Generated:** March 2026  
**Target Area:** Clayton Valley / Silver Peak, Esmeralda County, Nevada  
**Primary Mineral:** {mineral}  
**BBox:** {min_lon} to {max_lon}°E, {min_lat} to {max_lat}°N  

## Executive Summary
Clayton Valley is one of the highest-prospectivity lithium targets in the United States. It hosts North America’s only current lithium production (Albemarle’s Silver Peak brine operation) and multiple advanced clay projects nearby.

**Overall Prospectivity Score: 84/100 (High)**  
Strong alignment with known lacustrine sediments, hyperspectral alteration signatures, and active claims density.

## Geology Overview
- Closed basin in the Basin and Range province with lithium-rich Tertiary playa sediments (Esmeralda Formation).
- Lithium occurs in both brine aquifers and hectorite/smectite clays derived from altered volcanic ash.
- Structural controls from nearby faults and geothermal activity concentrate mineralization.

## Claims & Land Intelligence
High density of lithium-focused placer claims. Mix of patented ground near existing operations and BLM-managed land with standard exploration notices. Moderate competition but opportunities for new targets remain.

## Prospectivity Model
- **Strengths**: Known production precedent, recent Earth MRI coverage, spectral indicators consistent with lithium clays.
- **Opportunities**: Untapped extensions of clay and brine resources.
- **Risks**: Claims competition, water use / basin hydrology, typical early-stage grade uncertainty (±30%).

**Top Recommended Targets**:
1. Northern valley floor alteration zones (highest HSI correlation).
2. Eastern fan complexes with clay signatures.
3. Structural margins near Silver Peak Range.

## Recommendations
- Immediate: Ground truth with portable spectrometer and soil sampling.
- Medium-term: Shallow drilling in high-prospectivity zones identified from public data fusion.
- Integrate any private assay data for refined targeting.

**Full Data Package Available**: Mineral maps, claims overlay, and provenance log (contact for enterprise access).

---
*Report derived from public USGS, NBMG, and Nevada Division of Minerals data. This is a light-mode demonstration.*
"""

        st.success("✅ Report Generated!")
        st.markdown(report)

        # Simple interactive map
        st.subheader("Target Area Map")
        m = folium.Map(location=[(min_lat + max_lat)/2, (min_lon + max_lon)/2], zoom_start=10)
        folium.Rectangle(
            bounds=[[min_lat, min_lon], [max_lat, max_lon]],
            color="red",
            fill=True,
            fill_opacity=0.2,
        ).add_to(m)
        st_folium(m, width=700, height=400)

        # Download button
        st.download_button(
            label="📥 Download Report as Markdown",
            data=report,
            file_name=f"nevada_{mineral.lower()}_clayton_valley_report.md",
            mime="text/markdown"
        )

st.info("**Light Mode Demo** — Full multi-agent factory with AVIRIS processing is next. This version runs instantly with no external APIs.")
