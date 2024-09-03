import sys
from pathlib import Path

# Add the parent directory to the system path
current_dir = Path(__file__).resolve().parent
parent_dir = current_dir.parent
sys.path.append(str(parent_dir))

from exa_py import Exa
from langchain.agents import tool

from lib.config import get_exa_search_api_key

class ExaSearchTool:
    @tool
    def search(query: str):
        """Search for a webpage based on query"""
        return ExaSearchTool._exa().search(f"{query}", use_autoprompt=True, num_results=3)
    
    @tool
    def find_similar(url: str):
        """Search for webpages similar to a given URL.
        The URL passed in should be the URL returned from `search`"""
        return ExaSearchTool._exa().find_similar(url, num_results=3)
    
    @tool
    def get_contents(ids: str):
        """Get the contents of webpage.
        The ids must be passed in as a list, a list of ids returned from `search`"""
        ids = eval(ids)
        contents = str(ExaSearchTool._exa().get_contents(ids))
        print(contents)
        contents = contents.split("URL:")
        contents = [content[:1000] for content in contents]
        return "\n\n".join(contents)
    
    def tools():
        return [ExaSearchTool.search, ExaSearchTool.find_similar, ExaSearchTool.get_contents]
    
    def _exa():
        return Exa(api_key=get_exa_search_api_key()) 