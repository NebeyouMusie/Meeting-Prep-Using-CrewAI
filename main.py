import sys
from pathlib import Path

# Add the parent directory to the system path
current_dir = Path(__file__).resolve().parent
parent_dir = current_dir.parent
sys.path.append(str(parent_dir))

from crewai import Crew

from setup.tasks import MeetingpreparationTasks
from setup.agents import MeetingPreparationAgents

agents = MeetingPreparationAgents()
tasks = MeetingpreparationTasks()

print("## Welcome to Meeting Prep Crew")
print("-------------------------------")
participants = input("What are the participants (other than you) in the meeting?\n")
context = input("What is the context of the meeting?\n")
objective = input("What is your objective for this meeting?\n")


# Create Agents
researcher_agent = agents.research_agent()
industry_analyst_agent = agents.industry_analysis_agent()
meeting_strategy_agent = agents.meeting_strategy_agent()
summary_and_briefing_agent = agents.summary_and_briefing_agent()

# Create Tasks
research = tasks.research_task(researcher_agent, participants, context)
industry_analysis = tasks.industry_analysis_task(industry_analyst_agent, participants, context)
meeting_strategy = tasks.meeting_strategy_task(meeting_strategy_agent, context, objective)
summary_and_briefing = tasks.summary_and_briefing_task(summary_and_briefing_agent, context, objective)

meeting_strategy.context = [research, industry_analysis]
summary_and_briefing.context = [research, industry_analysis, meeting_strategy]

# Create crew responsible for Copy
crew = Crew(
        agents=[
            researcher_agent,
            industry_analyst_agent,
            meeting_strategy_agent,
            summary_and_briefing_agent
        ],
        tasks=[
            research,
            industry_analysis,
            meeting_strategy,
            summary_and_briefing
        ]
)

result = crew.kickoff()

# Print results
print("\n\n################################################")
print("## Here is the result")
print("################################################\n")
print(result)