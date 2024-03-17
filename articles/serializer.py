from rest_framework import serializers

from articles.models import User, Article, Category, Comment


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'is_active', 'is_superuser']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    # related names :
    category = CategorySerializer(read_only=True)
    author = UserSerializer(read_only=True)
    article_comment = CommentSerializer(read_only=True, many=True)

    class Meta:
        model = Article
        fields = '__all__'
