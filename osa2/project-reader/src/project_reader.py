import tomli
from urllib import request
from project import Project


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        data = tomli.loads(content)

        poetry = data["tool"]["poetry"]

        name = poetry.get("name", "")
        description = poetry.get("description", "")
        license = poetry.get("license", "")
        authors = poetry.get("authors", "")
        dependencies = list(poetry.get("dependencies", {}).keys())

        dev_dependencies = list(
            poetry.get("group", {})
                 .get("dev", {})
                 .get("dependencies", {})
                 .keys()
        )

        return Project(name, description, license, authors, dependencies, dev_dependencies)