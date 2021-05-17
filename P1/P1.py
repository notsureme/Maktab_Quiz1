import dill
import pickle, datetime

class Book:
    ISBN: int
    name: str
    author: str
    publisher: str
    publish_date: datetime.date
def __init__(self, ISBN, name, author, publisher,
publish_date):
    self.ISBN = ISBN
    self.name = name
    self.author = author
    self.publisher = publisher
    self.publish_date = publish_date



with open('books.pkl', 'rb') as file:
    obj = pickle.load(file)

my_obj = []

for element in obj:
    my_obj.append(element)

def sort_it(element):
    return element.ISBN


list2 = sorted(my_obj, key=sort_it)
for element in list2:
    print(element.ISBN,element.name, element.author, element.publisher, element.publish_date)


def sort_it(element):
    return element.name

list2 = sorted(my_obj,key=sort_it)

for element in list2:
    print(element.ISBN,element.name, element.author, element.publisher, element.publish_date)


def sort_it(element):
    return element.publisher_date

list2 = sorted(my_obj, key=sort_it)

for element in list2:
    print(element.ISBN, element.name, element.author, element.publisher, element.publish_date)

    