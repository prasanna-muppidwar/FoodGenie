from crewai import Task
from tools import tool
from agents import res_researcher, res_writer

# Food Research Task - Restaurant and Recipe Curation
food_research_task = Task(
    description=(
        '''
        As a food researcher, your task is to explore and gather information about local restaurants or food items related to {topic}. 
        You should identify hidden gems, trendy restaurants, or unique dishes that offer exciting culinary experiences. Make sure to 
        highlight their specialties, ambiance, price range, and any notable reviews or accolades. Your findings will be used to curate 
        content for food enthusiasts looking for personalized dining recommendations.
        
        Additionally, search for similar food items or recipes that match the theme of {topic}, providing a well-rounded list of culinary 
        suggestions.
        '''
    ),
    expected_output=(
        '''
        1. A curated list of restaurants offering {topic} dishes, including details such as location, signature dishes, price range, and reviews.
        2. A list of related recipes that can be tried at home, including ingredients and preparation steps.
        '''
    ),
    tools=[tool],
    agent=res_researcher  
)

food_writer_task = Task(
    description=(
        '''
        Your role as a food writer is to create engaging content based on the research provided. This content should tell a compelling story 
        about the food or restaurant experiences related to {topic}, focusing on the flavors, ingredients, atmosphere, and any cultural 
        significance behind the dishes. 

        Ensure that the writing evokes a sensory experience, helping the reader visualize the dish or restaurant environment. You will also 
        need to provide a simple recipe breakdown if applicable, so that readers can attempt to recreate the dish at home.
        '''
    ),
    expected_output=(
        '''
        1. A well-written, engaging article or review that highlights {topic} food items or restaurants.
        2. A detailed description of a related recipe, with clear instructions for preparation.
        '''
    ),
    tools=[tool],
    agent=res_writer, 
    output_file='output.md' 
)


