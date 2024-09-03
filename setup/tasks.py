from textwrap import dedent
from crewai import Task

class MeetingpreparationTasks:
    def research_task(self, agent, participants, context):
        return Task(
            description=dedent(f"""\
                Conduct comprhensive research on each of the individuals and companies
                involved in the upcoming meeting. Gather information on recent
                news, achievements, prfessional background, and any relevant
                business activities.
                
                Participants: {participants}
                Meeting Context: {context}"""),
            expected_output=dedent("""\
                A detailed report summarizing key findings about each participant
                and comapny, highlightig information that could be relevant for the meeting."""),
            async_execution=True,
            agent=agent
        )
    
    def industry_analysis_task(self, agent, participants, context):
        return Task(
            description=dedent("""\
                Analyze the current industry trends, challenges, and opportunities
                relevant to the meeting's context. Consider market reports, recent
                developments, and expert opinions to provide a comprhensive
                overview of the industry landscape.
                
                Participants: {participants}
                Meeting Context: {context}"""),
            expected_output=dedent("""\
                An insightful analysis that identifies major trends, potential
                challenges, and strategic opportunities."""),
            async_execution=True,
            agent=agent
        )
        
    def meeting_strategy_task(self, agent, context, objective):
        return Task(
            description=dedent(f"""\
                Develop strategic talking points, questions, and discussion angles
                for the meeting based on the research and industry analysis conducted
                
                Meeting Context: {context}
                Meeting Objective: {objective}"""),
            expected_output=dedent("""\
                Complete report with a list of key talking points, strategic questions
                to sk to help achieve the meetings objective during the meeting"""),
            agent=agent
        )
        
    def summary_and_briefing_task(self, agent, context, objective):
        return Task(
            description=dedent("""\
                Compile all the research findings, industry anallysis, and strategic
                talking points into a concise, comprhensive briefing document for
                the meeting.
                Ensure the briefing is easy to difest and equips the meeting
                participants with all necessary information and strategies.
                
                Meeting Context: {context}
                Meeting Objective: {objective}"""),
            expected_output=dedent("""\
                A well-structured briefing document that includes sections for
                participants bios, industry overview, talking points, and
                strategic recommendations."""),
            agent=agent,
            output_file='Meeting-Prep-Using-CrewAI/meeting_prep.md'
        )
        