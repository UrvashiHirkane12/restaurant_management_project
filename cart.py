class Cart:
    def  __init__(self, request):
        self.session = request.session
        cart = self.session.get("cart")
        if not cart:
            cart= self.session["cart"]={}
        self.cart =  cart

    def add(self, item_id, quantity=1):
        item_id =  str(item_id)
        self.cart[item_id]= self.cart.get(item_id, 0) + quantity
        self.save()

    def __len__(self):
        """return tottal items in cart:"""
        return sum(self.cart.values())      