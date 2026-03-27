from crewai import Agent, Task, Crew
import os

def create_light_forge_crew(bbox=None, target_mineral="Lithium"):
    # No external search tool for now (to keep it lightweight)
    # The Researcher will use its built-in knowledge + reasoning

    researcher = Agent(
        role="Public Data Researcher",
        goal=f"Gather and summarize public data on {target_mineral} in Nevada, focusing on Clayton Valley and the provided bbox",
        backstory="Expert at recalling and synthesizing open government data from USGS, NBMG, and Nevada Division of Minerals for mineral exploration",
        verbose=True,
        allow_delegation=False,
    )

    geologist = Agent(
        role="Exploration Geologist",
        goal="Synthesize public geology, prospectivity data, and claims into actionable insights and a prospectivity score",
        backstory="Nevada specialist with deep knowledge of Clayton Valley brines, lithium clays, and Basin & Range geology",
        verbose=True,
        allow_delegation=False,
    )

    report_forge = Agent(
        role="Report Forge Master",
        goal="Create a clean, professional markdown prospectivity report with executive summary, risks, and recommendations",
        backstory="Turns raw public data into client-ready insights suitable for PDF export",
        verbose=True,
        allow_delegation=False,
    )

    task_research = Task(
        description=f"Provide the latest known public information for {target_mineral} prospectivity in Clayton Valley / bbox {bbox or 'default Nevada lithium areas'}. Include key USGS lithium statistics, playa rankings, NDOM claims context, and relevant 2024-2026 reports.",
        expected_output="Structured summary with key facts, resources, claims density, recent surveys, and important context",
        agent=researcher,
    )

    task_geology = Task(
        description="Analyze the research output and produce a realistic prospectivity score (0-100), strengths, risks, and specific target recommendations for the area.",
        expected_output="Prospectivity score, bullet-point strengths/opportunities, risk matrix, and ranked drill targets",
        agent=geologist,
    )

    task_report = Task(
        description="Synthesize all outputs into a well-formatted markdown report with clear sections: Executive Summary, Geology, Claims & Land, Prospectivity Model, Risks, Recommendations.",
        expected_output="Complete, professional markdown report text ready for display",
        agent=report_forge,
    )

    crew = Crew(
        agents=[researcher, geologist, report_forge],
        tasks=[task_research, task_geology, task_report],
        verbose=2,
        memory=True,
        cache=True,
    )
    return crew
