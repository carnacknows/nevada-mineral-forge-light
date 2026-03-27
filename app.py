import streamlit as st
from forge_crew_light import create_light_forge_crew

st.set_page_config(page_title="Nevada Mineral Forge — Light", page_icon="⛏️", layout="wide")
st.title("🚀 Nevada Data Forge (Light Mode)")
st.markdown("**Public-data only** AI Agent reports for mineral prospectivity in Nevada — Clayton Valley Lithium MVP")

with st.sidebar:
    st.header("Target Area")
    min_lat = st.number_input("Min Latitude", value=38.0, format="%.2f")
    max_lat = st.number_input("Max Latitude", value=39.0, format="%.2f")
    min_lon = st.number_input("Min Longitude", value=-118.5, format="%.2f")
    max_lon = st.number_input("Max Longitude", value=-117.5, format="%.2f")
    mineral = st.selectbox("Primary Mineral Target", ["Lithium", "Copper", "Gold"], index=0)
    st.caption("Light mode runs fast using only public USGS / NBMG / NDOM data.")

if st.button("🔨 Run Light Forge Analysis", type="primary"):
    with st.spinner("Agents researching public sources and forging the report... (this may take 30-90 seconds)"):
        bbox = (min_lon, min_lat, max_lon, max_lat)
        crew = create_light_forge_crew(bbox=bbox, target_mineral=mineral)
        result = crew.kickoff()
        
        st.success("✅ Report Generated!")
        st.markdown(result)
        
        st.download_button(
            label="📥 Download Report as Markdown",
            data=result,
            file_name=f"nevada_{mineral.lower()}_prospectivity_report.md",
            mime="text/markdown"
        )

st.header("About Light Mode")
st.write("""
- Uses only freely available public data (no large file downloads)
- Fast and reliable on Streamlit Cloud free tier
- Perfect foundation — we can upgrade to full AVIRIS hyperspectral later on a separate backend
""")

st.info("**Tip:** For best search results, add a free Serper API key as a secret in Streamlit Cloud settings (key name: `SERPER_API_KEY`).")
