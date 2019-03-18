

class Donor:
    def __init__(self, name):
        self.name = name
        self.donation = []

    def __name__(self):
        return self.name

    def add_donations(self, amount):
        self.donation.append(amount)

    @property
    def total_donations(self):
        """return total donation of a single donor"""
        return sum(self.donation)

    @property
    def num_donations(self):
        """return number of donations a donor donated"""
        return len(self.donation)

    @property
    def ave_donations(self):
        return self.total_donations / self.num_donations

    @property
    def last_donation(self):
        if len(self.donation) > 0:
            return self.donation[-1]
        else:
            return 0

    def __str__(self):

        return f'{self.name}:{self.donation}'


class DonorCollection():
    def __init__(self):
        self.donors_dict = {}

    def find_donor(self, name):
        if name.lower() in self.donors_dict:
            return self.donors_dict[name.lower()]
        return None

    def add_donor(self, name):
        """allows for adding new donors to the db"""

        new_donor = Donor(name)
        self.donors_dict[new_donor.name] = new_donor
        return new_donor

    def search_donor(self, name):
        return self.donors_dict.get(name.lower())

    @staticmethod
    def sort_key(item):
        return item[1]

    def donor_list(self):
        name_list = [donor.name for donor in self.donors_dict.values()]
        return '\n'.join(name_list)




