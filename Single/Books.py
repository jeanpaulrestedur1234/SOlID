#Incorrecto

class Library:
    def __init__(self) -> None:
        self.books = []
        self.users = []
        self.loans = []

    def add_books(self, title, author, copies):
        self.books.append({"title": title, "author": author, "copies": copies})
        print(f"📚 Libro agregado: '{title}' por {author} ({copies} copias)")

    def add_user(self, name, id, email):
        self.users.append({"name": name, "id": id, "email": email})
        print(f"👤 Usuario registrado: {name} (ID: {id}, Email: {email})")

    def loan_books(self, user_id, book_title):
        for book in self.books:
            if book["title"] == book_title and book["copies"] > 0:
                book['copies'] -= 1
                self.loans.append({"user_id": user_id, "book_title": book_title})
                print(f"✅ Libro prestado: '{book_title}' al usuario con ID {user_id}")
                return True
        print(f"❌ No se pudo prestar el libro '{book_title}' (no hay copias disponibles o no existe)")
        return False

    def return_book(self, user_id, book_title):
        for loan in self.loans:
            if loan["user_id"] == user_id and loan["book_title"] == book_title:
                self.loans.remove(loan)
                for book in self.books:
                    if book["title"] == book_title:
                        book['copies'] += 1
                        print(f"📥 Libro devuelto: '{book_title}' por el usuario con ID {user_id}")
                        return True
        print(f"⚠️ No se encontró el préstamo de '{book_title}' para el usuario con ID {user_id}")
        return False

print('-'*100)
lib = Library()
lib.add_books("Cien Años de Soledad", "Gabriel García Márquez", 3)
lib.add_user("Juan Pérez", 1, "juan@example.com")

lib.loan_books(1, "Cien Años de Soledad")  # True
lib.return_book(1, "Cien Años de Soledad")  # True


print('-'*100)

##Correcto-----------------
from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str
    copies: int

@dataclass
class User:
    name: str
    id: int
    email: str

class LoanManager:
    def __init__(self):
        self.loans = []

    def loan_book(self, user: User, book: Book) -> bool:
        if book.copies <= 0:
            print(f"❌ No hay copias disponibles para '{book.title}'")
            return False
        book.copies -= 1
        self.loans.append({"user_id": user.id, "book_title": book.title})
        print(f"✅ Libro prestado: '{book.title}' al usuario con ID {user.id}")
        return True

    def return_book(self, user: User, book: Book) -> bool:
        for loan in self.loans:
            if loan["user_id"] == user.id and loan["book_title"] == book.title:
                self.loans.remove(loan)
                book.copies += 1
                print(f"📥 Libro devuelto: '{book.title}' por el usuario con ID {user.id}")
                return True
        print(f"❌ No se encontró un préstamo de '{book.title}' para el usuario con ID {user.id}")
        return False

class Library:
    def __init__(self):
        self.books: list[Book] = []
        self.users: list[User] = []
        self.loan_manager = LoanManager()

    def add_book(self, book: Book):
        if any(b.title == book.title for b in self.books):
            print(f"⚠️ El libro '{book.title}' ya está registrado.")
            return
        self.books.append(book)
        print(f"📚 Libro agregado: '{book.title}' por {book.author} ({book.copies} copias)")

    def add_user(self, user: User):
        if any(u.id == user.id for u in self.users):
            print(f"⚠️ El usuario con ID {user.id} ya está registrado.")
            return
        self.users.append(user)
        print(f"👤 Usuario registrado: {user.name} (ID: {user.id}, Email: {user.email})")

    def loan_book(self, user_id: int, book_title: str) -> bool:
        user = next((u for u in self.users if u.id == user_id), None)
        book = next((b for b in self.books if b.title == book_title), None)
        if not user:
            print(f"❌ Usuario con ID {user_id} no encontrado.")
            return False
        if not book:
            print(f"❌ Libro '{book_title}' no encontrado.")
            return False
        return self.loan_manager.loan_book(user, book)

    def return_book(self, user_id: int, book_title: str) -> bool:
        user = next((u for u in self.users if u.id == user_id), None)
        book = next((b for b in self.books if b.title == book_title), None)
        if not user:
            print(f"❌ Usuario con ID {user_id} no encontrado.")
            return False
        if not book:
            print(f"❌ Libro '{book_title}' no encontrado.")
            return False
        return self.loan_manager.return_book(user, book)

library = Library()

book=Book("Cien Años de Soledad", "Gabriel García Márquez", 3)
user=User("Juan Pérez", 1, "juan@example.com")
# Agregar libro y usuario
library.add_book(book)
library.add_user(user)

# Prestar y devolver
library.loan_book(user.id, book.title)
library.return_book(user.id, book.title)
