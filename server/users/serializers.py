from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

from reviews.models import Review
from users.models import User
from books.models import Book
from track.models import Track


class UserLoginSerializer(TokenObtainPairSerializer):
    username = serializers.CharField()
    password = serializers.CharField()

    class Meta:
        fields = ['username', 'password']

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return {
                'username': user.username,
                'profile_pic': user.profile_pic.url if user.profile_pic else None,
                'access': str(RefreshToken.for_user(user).access_token),
                'refresh': str(RefreshToken.for_user(user))
            }
        raise serializers.ValidationError({
            'code': 'authorization_failed',
            'message': 'Invalid credentials'
        })


class UserRegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    email = serializers.EmailField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    profile_pic = serializers.ImageField(required=False)

    class Meta:
        fields = ['username', 'password', 'email', 'first_name', 'last_name', 'profile_pic']
        write_only_fields = ['password']

    def validate(self, attrs):
        if User.objects.filter(email=attrs['email']).exists():
            raise serializers.ValidationError({"code": "email_exists", "message": "Email already exists", "field": "email"})
        if User.objects.filter(username=attrs['username']).exists():
            raise serializers.ValidationError({"code": "username_exists", "message": "Username already exists", "field": "username"})
        try:
            validate_password(attrs['password'])
        except Exception as e:
            raise serializers.ValidationError({"code": "invalid_password", "message": str(e)})

        return attrs

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )
        if 'profile_pic' in validated_data:
            user.profile_pic = validated_data['profile_pic']

        user.set_password(validated_data['password'])
        user.save()
        return user


class UserSerializer(serializers.ModelSerializer):
    total_reviews = serializers.SerializerMethodField()
    book_status_count = serializers.SerializerMethodField()

    class Meta:
        model = User
        exclude = ['password', 'is_superuser', 'is_staff', 'is_active', 'groups', 'user_permissions', 'last_login',
                   'date_joined']
        read_only_fields = ['id', 'total_reviews', 'book_status_count', 'username']

    def get_total_reviews(self, obj):
        return Review.objects.filter(user=obj).count()

    def get_book_status_count(self, obj):
        out = {
            "completed": Track.objects.filter(user=obj, status="completed").count(),
            "reading": Track.objects.filter(user=obj, status="reading").count(),
            "planning": Track.objects.filter(user=obj, status="planning").count(),
            "dropped": Track.objects.filter(user=obj, status="dropped").count(),
            "paused": Track.objects.filter(user=obj, status="paused").count(),
        }

        total = out['completed'] + out['reading'] + out['planning'] + out['dropped'] + out['paused']
        out['total'] = total
        return out


class UserUnAuthSerializer(UserSerializer):
    class Meta:
        model = User
        exclude = ['password', 'is_superuser', 'is_staff', 'is_active', 'groups', 'user_permissions', 'last_login',
                   'date_joined', 'email']


