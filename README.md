# Nevada Data Forge (Light Mode) ⛏️

**AI Agent Factory for Mineral Prospectivity Reports**  
Uses only **public-domain data** (USGS lithium reports, NBMG Open Data, Nevada Division of Minerals claims) + CrewAI multi-agent workflow → clean, professional reports in minutes.

Built for the Nevada MVP with focus on **Clayton Valley lithium** (the only producing lithium operation in the US). Designed to deploy instantly on **Streamlit Community Cloud**.

## Features
- Instant prospectivity reports from public sources only
- Targets: Lithium (default), Copper, Gold
- Executive summary, geology overview, claims intelligence, risk matrix, drill recommendations
- Simple Streamlit UI with bbox picker and one-click “Run Forge”
- Fully open-source and MIT licensed

## Quick Deploy to Streamlit
1. Fork this repo (optional but recommended)
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Click "New app" → paste your GitHub repo URL → Deploy

## Tech Stack
- CrewAI (Apache 2.0)
- Streamlit
- Public data: USGS, NBMG, Nevada Division of Minerals (NDOM)
- All dependencies are open-source friendly

## Roadmap
- Light mode (live now) — public data only
- Heavy mode (next) — full AVIRIS hyperspectral processing on a GPU backend
- Marketplace store for generated reports

## License
MIT — free to fork, modify, and build commercial products on top of it.
