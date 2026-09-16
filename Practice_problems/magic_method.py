class Book:

    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self): #String representation of the object when printing it directly to the console
        return f"'{self.title}' by {self.author}"

    def __eq__(self,other):#To check if two objects are same
        return self.title == other.title and self.author == other.author

    def __lt__(self,other):#To check if one instance of the class is lesser than the other instance
        return self.num_pages < other.num_pages

    def __gt__(self,other):#To check if one instance is greater than the other
        return self.num_pages > other.num_pages

    def __add__(self,other):#To customize the output when adding two objects as two objects cant be added
        return self.num_pages + other.num_pages

    def __contains__(self,keyword):#To check if a keyword is present in some attribute of an object which can be specified in the dunder function
        return keyword in self.title or keyword in self.author

    def __getitem__(self,key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "pages":
            return self.num_pages
        else:
            return f"Key {key} was not found"


book1 = Book("The Hobbit","J.R.R. Tolkien", 310)
book2 = Book("Harry Potter and the Philosopher's Stone", "J.K Rowling", 223)
book3 = Book("Alice in Wonderland", "Lewis Caroll", 190)

print(book1 == book2)
print(book1 < book2)
print(book1 + book2)
print("Wonderland" in book3)
print(book1["cheese"])