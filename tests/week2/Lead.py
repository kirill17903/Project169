class Lead:
    def __init__(self, name):
        self.name = name


def change_name(lead, new_name):
    lead.name = new_name


my_lead = Lead("Алексей")
print(f"До: {my_lead.name}")
change_name(my_lead, "Максим")
print(f"После: {my_lead.name}")