from mcp.server.fastmcp import FastMCP
from src.job_api import fetch_linkedin_jobs

mcp = FastMCP("Job Recommender")

@mcp.tool()
async def fetch_linkedin(listofkeywords):
    return fetch_linkedin_jobs(listofkeywords)

if __name__ == "__main__":
    mcp.run(transport='stdio')