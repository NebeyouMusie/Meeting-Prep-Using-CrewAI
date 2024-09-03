# Meeting Prep Using CrewAI

## Description
- This GitHub repository, "Meeting-Prep-Using-CrewAI", is a project that aims to utilize CrewAI to assist in meeting preparation. The project is written in Python and utilizes the Langchain, CrewAI, and GROQ-API libraries.

## Main Function Points
- Utilize CrewAI to assist in meeting preparation
- Provide a tool to help users prepare for meetings more efficiently

## Libraries Used
- langchain
- langchain-exa
- langchain_groq
- langchain_community
- exa_py
- python-dotenv
- crewai

## File and Folder Explanation
1. `lib`: contains configuration and utility code files.
2. `setup`: contains core building blocks for our crew.
3. `output`: contains the file output of our crew in a markdown foramt.
4. `main.py`: main function that will run our crew.
5. `lib/conifg.py`: contains functions to load our environment variables and get our api keys.
6. `lib/utils.py`: contains a function to initialize our llm.
7. `setup/agents.py`: contains a class for setting up different agents with specific skills and a particular job to do. 
8. `setup/tasks.py`: contains a class for setting up different tasks which are specific assignments completed by agents. 
9. `setup/tools.py`: contains a class for setting up a tool which is a skill or function that agents can utilize to perform various actions. 

## Installation
 1. Prerequisites
    - Git
    - Command line familiarity
 2. Clone the Repository: `git clone https://github.com/NebeyouMusie/Meeting-Prep-Using-CrewAI.git`
 3. Create and Activate Virtual Environment (Recommended)
    - `python -m venv venv`
    - `source venv/bin/activate` for Mac and `venv/bin/activate` for Windows
 4. Navigate to the projects directory `cd ./Meeting-Prep-Using-CrewAI` using your terminal
 5. Install Libraries: `pip install -r requirements.txt`
 6. Enter your `GROQ_API_KEY` and `EXA_SEARCH_API_KEY` in the `example.env` file then change the file to `.env`. You can get your `GROQ_API_KEY` from [here](https://console.groq.com/keys) and your `EXA_SEARCH_API_KEY` from [here](https://dashboard.exa.ai/api-keys)
 7. run `python main.py`
 8. The output will be saved in a folder called `output` in a `meeting_prep.md` markdown format

## Collaboration
- Collaborations are welcomed ❤️

## Acknowledgments
 - I would like to thank [Crew AI](https://docs.crewai.com/)
   
## Contact
 - LinkedIn: [Nebeyou Musie](https://www.linkedin.com/in/nebeyou-musie)
 - Gmail: nebeyoumusie@gmail.com
 - Telegram: [Nebeyou Musie](https://t.me/NebeyouMusie)
