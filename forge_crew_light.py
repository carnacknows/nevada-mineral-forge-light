from crewai import Agent, Task, Crew

def create_light_forge_crew(bbox=None, target_mineral="Lithium"):
    researcher = Agent(
        role="Public Data Researcher",
        goal=f"Summarize known public information about {target_mineral} in Nevada's Clayton Valley area.",
        backstory="Reliable synthesizer of USGS, NBMG, Nevada Division of Minerals, and Earth MRI public data.",
        verbose=False,
        allow_delegation=False,
    )

    geologist = Agent(
        role="Exploration Geologist",
        goal="Analyze the summary and generate a prospectivity score (0-100), strengths, risks, and recommendations.",
        backstory="Experienced Nevada geologist specializing in lithium brines and clays in the Basin and Range.",
        verbose=False,
        allow_delegation=False,
    )

    report_forge = Agent(
        role="Report Forge Master",
        goal="Produce a clean, professional markdown report.",
        backstory="Turns technical insights into clear, executive-level summaries.",
        verbose=False,
        allow_delegation=False,
    )

    task_research = Task(
        description=f"Provide a factual summary of public data on {target_mineral} in Clayton Valley, Nevada. Include key geology, resources, claims context, and recent public reports.",
        expected_output="Concise structured summary with key facts.",
        agent=researcher,
    )

    task_geology = Task(
        description="Generate a prospectivity score (0-100), strengths/opportunities, risks, and 2-3 ranked next steps or drill targets.",
        expected_output="Score + bullet lists for strengths, risks, and recommendations.",
        agent=geologist,
    )

    task_report = Task(
        description="Combine everything into a professional markdown report with these sections: Executive Summary, Geology, Claims & Land, Prospectivity Model, Risks, Recommendations.",
        expected_output="Full, well-formatted markdown report.",
        agent=report_forge,
    )

    crew = Crew(
        agents=[researcher, geologist, report_forge],
        tasks=[task_research, task_geology, task_report],
        verbose=False,   # Must be boolean
        memory=False,
        cache=True,
    )
    return crew
