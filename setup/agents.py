import sys
from pathlib import Path

# Add the parent directory to the system path
current_dir = Path(__file__).resolve().parent
parent_dir = current_dir.parent
sys.path.append(str(parent_dir))

from textwrap import dedent
from crewai import Agent

from setup.tools import ExaSearchTool
from lib.utils import groq_llm

class MeetingPreparationAgents:
    def research_agent(self):
        return Agent(
                role='Research Specialist',
                goal='Conduct thorough research on people and companies involved in the meeting',
                tools=ExaSearchTool.tools(),
                backstory=dedent("""\
                                As a Research Specilaist, your mission is t uncover detailed information
                                about the individuals and entities participating in the meeting. Your 
                                insights will lay the groundwork for strategic meeting preparation."""),
                llm=groq_llm(),
                verbose=True    
        )
    
    def industry_analysis_agent(self):
        return Agent(
                role='Industry Analyst',
                goal='Analyze the current industry trennds, challenges, and opportunities',
                tools=ExaSearchTool.tools(),
                backstory=dedent("""\
                                As an Industry Analyst, your analysis will identify key trends,
                                challenges facing the industry, and potential opportunities that
                                could be leveraged during the meeting for strategic advantage."""),
                llm=groq_llm(),
                verbose=True
        )
        
    def meeting_strategy_agent(self):
        return Agent(
                role='Meeting Strategy Advisor',
                goal='Develop talking points, questions, and strategic angles for the meeting',
                tools=ExaSearchTool.tools(),
                backstory=dedent("""\
                                As a Strategy Advisor, your expertise will guide the development of
                                talking points, insightful questions, and strategic angles
                                to ensure the meeting's objectives are achieved."""),
                llm=groq_llm(),
                verbose=True
        )
        
    def summary_and_briefing_agent(self):
        return Agent(
                role='Briefing Coordinator',
                goal='Compile all gathered information into a concise, informative briefing document',
                tools=ExaSearchTool.tools(),
                backstory=dedent("""\
                                As the Briefing Coordinator, your role is to consolidate the research,
                                analysis, and strategic insights."""),
                llm=groq_llm(),
                verbose=True
        )