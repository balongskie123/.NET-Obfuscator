import requests
import os

# Search GitHub API for ".NET obfuscator"
response = requests.get("https://api.github.com/search/repositories?q=.NET+obfuscator")
new_tools = [repo["html_url"] for repo in response.json()["items"]]

if new_tools:
    # Write new tools to a markdown file
    with open("new_obfuscators.md", "w") as f:
        f.write("## New Tools Found\n")
        f.write("\n".join([f"- {url}" for url in new_tools]))
    
    # Set output using environment files (new method)
    with open(os.environ['GITHUB_OUTPUT'], 'a') as f:
        f.write(f"new_entries=true\n")
else:
    print("No new tools found")