class Group:
    def __init__(self, name, members=[]):
        self.name = name
        self.members = members

    def add(self, name):
        self.members.append(name)

    def get_members(self):
        return sorted(self.members)

    def delete(self, name):
        if name not in self.members:
            raise ValueError("Member not in group")
        else:
            self.members.remove(name)

    def merge(self, new_group):
        for person in new_group.members:
            self.members.append(person)

        return Group("group 8", self.members)


group6 = Group("group6", ["A", "D"])
group7 = Group("group7", ["B", "C"])
merged_group = group6.merge(group7)
