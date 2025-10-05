class Author:
    def __init__(self, name):
        self.name = name

    def contracts(self):
        # Return list of contracts for this author
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        # Return list of books related to this author through contracts
        return [contract.book for contract in self.contracts()]

    def sign_contract(self, book, date, royalties):
        # Create a new contract for this author and book
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        # Sum up royalties from all contracts related to this author
        return sum(contract.royalties for contract in self.contracts())


class Book:
    def __init__(self, title):
        self.title = title

    def contracts(self):
        # Return list of contracts for this book
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        # Return list of authors related to this book through contracts
        return [contract.author for contract in self.contracts()]


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        # Type validations
        if not isinstance(author, Author):
            raise TypeError("author must be an instance of Author")
        if not isinstance(book, Book):
            raise TypeError("book must be an instance of Book")
        if not isinstance(date, str):
            raise TypeError("date must be a string")
        if not isinstance(royalties, int):
            raise TypeError("royalties must be an integer")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties

        Contract.all.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        """Return all contracts with a specific date, sorted by date overall."""
        sorted_contracts = sorted(cls.all, key=lambda c: c.date)
        return [c for c in sorted_contracts if c.date == date]
