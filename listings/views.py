from django.shortcuts import render, get_object_or_404, redirect ,HttpResponseRedirect
from . models import Listing
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import price_choices, bedroom_choices, state_choices
from .forms import add_listing
from owner.models import Owner


def index(request):
    
    listings = Listing.objects.order_by('-list_date')
    
    paginator = Paginator(listings, 3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)


    context = {
        'listings':paged_listings
    }

    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    context = {
        'listing' : listing
    }

    return render(request, 'listings/listing.html', context)




def search(request):
    queryset_list = Listing.objects.order_by('-list_date')

    # keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords'] 
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)

    # City
    if 'city' in request.GET:
        city = request.GET['city'] 
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)
    
    # State
    if 'state' in request.GET:
        state = request.GET['state'] 
        if state:
            queryset_list = queryset_list.filter(state__iexact=state)
    
    # Bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms'] 
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)

    # Price
    if 'price' in request.GET:
        price = request.GET['price'] 
        if price:
            queryset_list = queryset_list.filter(price__lte=price)

    context = {
        'bedroom_choices' : bedroom_choices,
        'state_choices' : state_choices,
        'price_choices' : price_choices,
        'listings': queryset_list,
        'values': request.GET,
        }

    return render(request, 'listings/search.html', context)


def addlisting(request):
    if request.method == 'POST':
        
        listing_form = add_listing(request.POST or None,  request.FILES or None )
        

        if listing_form .is_valid():
            
            instance = listing_form.save(commit=False)
            user = request.user
            user1 = str(user)
            print("type user1 = ",type(user1))
            print("type user1 = ",user1)
            own=[]
        
            
            objs = Owner.objects.all()
            print(objs)
            for obj in objs:
                temp = str(obj)
                if user1 == temp:
                    own.append(obj)
                    break
           # print("ans",type(own))
            print("ans",(own))
            #for i in own:
            new=own[0]
            instance.owner = new
            print("new type",type(new))
            instance.save()
            
            return redirect('listings')
    
        
            
    else:
        listing_form = add_listing()
    return render(request, 'listings/listing_form.html', {'listing_form': listing_form})
    
   