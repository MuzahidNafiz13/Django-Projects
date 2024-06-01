from django.shortcuts import render
from datetime import datetime

def index(request):
    context = {
        'blog_list': [
            {'title': 'First Blog', 'content': 'This is my first blog post!', 'date': datetime(2023, 1, 12, 10, 30)},
            {'title': 'Second Blog', 'content': 'Another blog post to read!', 'date': datetime(2022, 12, 12, 10, 30)},
            {'title': 'Third Blog', 'content': 'Yet another interesting post!', 'date': datetime(2023, 1, 12, 10, 30)},
        ],
        'fruits': ["apple", "banana", "cherry"]
    }
    return render(request, 'blog/index.html', context)
