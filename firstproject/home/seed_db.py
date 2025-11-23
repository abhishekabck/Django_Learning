from home.models import *
from faker import Faker
import random

from home.models import Book, Author

fake = Faker('en_IN')

def dbSeeder() -> None: # college
    college_names = [
        'IIT Madaras', 'KNIT Sultanpur', 'Lucknow University',
        'MMMUT', 'VIT Chennai', 'Lovely Professional university',
        'Chandigarh university', 'Ms Ramaiah', 'NIT Trichy', 'PSIT',
    ]
    for cname in college_names:
        address = fake.address()
        College.objects.create(
            college_name = cname,
            college_address = address
        )

def dbSeeder2(records = 10) -> None:  # student table
    colleges = College.objects.all()
    for i in range(records):
        college = random.choice(colleges)
        name = fake.name()
        email = fake.email()
        mobile_number = fake.numerify("##########")
        gender = random.choice(['male', 'female'])
        age = random.randint(18, 25)
        bio = fake.text()

        # print("INserting Mobile_number:", mobile_number)
        Student.objects.create(
            college = college,
            name = name,
            email = email,
            mobile_number = mobile_number,
            gender = gender,
            age = age,
            student_bio = bio,
        )

#fake authors and books generations
def generate_fake_authors(records = 10) -> None:
    for i in range(records):
        author_name = fake.name()
        Author.objects.create(
            author_name = author_name,
        )
    print("Authors generated successfully")

def generate_fake_books(records = 10) -> None:
    authors = Author.objects.all()
    for i in range(records):
        book_name = fake.sentence(nb_words=4)
        book_price = random.randint(100, 2000)
        book_published_date = fake.date_between(start_date='-10y', end_date='today')
        Book.objects.create(
            book_name = book_name,
            author = random.choice(authors),
            price = book_price,
            published_date = book_published_date,
        )
    print("Books generated successfully!")
