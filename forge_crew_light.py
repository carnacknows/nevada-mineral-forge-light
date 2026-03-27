from crewai import Agent, Task, Crew

def create_light_forge_crew(bbox=None, target_mineral="Lithium"):
    # Super-light version that uses built-in reasoning only (no external LLM calls)

    researcher = Agent(
        role="Public Data Researcher",
        goal=f"Recall and summarize public knowledge about {target_mineral} in Nevada's Clayton Valley.",
        backstory="You are an expert on public USGS, NBMG, and Nevada Division of Minerals data for lithium exploration.",
        verbose=False,
        allow_delegation=False,
    )

    geologist = Agent(
        role="Exploration Geologist",
        goal="Create a realistic prospectivity assessment for the area.",
        backstory="You are a veteran Nevada geologist specializing in lithium brines and clays.",
        verbose=False,
        allow_delegation=False,
    )

    report_forge = Agent(
        role="Report Forge Master",
        goal="Write a clean, professional prospectivity report.",
        backstory="You turn technical summaries into clear executive reports.",
        verbose=False,
        allow_delegation=False,
    )

    task_research = Task(
        description=f"Summarize public data on {target_mineral} in Clayton Valley, Nevada. Include geology, known resources, claims context, and key facts.",
        expected_output="Bullet-point summary of key public facts.",
        agent=researcher,
    )

    task_geology = Task(
        description="Based on the summary, assign a prospectivity score (0-100), list strengths, risks, and 2-3 practical next steps.",
        expected_output="Score + bullet lists for strengths, risks, and recommendations.",
        agent=geologist,
    )

    task_report = Task(
        description="Combine into a professional markdown report with sections: Executive Summary, Geology, Claims & Land, Prospectivity Model, Risks, Recommendations.",
        expected_output="Full markdown report.",
        agent=report_forge,
    )

    crew = Crew(
        agents=[researcher, geologist, report_forge],
        tasks=[task_research, task_geology, task_report],
        verbose=False,
        memory=False,
        cache=True,
    )
    return crew
