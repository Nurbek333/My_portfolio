from django.shortcuts import render, get_object_or_404, redirect,HttpResponseRedirect
from .models import AboutSection, Project, ProjectCategory,PortfolioItem, Post, Comment,Contact
from .forms import CommentForm
from hitcount.utils import get_hitcount_model
from hitcount.views import HitCountMixin
from .bot import send_message
from django.urls import reverse
from django.views import View
from django.core.paginator import Paginator
# Create your views here.
def index(request):
    portfolio_items = PortfolioItem.objects.all()
    about_section = AboutSection.objects.first()
    return render(request,"index.html", {'portfolio_items': portfolio_items, 'about_section': about_section})


def about_us(request):
    # Ma'lumotlarni modeldan olish
    about_section = AboutSection.objects.first()  # Birinchi yozuvni olish

    # Ma'lumotlarni shablonga yuborish
    context = {
        'about_section': about_section
    }
    return render(request,"about-us.html", context)



def blog(request):
    posts_list = Post.objects.all()  # Barcha postlarni olish
    paginator = Paginator(posts_list, 2)  # Har bir sahifada 2 post

    page_number = request.GET.get('page')  # URL dan sahifa raqamini olish
    page_obj = paginator.get_page(page_number)  # Sahifa obyektini olish
    
    return render(request, "blog.html", {'page_obj': page_obj})

class ContactView(View):
    template_name = "contact.html"
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
    def post(self, request, *args, **kwargs): 
        name = request.POST.get('first_name', '')
        email = request.POST.get('email', '')
        message = request.POST.get('description', '')
        contact = Contact(first_name=name,email=email,description=message)
        contact.save()
        
        send_message(f"Ism: {name}\nEmail: {email}\nText:{message}")

        return HttpResponseRedirect(reverse('index-page')) 


def portfolio_detail(request, pk):
    item = get_object_or_404(PortfolioItem, pk=pk)
    return render(request,"portfolio-details.html", {'item': item})



def portfolio(request):
    portfolio_items = PortfolioItem.objects.all()
    return render(request,"portfolio.html", {'portfolio_items': portfolio_items})



def single_blog(request, slug):
    post = get_object_or_404(Post, slug=slug)
    
    hit_count = get_hitcount_model().objects.get_for_object(post)
    hit_count_response = HitCountMixin.hit_count(request, hit_count)
    
    # Agar bu sahifa avval ko'rilmagan bo'lsa, ko'rishlar sonini oshiring
    if hit_count_response.hit_counted:
        post.views += 1
        post.save()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            # Extract form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            
            # Create a Comment object with the correct fields
            Comment.objects.create(
                post=post,
                name=name,
                email=email,
                subject=subject,
                message=message
            )
            
            # Redirect or render a response after successful form submission
            return redirect('post_detail', slug=slug)
    else:
        form = CommentForm()
    
    return render(request, 'single-blog.html', {'form': form, 'post': post})

 