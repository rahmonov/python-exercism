ALLERGENS = {
    'eggs': 1,
    'peanuts': 2,
    'shellfish': 4,
    'strawberries': 8,
    'tomatoes': 16,
    'chocolate': 32,
    'pollen': 64,
    'cats': 128
}


class Allergies():
    def __init__(self, score):
        self.score = score

    def is_allergic_to(self, name):
        return bool(self.score & ALLERGENS[name])

    @property
    def lst(self):
        return [allergen for allergen in ALLERGENS.keys() if self.is_allergic_to(allergen)]