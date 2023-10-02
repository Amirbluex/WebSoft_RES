from django.db import models
from account.models import User
from django.utils.html import format_html
from django.utils.text import slugify
from django.urls import reverse


class Category(models.Model):
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE, related_name='subs', verbose_name='والد')
    title = models.CharField(max_length=100, verbose_name="عنوان")
    slug = models.SlugField(blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="ساخته شده در")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="articles", verbose_name="نویسنده")
    category = models.ManyToManyField(Category, related_name="articles", verbose_name="دسته بندی")
    title = models.CharField(max_length=70, verbose_name="عنوان")
    body = models.TextField(verbose_name="متن بدنه")
    image = models.ImageField(upload_to='images/articles', blank=True, null=True, verbose_name="تصویر")
    created = models.DateTimeField(auto_now_add=True, verbose_name="ساخته شده در")
    updated = models.DateTimeField(auto_now=True, verbose_name="آپدیت")
    published = models.BooleanField(default=True, verbose_name="انتشار")
    slug = models.SlugField(blank=True, unique=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = "مقاله"
        verbose_name_plural = "مقالات"

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.title)
        super(Article, self).save()

    def get_absolute_url(self):
        return reverse('blog:article_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return f"{self.title} - {self.body[:30]}"

    def show_img(self):
        if self.image:
            return format_html(f'<img src="{self.image.url}" width="50px" height="50px">')
        return format_html('<h3 style="color: blue" >تصویر ندارد</h3>')
    show_img.short_description = "تصویر"
