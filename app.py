import streamlit as st
import folium
from streamlit_folium import st_folium
from folium.plugins import Draw
from datetime import datetime

st.set_page_config(page_title="Nevada Mineral Forge Light", layout="wide")

st.title("⛏️ Nevada Mineral Forge Light")
st.markdown("**AtomicForge** — Public data forged into mineral intelligence")

tab1, tab2 = st.tabs(["📍 Claims & Land Intelligence", "🔬 HSI On-Demand Analysis"])

with tab1:
    st.header("Claims and Land Intelligence")
    st.info("Your original claims and land intelligence functionality goes here.")
    st.write("This tab remains unchanged from your previous version.")
    # Paste your original claims code here later if desired

with tab2:
    st.header("🔬 Hyperspectral Forge — On-Demand HSI Analysis")
    st.markdown("Turn public Earth MRI / GEMx AVIRIS data into actionable lithium & mineral insights.")

    col_map, col_controls = st.columns([3, 1])

    with col_map:
        st.subheader("📍 Select Area on Map")
        m = folium.Map(location=[38.0, -117.0], zoom_start=7, tiles="CartoDB positron")
        
        Draw(
            draw_options={'polygon': True, 'rectangle': True}
        ).add_to(m)
        
        map_data = st_folium(m, width="100%", height=520, returned_objects=["last_active_drawing"])

    with col_controls:
        st.subheader("Controls")
        if st.button("🚀 Load Clayton Valley Lithium Demo", type="primary"):
            st.success("✅ Clayton Valley / Silver Peak Lithium Demo Loaded")
            st.info("Focus: Lithium-bearing hectorite clays (~2.2–2.3 μm)")

        st.subheader("Spectral Targets")
        targets = st.multiselect(
            "Select mineral indicators",
            options=[
                "Lithium Clays (Hectorite / Smectite ~2.2–2.3 μm)",
                "Gold Alteration (Iron Oxides)",
                "Argillic Alteration",
                "Critical Minerals"
            ],
            default=["Lithium Clays (Hectorite / Smectite ~2.2–2.3 μm)"]
        )

        if st.button("🔥 Run HSI Analysis for This Area", type="primary"):
            with st.spinner("Forging HSI report using public GEMx / Earth MRI data..."):
                st.success("✅ HSI Analysis Complete (Demonstration Mode)")
                
                st.subheader("📊 Forged Report — Clayton Valley Lithium Demo")
                
                st.markdown("""
                **Key Findings** (based on public USGS GEMx and lithium playa studies ver. 2.0):
                - Strong hectorite/smectite spectral signatures detected in playa sediments (~2.2–2.3 μm absorption features).
                - High lithium prospectivity — Clayton Valley is the U.S. benchmark deposit.
                - Fused with local BLM claims data.
                - Recommendation: Prioritize ground sampling / follow-up geochemistry in high-abundance zones.
                """)
                
                # Better placeholder image
                st.image(
                    "https://via.placeholder.com/600x350/FF4500/FFFFFF?text=Hectorite+Abundance+Heatmap+(Clayton+Valley)", 
                    caption="Hectorite Mineral Abundance Heatmap (Demo — Phase 2 will use real AVIRIS raster)"
                )
                
                col_a, col_b = st.columns(2)
                with col_a:
                    st.download_button(
                        label="📥 Download Full PDF Report",
                        data="AtomicForge Nevada HSI Report - Clayton Valley Lithium Demo\n\nKey Findings:\n- Strong hectorite signatures detected\n- High lithium prospectivity\n- Recommended follow-up sampling zones",
                        file_name="Clayton_Valley_HSI_Report.pdf",
                        mime="application/pdf"
                    )
                with col_b:
                    st.download_button(
                        label="📥 Download GeoTIFF (Mock)",
                        data=b"placeholder geotiff data",
                        file_name="hectorite_abundance.tif",
                        mime="image/tiff"
                    )

    st.caption("⚠️ Demonstration using public USGS Earth MRI / GEMx AVIRIS data (~15m resolution). Full on-demand cube processing with local forge coming in Phase 2.")

st.sidebar.info(f"AtomicForge Nevada • {datetime.now().strftime('%Y-%m-%d')}")


