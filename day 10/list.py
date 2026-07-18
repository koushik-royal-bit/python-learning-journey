skills = [
    ["Python", 95],
    ["SQL", 80],
    ["Git", 70]
]

print("Original Skills:")
print(skills)

print("\nTop Skill:")
print(skills[0][0])

print("\nGit Score:")
print(skills[2][1])

skills[1][1] = 90
skills.append(["Linux", 75])
skills.insert(1, ["Pandas", 85])
skills.remove(["Git", 70])

new_skills = [["Docker", 65], ["AWS", 60]]
skills.extend(new_skills)

print("\nUpdated Skills:")
print(skills)

print("\nFinal Skill List:")
print(skills)