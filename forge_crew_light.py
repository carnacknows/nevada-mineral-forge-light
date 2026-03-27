from crewai import Agent, Task, Crew

def create_light_forge_crew(bbox=None, target_mineral="Lithium"):
    # Ultra-light agents with no external tools or LLM config that forces OpenAI
    researcher = Agent(
        role="Public Data Researcher",
        goal=f"Summarize known public information about {target_mineral} in Nevada's Clayton Valley area.",
        backstory="Reliable synthesizer of USGS, NBMG, and Nevada Division of Minerals public data for mineral exploration.",
        verbose=True,
        allow_delegation=False,
    )

    geologist = Agent(
        role="Exploration Geologist",
        goal="Turn the research into a prospectivity assessment with score, strengths, risks, and recommendations.",
        backstory="Experienced Nevada geologist focused on lithium brines and clays in the Basin and Range.",
        verbose=True,
        allow_delegation=False,
    )

    report_forge = Agent(
        role="Report Forge Master",
        goal="Produce a clean, professional markdown report.",
        backstory="Turns technical insights into clear, client-ready summaries.",
        verbose=True,
        allow_delegation=False,
    )

    task_research = Task(
        description=f"Provide a concise summary of public knowledge on {target_mineral} in Clayton Valley, Nevada (bbox {bbox or 'default area'}). Include key geology, resources, and recent context.",
        expected_output="Structured bullet-point summary of facts and data points.",
        agent=researcher,
    )

    task_geology = Task(
        description="Create a realistic prospectivity score (0-100), list strengths/opportunities, risks, and 2-3 ranked next steps.",
        expected_output="Score + bullet lists for strengths, risks, and recommendations.",
        agent=geologist,
    )

    task_report = Task(
        description="Combine everything into a well-structured markdown report with sections: Executive Summary, Geology, Claims & Land, Prospectivity, Risks, Recommendations.",
        expected_output="Full professional markdown report.",
        agent=report_forge,
    )

    crew = Crew(
        agents=[researcher, geologist, report_forge],
        tasks=[task_research, task_geology, task_report],
        verbose=2,
        memory=False,   # disable memory to reduce LLM pressure
        cache=True,
    )
    return crew
