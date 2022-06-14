import  requests

response = requests.get("https://gitlab.com/api/v4/users/marv254/projects")
my_projects = response.json()

for project in my_projects:
    print(f"Project Name: {project['name']} Project Url: {project['web_url']}")
