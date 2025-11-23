import datetime
import random
from orm_practice.models import Author, Category, Post
from faker import Faker
fake = Faker()

def generate_author(records=10):
    for i in range(records):
        Author.objects.create(
            name=fake.name(),
            email=fake.email(),
            bio=fake.text(),
            birth_date=fake.date_between(start_date='-70y', end_date='-20y')
        )
    print("Authors generated successfully!")

def generate_categories(records=10):
    categories = """Technology
        Lifestyle
        Travel
        Food & Recipes
        Health & Fitness
        Fashion & Beauty
        Business & Finance
        Education
        Parenting
        Sports
        Entertainment
        Photography
        DIY & Crafts
        Science & Nature
        Music
        Personal Development
        News & Current Affairs
        Gaming
        Art & Design
        Environment & Sustainability"""
    cat_list = [c.strip() for c in categories.split('\n') if c.strip()]
    present_cateogries = {c.title for c in Category.objects.all()}

    for x in cat_list:
        if x not in present_cateogries:
            Category.objects.create(title=x,
                                    description=fake.sentence(nb_words=10))

    print("Categories generated successfully!")


def generate_posts(records=10):
    authors = Author.objects.all()
    categories = list(Category.objects.all())

    for i in range(records):
        author_choice = random.choice(authors)
        start_date = author_choice.birth_date + datetime.timedelta(days=365*20)
        if start_date > datetime.date.today():
            pub_date = datetime.datetime.now()
        else:
            pub_date = fake.date_time_between(start_date=start_date, end_date='now')

        post = Post.objects.create(
            title=fake.sentence(nb_words=6),
            content=fake.text(max_nb_chars=2000),
            published_date=pub_date,
            author=author_choice,
            views=random.randint(0, 10000)
        )
        # Assign 1-3 random categories to the post
        selected_categories = random.sample(categories, k=random.randint(1, 3))
        post.categories.add(*selected_categories)
    print("posts created successfully!")



