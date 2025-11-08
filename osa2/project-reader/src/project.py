class Project:
    def __init__(self, name, description, license, authors, dependencies, dev_dependencies):
        self.name = name
        self.description = description
        self.license = license
        self.authors = authors
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def _stringify_dependencies(self, dependencies):
        return ", ".join(dependencies) if len(dependencies) > 0 else "-"
    
    def _viivat_(self, authors):
        return "\n" + "\n".join(f"- {author}" for author in authors)

    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.license}"
            f"\nAuthors: {self._viivat_(self.authors)}"
            f"\nDependencies: {self._viivat_(self.dependencies)}"
            f"\nDevelopment dependencies: {self._viivat_(self.dev_dependencies)}"
        )
