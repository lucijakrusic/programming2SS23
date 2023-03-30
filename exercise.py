"""
Let's make a citation system that will allow us to create a bibliography of sorts.
The first thing we want to do is to define a Publication class
the class shoula have an autor, title and publisher.

We should also be mindful that noone touches our properties are protected by convention.
We should also write a get_citation() method that will return the author, title an publisher string nicely formatted.
"""


class Publication:

   def __eq__(self, __o) -> bool:
       """indicates that the method returns a bool value"""
       return self._author == __o._author \
           and self._title == __o._title


"""
In Python, the __eq__() method is a special method used for comparing two objects for equality. 
When you use the == operator in Python, it calls the __eq__() method internally to compare the two objects.
The __eq__() method here checks if two publication objects are equal. 
It does this by comparing the author and title attributes of both objects. 
If they are equal, the method returns True; otherwise, it returns False.
Here we're doing it so that we avoid duplicate citations.
BTW. the '\' is just for breaking one line in two (for readability) - a continuation character
"""
# -----------------------------------------------------

"""
Let's make a book object that inherits from the publication.
It has an author, title, publisher, year and isbn

"""


class Book(Publication):
    """A Book"""

    def __init__(self, author, title, publisher, year, isbn):
        """Creates a book object with"""
        super().__init__(author, title, publisher)


"""
The super() function is used to call a method in a parent class from a subclass. 
In this case, the super().__init__(author, title, publisher) line calls the __init__() method of the Publication class with the author,
 title, and publisher arguments.
 This initializes the corresponding attributes of the Book object using the constructor of the Publication class.
"""

# -------------------------------------------------------------


"""
Let's make an article class that inherits from the publication and
creates an article of a volume or journal.

It inherits an author, title, publisher and also has a book_title and pages

"""


# -------------------------------------------------------------
"""
Let's make an author class that creates an author with a first name and last name
let's also make sure we don't have duplicate authors and 
use the __str__method to return a nicely formatted firstname, lastname
"""


# ----------------------------------------------------------------

""" let's make the same for the publisher. the publisher has a name and address
we also want a __str__ method to nicely print out publisher:address"""


if __name__ == '__main__':

 """The if __name__ == '__main__': statement is a common pattern used in Python modules to
   allow the module to be run as a script or used as a module in another program.

When a Python module is imported, its code is executed immediately. The if __name__ == '__main__': 
statement allows you to write code in the module that will only be executed if the module is run as the main program (i.e., not imported by another module).

Let's create some author and publisher objects.
After that let's create a couple of books
Let's add the books to a tuple called books.
Finally, let's use a loop to print out the citation for each book using the get_citation() method
 """
