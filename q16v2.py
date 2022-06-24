# This was another method I found while trying to figure it out the first time, this is way cleaner, but more skills that I more or less just googled to figure out the answer.

score = 0
result = ""
class skill: 
    def __init__(self, name, value): 
        self.name = name
        self.value = value

skills = [
    skill("PYTHON", 1),
    skill("RUBY", 2),
    skill("BASH", 4),
    skill("GIT", 8),
    skill("HTML", 16),
    skill("TDD", 32),
    skill("CSS", 64),
    skill("JAVASCRIPT", 128),
]

for skill in skills:
    knows_skill = input(f"Do you know {skill.name}?:")

    if knows_skill == "yes": 
        score = score + skill.value 

    elif knows_skill == "no":
        result = result + skill.name

print("your score is: ",score)
print("You should learn:", result,)

    


