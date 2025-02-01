# scrape_obfuscators.py
import requests

# Search GitHub API for ".NET obfuscator"
response = requests.get("https://api.github.com/search/repositories?q=.NET+obfuscator")
new_tools = [repo["html_url"] for repo in response.json()["items"]]

if new_tools:
    with open("new_obfuscators.md", "w") as f:
        f.write("## New Tools Found\n")
        f.write("\n".join([f"- {url}" for url in new_tools]))
    print(f"::set-output name=new_entries::true")  # Set output for GitHub Actions
else:
    print("No new tools found")