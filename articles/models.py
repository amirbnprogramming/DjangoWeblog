from django.db import models
from abc import abstractmethod
from django.contrib.auth import get_user_model
from jalali_date import date2jalali

User = get_user_model()


class BaseModel(models.Model):
    title = models.CharField(max_length=250, verbose_name='title')
    url_title = models.CharField(max_length=250, verbose_name='url_title')
    is_active = models.BooleanField(default=True, verbose_name='is_active')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='created_at')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='updated_at')

    class Meta:
        abstract = True

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def get_full_fields(self):
        pass

    @classmethod
    def get_active_objects(cls):
        return cls.objects.filter(is_active=True).all()

    @classmethod
    def get_all_objects(cls):
        return cls.objects.all()


class Category(BaseModel):
    parent = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='parent_category', null=True,
                               blank=True, related_name='category_parent')

    def __str__(self):
        return self.title

    def get_full_fields(self):
        return f'{self.title} - {self.parent}'

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class Article(BaseModel):
    author = models.ForeignKey(User, on_delete=models.CASCADE, max_length=250, verbose_name='author',
                               related_name='article_author')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='category', related_name='article_category')
    short_description = models.CharField(max_length=500, verbose_name='short_description')
    description = models.TextField(verbose_name='description')

    def get_jalali_create_date(self):
        return date2jalali(self.created_at)

    def get_jalali_create_time(self):
        return self.created_at.strftime('%H:%M')

    def __str__(self):
        return self.title

    def get_full_fields(self):
        return f'{self.title} - {self.author} - {self.category}'

    class Meta:
        verbose_name = 'article'
        verbose_name_plural = 'articles'


class Comment(BaseModel):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='article', related_name='article_comment')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='author')
    text = models.TextField(verbose_name='text')
    title = None
    url_title = None

    def __str__(self):
        return self.text

    def get_full_fields(self):
        return f'{self.article} - {self.author} - {self.text}'

    class Meta:
        verbose_name = 'comment'
        verbose_name_plural = 'comments'
