## 3. Find all posts published in the last 30 days.
> from django.utils import timezone 
> import datetime 
> from django.db.models import Q 
> thirty_days_ago = timezone.now() - datetime.timedelta(days=30)
> posts = Post.objects.filter(published_date__gte=thirty_days_ago)

## 4. Find all categories that currently have no posts assigned to them.
>  Category.objects.annotate(num_posts = Count('posts')).filter(num_posts = 0)
> Category.objects.annotate(num_posts=Count('posts')).order_by('-num_posts')

## 6. Retrieve all authors who have never published a post.
> Author.objects.annotate(num_posts=Count('posts')).filter(num_posts=0)

## 7. Update the bio of all authors who have more than 10 posts to "Prolific author".
> ##### This is fast as this query fires a single update query
> authors_to_update = Author.objects.annotate(num_posts=Count('posts')).filter(num_posts__gt=10)
> authors_to_update.update(bio="Prolific Author")
> ##### This is slower as this query fires query for all authors that are eligible
> for author in Author.objects.annotate(num_posts = Count('posts')).filter(num_posts__gt = 10):
>   author.bio = "Prolific Author"
>   author.save()

## 8. Retrieve the top 3 authors with the highest average post views.
> from django.db.models import Avg
> top_authors = Author.objects.annotate(avg_views=Avg('posts__views')).order_by('-avg_views')[:3]





