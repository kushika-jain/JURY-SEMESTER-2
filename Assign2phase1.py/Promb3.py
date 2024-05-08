"""Using Datatypes - Study Drill Complex Datatypes
Stage-0 In this task you have to practise list, tuple and Dictionary.
Stage-1 Combine and Learn about all the data types (Like how they behave? What can be
achieved using them together?)
Stage-3 Think of a situation/case where you can use all of the data types together (Create
Scenario)
Stage-4 Discuss your findings
"""
party_members = [
    ("PM001", "Kushika", "Leader"),
    ("PM002", "Juhi", "Deputy Leader"),
    ("PM003", "Muskan", "Secretary")
]

memberships = {
    "Party Committee": ["PM001", "PM002", "PM003"],
    "Fundraising Team": ["PM001", "PM003"],
    "Media Team": ["PM002"]
}

party_members.append(("PM004", "Kunika", "Treasurer"))

memberships["Party Committee"].append("PM004")

memberships["Media Team"].remove("PM002")

print("Party Members:")
for member in party_members:
    print(member)

print("\nMemberships:")
for team, members in memberships.items():
    print(team, ":", members)
