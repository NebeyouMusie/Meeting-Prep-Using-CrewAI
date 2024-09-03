import sys
from pathlib import Path

# Add the parent directory to the system path
current_dir = Path(__file__).resolve().parent
parent_dir = current_dir.parent
sys.path.append(str(parent_dir))

from exa_py import Exa
from langchain.agents import tool

from lib.config import get_exa_search_api_key, load_config

load_config()

class ExaSearchTool:
    @tool
    def search_and_contents(query: str):
        """Search for webpages based on the query and retrieve their contents."""
        # This combines two API endpoints: search and contents retrieval
        return ExaSearchTool.exa.search_and_contents(
            query, use_autoprompt=True, num_results=5, text=True, highlights=True
        )


    @tool
    def find_similar_and_contents(url: str):
        """Search for webpages similar to a given URL and retrieve their contents.
        The url passed in should be a URL returned from `search_and_contents`.
        """
        # This combines two API endpoints: find similar and contents retrieval
        return ExaSearchTool.exa.find_similar_and_contents(url, num_results=5, text=True, highlights=True)
    
    def tools():
        return [ExaSearchTool.search_and_contents, ExaSearchTool.find_similar_and_contents]
    
    def exa():
        
        return Exa(api_key=get_exa_search_api_key()) 