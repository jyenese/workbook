from array import array


score = 0
result = ""

PYTHON = 1
RUBY = 2
BASH = 4
GIT = 8
HTML = 16
TDD = 32
CSS = 64
JAVASCRIPT = 128


skill = input("Do you know Python?:")

if skill == "yes":
    score = score + PYTHON
elif skill == "no":
    result = "Python (1 point)"

skill = input("Do you know Ruby?:")

if skill == "yes": 
    score = score + RUBY
elif skill == "no":
    result = result + ",Ruby (2 points)"

skill = input("Do you know Bash?:")    
if skill == "yes":
    score = score + BASH    
elif skill == "no":
    result = result + ",BASH (4 points)"

skill = input("Do you know Git?:")    
if skill == "yes":
    score = score + GIT
elif skill == "no":
    result = result + ",GIT (8 points)"

skill = input("Do you know HTML?:")    
if skill == "yes":
    score = score + HTML 
elif skill == "no":
    result = result + ",HTML (16 points)"

skill = input("Do you know TDD?:")    
if skill == "yes":
    score = score + TDD   
elif skill == "no":
    result = result + ",TDD (32 points)"

skill = input("Do you know CSS?:")    
if skill == "yes":
    score = score + CSS
elif skill == "no":
    result = result + ",CSS (64 points)"

skill = input("Do you know Javascript??:")    
if skill == "yes":
    score = score + JAVASCRIPT
elif skill == "no":
    result = result + ",JAVASCRIPT (128 points)"

print("Your score is:",score)
print("You should learn:", result)
