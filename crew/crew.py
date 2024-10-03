from crewai import Crew, Process
from tasks import food_writer_task, food_research_task
from agents import res_researcher, res_writer
from tools import tool



crew = Crew(
    agents=[res_researcher, res_writer],
    tasks=[ food_research_task, food_writer_task],
    process=Process.sequential,
)


result = crew.kickoff(inputs={'topic': 'suggest me best veg protein meal to order'})
print(result)