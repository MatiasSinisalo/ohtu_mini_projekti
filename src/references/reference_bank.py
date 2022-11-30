from references.book import Book
class ReferenceBank:
    '''
    Save references
    '''
    def __init__(self):
        self.reference_bank = {}
        self.running_number = 0
        
    def add_reference(self, book:Book):

        refString = self.generate_referenceString(book)
        self.reference_bank[refString] = book



    def generate_referenceString(self, book:Book):

        name = book.author.replace(" ","")
        published = book.year

        first_five_letters = name[0:5].lower()
        generated = first_five_letters+str(published)

        if generated in self.reference_bank.keys():
                generated += f"({self.running_number})"
                self.running_number += 1

        return generated

    def get_reference_bank(self):
        return self.reference_bank
