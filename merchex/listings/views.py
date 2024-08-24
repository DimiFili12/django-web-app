from django.shortcuts import render
from listings.models import Band, Listing
from listings.forms import BandForm, ContactUsForm, ListingForm
from django.core.mail import send_mail
from django.shortcuts import redirect

def band_list(request):
    bands = Band.objects.all()
    return render(request, 
                  'listings/band_list.html',
                  {'bands': bands})

def band_details(request, id):
    band = Band.objects.get(id=id)
    return render(request,
                  'listings/band_details.html',
                  {'band': band})

def band_create(request):
    if request.method == 'POST':
        form = BandForm(request.POST)
        if form.is_valid():
            band = form.save()
            return redirect('band-detail', band.id)
    else:
        form = BandForm()
    return render(request,
                'listings/band_create.html',
                {'form': form})
    
def band_update(request, id):
    band = Band.objects.get(id=id)
    if request.method == 'POST':
        form = BandForm(request.POST, instance=band)
        if form.is_valid():
            form.save()
            return redirect('band-detail', band.id)
    else:
        form = BandForm(instance=band)
    return render(request,
                'listings/band_update.html',
                {'form': form})

def band_delete(request, id):
    band = Band.objects.get(id=id)
    if request.method == 'POST':
        band.delete()
        return redirect('band_list')
    return render(request,
                    'listings/band_delete.html',
                    {'band': band})

def about(request):
    return render(request, 'listings/about.html')

def contact(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            send_mail(
                subject=f'Message from {form.cleaned_data["name"] or "anonymous"} via MerchEx Contact Us form',
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['admin@merchex.xyz'],
            )
            return redirect('email-sent')
    else:
        form = ContactUsForm()
    return render(request,
                'listings/contact.html',
                {'form': form})

def listing_list(request):
    listings = Listing.objects.all()
    return render(request, 'listings/listing_list.html', {'listings': listings})

def listing_details(request, id):
    listing = Listing.objects.get(id=id)
    return render(request, 'listings/listing_details.html', {'listing': listing})

def listing_create(request):
    if request.method == 'POST':
        form = ListingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listing-list')
    else:
        form = ListingForm()
    return render(request, 
                  'listings/listing_create.html', 
                  {'form': form})

def listing_update(request, id):
    listing = Listing.objects.get(id=id)
    if request.method == 'POST':
        form = ListingForm(request.POST, instance=listing)
        if form.is_valid():
            form.save()
            return redirect('listing-detail', id=listing.id)
    else:
        form = ListingForm(instance=listing)
    return render(request, 'listings/listing_update.html', {'form': form, 'listing': listing})

def listing_delete(request, id):
    listing = Listing.objects.get(id=id)
    if request.method == 'POST':
        listing.delete()
        return redirect('listing-list')
    return render(request, 'listings/listing_delete.html', {'listing': listing})

def sample(request):
    return render(request, 'listings/sample.html')

def email_sent(request):
    return render(request, 'listings/email_sent.html')