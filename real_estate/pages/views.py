from django.shortcuts import get_object_or_404, render

# Create your views here.
from .models import *

def home_view(request):
    items = Listing.objects.all()

    bedroom_choices = {
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '10': 10,
      }

    price_choices = {
        '100000': '$100,000',
        '200000': '$200,000',
        '300000': '$300,000',
        '400000': '$400,000',
        '500000': '$500,000',
        '600000': '$600,000',
        '700000': '$700,000',
        '800000': '$800,000',
        '900000': '$900,000',
        '1000000': '$1M+',
    }

    state_choices = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming',
    }

    context = {
        'items': items,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'state_choices': state_choices
    }

    return render(request, 'home.html', context)


def about_view(request):
    return render(request, 'about.html')


def listing_view(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)

    context = {
        'listing': listing
    }

    return render(request, 'listing.html', context)


def listings_view(request):
    items = Listing.objects.all()

    context = {
        'items': items
    }

    return render(request, 'listings.html', context)


def search_view(request):
    queryset_list = Listing.objects.order_by('-list_date')

    bedroom_choices = {
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '10': 10,
      }

    price_choices = {
        '100000': '$100,000',
        '200000': '$200,000',
        '300000': '$300,000',
        '400000': '$400,000',
        '500000': '$500,000',
        '600000': '$600,000',
        '700000': '$700,000',
        '800000': '$800,000',
        '900000': '$900,000',
        '1000000': '$1M+',
    }

    state_choices = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming',
    }

    # Description
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']

        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)

    # City
    if 'city' in request.GET:
        city = request.GET['city']

        if city:
            queryset_list = queryset_list.filter(city__icontains=city)

    # State
    if 'state' in request.GET:
        state = request.GET['state']

        if state:
            queryset_list = queryset_list.filter(state__icontains=state)

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
        'items': queryset_list,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'state_choices': state_choices,
        'values': request.GET
    }

    return render(request, 'search.html', context)
