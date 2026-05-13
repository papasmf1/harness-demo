class Developer:
    def __init__(self, name: str, language: str, years_of_experience: int):
        self.name = name
        self.language = language
        self.years_of_experience = years_of_experience
        self.skills: list[str] = []
        self.projects: list[str] = []

    def add_skill(self, skill: str) -> None:
        if skill not in self.skills:
            self.skills.append(skill)

    def add_project(self, project: str) -> None:
        self.projects.append(project)

    def introduce(self) -> str:
        skills_str = ", ".join(self.skills) if self.skills else "없음"
        return (
            f"안녕하세요, 저는 {self.name}입니다. "
            f"주 언어는 {self.language}이고, "
            f"경력은 {self.years_of_experience}년입니다. "
            f"보유 스킬: {skills_str}"
        )

    def __repr__(self) -> str:
        return f"Developer(name={self.name!r}, language={self.language!r}, years={self.years_of_experience})"


if __name__ == "__main__":
    dev = Developer(name="김철수", language="Python", years_of_experience=3)
    dev.add_skill("Django")
    dev.add_skill("FastAPI")
    dev.add_project("쇼핑몰 백엔드")
    print(dev.introduce())
    print(dev)
