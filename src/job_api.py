import os
from dotenv import load_dotenv, find_dotenv
from apify_client import ApifyClient

load_dotenv(find_dotenv())

APIFY_API_TOKEN = os.getenv("APIFY_API_TOKEN")
os.environ["APIFY_API_TOKEN"] = APIFY_API_TOKEN

apify_client = ApifyClient(APIFY_API_TOKEN)


# Fetch jobs from LinkedIn using Apify
def fetch_linkedin_jobs(search_query, location="Mexico", rows=60):
    run_input = {
        "title": search_query,
        "location": location,
        "rows": rows,
        "proxy": {
            "useApifyProxy": True,
            "apifyProxyGroups": ["RESIDENTIAL"],
        }
    }
    run = apify_client.actor("BHzefUZlZRKWxkTck").call(run_input=run_input)
    print(run)
    jobs = list(apify_client.dataset(run["defaultDatasetId"]).iterate_items())
    return jobs
