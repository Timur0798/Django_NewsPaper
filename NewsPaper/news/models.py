from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum

# Create your models here.
class Author(models.Model):
    authorUser=models.OneToOneField(User,on_delete=models.CASCADE)
    authorRating=models.IntegerField(default=0)
    def update_rating(self):
        sumRating = self.post_set.aggregate(postRating=Sum('newsRating'))
        pRat = 0
        pRat += sumRating.get('postRating')

        commentRat = self.authorUser.comment_set.aggregate(commentRating=Sum('rating'))
        cRat = 0
        cRat = commentRat.get('commentRating')

        self.authorRating = pRat*3 + cRat
        self.save()


class Category(models.Model):
    name = models.CharField(max_length=64,unique=True)


class Post(models.Model):
    author = models.ForeignKey(Author,on_delete=models.CASCADE)

    Article = 'AR'
    News = 'NW'
    CATEGORY_CHOICES = (
        (Article, 'Статья'),
        (News, 'Новость')
    )
    categoryType = models.CharField(max_length=2,choices=CATEGORY_CHOICES,default=Article)
    creationTime = models.DateTimeField(auto_now_add=True)
    newsCategory = models.ManyToManyField(Category,through='PostCategory')
    title = models.CharField(max_length=128)
    text = models.TextField()
    newsRating = models.IntegerField(default=0)

    def like(self):
        self.newsRating += 1
        self.save()

    def dislike(self):
        self.newsRating -= 1
        self.save()

    def preview(self):
        return self.text[0:123] + '...'

    def __str__(self):
        return f'{self.author.authorUser}: {self.title}: {self.creationTime}'


class PostCategory(models.Model):
    postThrough = models.ForeignKey(Post,on_delete=models.CASCADE)
    categoryThrough = models.ForeignKey(Category,on_delete=models.CASCADE)


class Comment(models.Model):
    commentPost = models.ForeignKey(Post,on_delete=models.CASCADE)
    commentUser = models.ForeignKey(User,on_delete=models.CASCADE)
    commentCreation = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()