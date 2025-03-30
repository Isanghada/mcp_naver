# server.py
import httpx
import json
import os

from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("NAVER OPEN API", dependencies=["httpx"])


BASE_URL = "https://openapi.naver.com/v1"
API_HEADERS = {
    "X-Naver-Client-Id": os.environ.get("NAVER_CLIENT_ID"),
    "X-Naver-Client-Secret": os.environ.get("NAVER_CLIENT_SECRET")
}

# Using Naver Local API
@mcp.tool(
    name="search_local",
    description="Use the search API to return the results of a search for companies and institutions registered with the neighborhood service in JSON format."
)
async def search_local(
    query:str,
    display:int = 5,
    start:int = 1,
    sort:str = "random"
) -> json:
    """Using Naver Local API

    Args:
        query (str): Query to use for API
        display (int, optional): Number of search results. Defaults to 5. Max to 5.
        start (int, optional): Search Start Location. Defaults to 1. Max to 1.
        sort (str, optional): Sorting Method ("random", "comment"). Defaults to "random".

    Returns:
        json: Return search results in json format
    """
    async with httpx.AsyncClient() as client:
        response = await client.get(f'{BASE_URL}/search/local.json',
                                    params={
                                        "query":query,
                                        "display":display,
                                        "start":start,
                                        "sort":sort
                                    },
                                    headers=API_HEADERS)
        response.raise_for_status()
        return json.load(response.text)

# Using Naver News API
@mcp.tool(
    name="search_news",
    description="Returns the news search results of a neighbor search in JSON format."
)
async def search_news(
    query:str,
    display:int = 10,
    start:int = 1,
    sort:str = "sim"
) -> json:
    """Using Naver News API

    Args:
        query (str): Query to use for API
        display (int, optional): Number of search results. Defaults to 10. Max to 100
        start (int, optional): Search Start Location. Defaults to 1. Max to 1000.
        sort (str, optional): Sorting Method ("sim", "date"). Defaults to "sim".

    Returns:
        json: Return search results in json format
    """
    async with httpx.AsyncClient() as client:
        response = await client.get(f'{BASE_URL}/search/news.json',
                                    params={
                                        "query":query,
                                        "display":display,
                                        "start":start,
                                        "sort":sort
                                    },
                                    headers=API_HEADERS)
        response.raise_for_status()
        return json.load(response.text)

# Using Naver Typing Error Conversion API
@mcp.tool(
    name="search_typing_error_conversion",
    description="Returns the result of incorrectly setting the Korean/English key and correct conversion of the entered search word in JSON format"
)
async def search_typing_error_conversion(query:str) -> json:
    """Using Naver Typing Error Conversion API

    Args:
        query (str): Query to use for API

    Returns:
        json: Return search results in json format
    """
    async with httpx.AsyncClient() as client:
        response = await client.get(f'{BASE_URL}/search/errata.json',
                                    params={"query":query},
                                    headers=API_HEADERS)
        response.raise_for_status()
        return json.load(response.text)