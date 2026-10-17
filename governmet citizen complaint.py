"""
Citizen Complaint System (Government domain)
PROG211 - Object-Oriented Programming 1

DPG alignment:
- Open-source: intended to be hosted on GitHub.
- Inclusive: simple text menu-free design, plain language messages.
- Privacy-respecting: no names, phone numbers or addresses are stored.
  Citizens are identified only by an anonymous code.
- Modular and reusable: each class has one job and can be reused.
"""

# Tuples (optional bonus): fixed values that should never change.
CATEGORIES = ("Water", "Electricity", "Roads", "Waste", "Health", "Other")
STATUSES = ("Open", "In Progress", "Resolved")


class Citizen:
    """Anonymous citizen: only a generated code, no personal data."""

    total_citizens = 0  # class attribute

    def __init__(self, district):
        Citizen.total_citizens += 1
        self.citizen_code = f"CIT{Citizen.total_citizens:03d}"
        self.district = district  # general area only, not an address

    def display_info(self):
        print(f"Citizen {self.citizen_code} | District: {self.district}")

    @classmethod
    def get_total_citizens(cls):
        """Class method: how many anonymous citizens are registered."""
        return cls.total_citizens


class Complaint:
    """A single complaint filed by a citizen."""

    total_complaints = 0  # class attribute

    def __init__(self, citizen, category, description):
        if category not in CATEGORIES:
            category = "Other"
        Complaint.total_complaints += 1
        self.complaint_id = f"CMP{Complaint.total_complaints:03d}"
        self.citizen = citizen  # interaction: Complaint uses a Citizen object
        self.category = category
        self.description = description
        self.status = STATUSES[0]  # "Open"

    def update_record(self, new_status):
        """Instance method: change the complaint status."""
        if new_status in STATUSES:
            self.status = new_status
            print(f"{self.complaint_id} updated to '{self.status}'.")
        else:
            print(f"Invalid status. Choose from {STATUSES}.")

    def display_info(self):
        """Instance method: show complaint details."""
        print(
            f"{self.complaint_id} | {self.category} | {self.status} | "
            f"By {self.citizen.citizen_code} ({self.citizen.district})\n"
            f"   -> {self.description}"
        )

    @classmethod
    def get_total_complaints(cls):
        """Class method: how many complaints have been created."""
        return cls.total_complaints

    @staticmethod
    def is_valid_description(text):
        """Static method: description must have at least 10 characters."""
        return len(text.strip()) >= 10


# The ONE data structure: a dictionary with complaint_id as the key.
complaints_db = {}


def add_complaint(complaint):
    """Add a complaint to the dictionary."""
    complaints_db[complaint.complaint_id] = complaint
    print(f"Complaint {complaint.complaint_id} added successfully.")


def display_complaints():
    """Display every complaint stored in the dictionary."""
    print("\n--- ALL COMPLAINTS ---")
    if not complaints_db:
        print("No complaints recorded yet.")
        return
    for complaint in complaints_db.values():
        complaint.display_info()


def main():
    # Task 1: object creation
    citizen1 = Citizen("Western Area Urban")
    citizen2 = Citizen("Bo District")
    citizen1.display_info()
    citizen2.display_info()

    # Interaction between objects: Complaint receives a Citizen
    desc1 = "No running water in our community for two weeks."
    desc2 = "Large potholes on the main road near the market."
    desc3 = "Short"

    if Complaint.is_valid_description(desc1):
        add_complaint(Complaint(citizen1, "Water", desc1))
    if Complaint.is_valid_description(desc2):
        add_complaint(Complaint(citizen2, "Roads", desc2))
    if not Complaint.is_valid_description(desc3):
        print("Complaint rejected: description too short.")

    # Task 2: display from the data structure
    display_complaints()

    # Task 3: instance method updates a stored object
    print()
    complaints_db["CMP001"].update_record("In Progress")
    complaints_db["CMP002"].update_record("Resolved")
    display_complaints()

    # Task 3: class methods
    print(f"\nTotal citizens: {Citizen.get_total_citizens()}")
    print(f"Total complaints: {Complaint.get_total_complaints()}")


if __name__ == "__main__":
    main()