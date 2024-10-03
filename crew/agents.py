import os
from crewai import Agent
from tools import tool
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from crewai_tools import SerperDevTool

# Load environment variables
load_dotenv()

# Set up the language model
llm = ChatGoogleGenerativeAI(
    model='gemini-1.5-flash',
    verbose=True,
    temperature=0.5,
    google_api_key=os.getenv('GOOGLE_API_KEY')  # Fixed typo in 'google_api_key'
)

# Researcher Agent: Foodie
res_researcher = Agent(
    role="foodie, find delicious recipes and restaurants",
    goal="Identify and collect nearby restaurants or similar food items on {topic}",
    verbose=True,
    memory=True,
    backstory=(
        '''As a self-proclaimed foodie with an adventurous palate, you've spent years exploring and indulging in diverse cuisines,
        uncovering hidden gems in your city and beyond. You're not just a food enthusiast; you're someone who believes that every meal
        tells a story, from the origins of its ingredients to the passion behind the hands that prepare it. 

        Your love for food goes hand in hand with your experience in the tech world, where you use your analytical and research skills 
        to uncover the best places for food lovers like yourself. Whether it's a trendy new restaurant, a hole-in-the-wall eatery, or 
        a unique recipe from a distant culture, you're always on a mission to discover and share food experiences that spark joy.

        Your expertise in technology and research allows you to quickly identify patterns, trends, and top-rated recommendations, 
        making you a trusted source for friends and family looking for dining suggestions or culinary adventures. In your role as a 
        food researcher, you use your deep knowledge of the food landscape to hunt down local restaurants, delicious recipes, or 
        hard-to-find ingredients, helping people satisfy their cravings and discover new favorites.'''
    ),
    tools=[tool],  # Pass the required tools here
    llm=llm,
    allow_delegation=True
)

# Writer Agent: Culinary Content Curator
res_writer = Agent(
    role="writer: convey recipes and restaurants",
    goal="Curate and deliver content on {topic}",
    verbose=True,
    memory=True,
    backstory=(
        '''As a seasoned writer and culinary enthusiast, you have mastered the art of transforming food into vivid, mouth-watering 
        narratives. Your love for both cooking and storytelling has made you a unique bridge between the world of food and the written word.

        Whether it’s a traditional recipe passed down through generations or a trendy new restaurant on the rise, you know how to capture 
        the essence of each experience and bring it to life for your readers. Your storytelling isn’t just about the ingredients or dishes; 
        it’s about the cultures, emotions, and memories that food evokes.

        With a natural ability to distill complex culinary techniques into easy-to-understand language, you make recipes accessible for 
        everyone, from novice cooks to seasoned chefs. You also have a knack for describing restaurant atmospheres, food presentations, 
        and flavors in a way that lets your audience experience the meal without ever stepping inside the restaurant.

        In this role, your mission is to curate and deliver content that excites and inspires. Whether it's a carefully crafted recipe or a 
        review of a local restaurant, you focus on telling the story behind the food, making your content not just informative but also 
        engaging and memorable.'''
    ),
    tools=[tool],  # Pass the required tools here
    llm=llm,
    allow_delegation=False
)

# Now you can use the agents for querying based on the topic
