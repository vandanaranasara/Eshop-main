from django.shortcuts import render, redirect
from store.models.category import Category
from store.models.product import Products
from store.models.customer import Customer

def add_product(request):
    user_id = request.session.get('customer')
    user_type = request.session.get('user_type')

    if user_type != 'seller':
        return redirect('homepage')

    categories = Category.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        category_id = request.POST.get('category')
        description = request.POST.get('description')
        image = request.FILES.get('image')

        # Get seller instance
        seller = Customer.objects.get(id=user_id)

        # Create and save product
        product = Products(
            name=name,
            price=price,
            category_id=category_id,
            description=description,
            image=image,
            seller=seller
        )
        product.save()
        return redirect('store')

    return render(request, 'add_product.html', {'categories': categories})
