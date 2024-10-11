from django.shortcuts import render

posts = [{'author': 'CoreyMS', 
         'title': 'Blog Post 1', 
         'content': 'First post content', 
         'date_posted': 'August 27, 2018'},
         {'author': 'Jordan Mason', 
         'title': 'Blog Post 2', 
         'content': '2nd post content', 
         'date_posted': 'Oct 10, 2024'}]

# Create your views here.
def home(request):
    context = {'posts': posts}
    return render(request, 'blog/home.html')

def about(request):
    return render(request, 'blog/about.html')
 
