
from state_machine import (State, Event, acts_as_state_machine,
after, before, InvalidStateTransition)

username = ""
cart = []
credit_score = 0
cost = 0
i = 0

@acts_as_state_machine
class CheckoutProcess:

    #define the states
    browsing = State(initial=True)
    cart = State()
    checkout = State()
    payment = State()
    verification = State()
    pending = State()
    confirmed = State()
    shipped = State()
    delivered = State()
    cancelled = State()
    rejected = State()

    #define transitions
    add_to_cart = Event(from_states=(browsing, cart), to_state=cart)
    go_checkout = Event(from_states=(cart), to_state=checkout)
    add_payment = Event(from_states=(checkout), to_state=payment)
    verify_payment = Event(from_states=(payment), to_state=verification)
    order_pending = Event(from_states=(verification), to_state=pending)
    order_confirmed = Event(from_states=(pending), to_state=confirmed)
    order_shipped = Event(from_states=(confirmed), to_state=shipped)
    order_delivered = Event(from_states=(shipped), to_state=delivered)
    order_cancelled = Event(from_states=(browsing, cart, checkout, payment, verification, pending, confirmed, shipped, delivered), to_state=cancelled)
    order_rejected = Event(from_states=(browsing, cart, checkout, payment, verification, pending, confirmed, shipped, delivered, cancelled), to_state=rejected)
    
    @before('add_to_cart')
    def add_to_cart_prior(self):
        global cart
        global cost
        item = input("Enter the item you want to add to the cart: ")
        cart.append(item)
        price = float(input("Enter the price of the item: "))
        cost += price
        return True
    
    @before('go_checkout')
    def go_checkout_prior(self):
        confirm = input("Are you sure you want to proceed to checkout? (y/n): ")
        return True if confirm.lower() == 'y' else False
    
    @before('add_payment')
    def add_payment_prior(self):
        global credit_score
        global username
        confirm = input("Are you sure you want to enter payment info? (y/n): ")
        if confirm.lower() == 'y':
            username = input("Enter your name: ")
            credit_score = int(input("Enter your credit score (0-800): "))
            if credit_score < 0 or credit_score > 800:
                print("Invalid credit score!")
                return False
        else:
            return False
        
    @before('verify_payment')
    def verify_payment_prior(self):
        global username
        global credit_score
        global cart
        global cost
        print("Verifying payment info...")
        print()
        print(f"User ID: {username}")
        print(f"Credit score: {credit_score}")
        print(f"Items in cart: {cart}")
        print(f"Total cost: ${cost:.2f}")
        print()
        confirm = input("Are you sure all your payment info is correct? (y/n): ")
        return True if confirm.lower() == 'y' else False
    

    @after('add_to_cart')
    def add_to_cart_info(self):
        global i
        global cost
        print(f"Item '{cart[i]}' added to cart!")
        i += 1
        print(f"Current total cost: ${cost:.2f}")
        print()
        print("Current Stage: Cart")
        print("Please proceed to checkout when you are done adding!")
    
    @after('go_checkout')
    def go_checkout_info(self):
        global cart
        global cost
        print("Proceeding to checkout!")
        print(f"Items in cart: {cart}")
        print(f"Total cost: ${cost:.2f}")
        print()
        print("Current Stage: Checkout")
        print("Please enter payment info!")
       
    
    @after('add_payment')
    def add_payment_info(self):
        print("Payment info entered!")
        print()
        print("Current Stage: Payment")
        print("Please verify your order info!")
    
    @after('verify_payment')
    def verify_payment_info(self):
        if (credit_score > 0 and credit_score <= 400 and cost > 500) or (credit_score > 400 and credit_score <= 600 and cost > 2000):
            print("Order rejected! Credit score is too low for this purchase.")
            self.order_rejected()
            return False
        else:
            print("Order verified!")
            print()
            print("Current Stage: Verification")
            print("Please submit the order for approval next!")
            
    @after('order_pending')
    def order_pending_info(self):
        print("Order is pending!")
        print()
        print("Current Stage: Pending")
        print("Please wait for order to be confirmed!")
        
    @after('order_confirmed')
    def order_confirmed_info(self):
        print("Order is confirmed!")
        print()
        print(f"Items in cart: {cart}")
        print(f"Total cost: ${cost:.2f}")
        print("Current Stage: Confirmed")
        print("Please wait for order to be shipped!")

    @after('order_shipped')
    def order_shipped_info(self):
        print("Order is shipped!")
        print()
        print("Current Stage: Shipped")
        print("Please wait for order to be delivered!")
    
    @after('order_delivered')
    def order_delivered_info(self):
        print("Order is delivered!")
        print()
        print("Current Stage: Delivered")
        exit(0)

    @after('order_rejected')
    def order_rejected_info(self):
        print("Order is rejected!")
        exit(0)
    
    @after('order_cancelled')
    def order_cancelled_info(self):
        print("Order is cancelled!")
        print()
        print("Current Stage: Cancelled")
        exit(0)
    
class OnlineStoreApplication:
    def __init__(self) -> None:
        self.state = CheckoutProcess()

    def add_to_cart(self):
        self.state.add_to_cart()
    def go_checkout(self):
        self.state.go_checkout()
    def add_payment(self):
        self.state.add_payment()
    def verify_payment(self):
        self.state.verify_payment()
    def order_pending(self):
        self.state.order_pending()
    def order_confirmed(self):
        self.state.order_confirmed()
    def order_shipped(self):
        self.state.order_shipped()
    def order_delivered(self):
        self.state.order_delivered()
    def order_cancelled(self):
        self.state.order_cancelled()
    def order_rejected(self):
        self.state.order_rejected()

def menu():
    print()
    print("1. Add Item to Cart")
    print("2. Proceed to Checkout")
    print("3. Enter Payment Info")
    print("4. Verify Order")
    print("5. Approve Order")
    print("6. Reject Order")
    print("7. Confirm Order")
    print("8. Ship Order")
    print("9. Deliver Order")
    print("10. Cancel Order")
    print()

def main():
    switch = OnlineStoreApplication()
    while True:
        menu()
        choice = int(input("Select an action: "))
        try:
            if choice == 1:
                switch.add_to_cart()
            elif choice == 2:
                switch.go_checkout()
            elif choice == 3:
                switch.add_payment()
            elif choice == 4:
                switch.verify_payment()
            elif choice == 5:
                switch.order_pending()
            elif choice == 6:
                switch.order_rejected()
            elif choice == 7:
                switch.order_confirmed()
            elif choice == 8:
                switch.order_shipped()
            elif choice == 9:
                switch.order_delivered()    
            elif choice == 10:
                switch.order_cancelled()
                print("Exiting the application...")
                break            
            else:
                print("Invalid choice!")
                continue
        except InvalidStateTransition as err:
            print(f"Could not perform {choice} in {switch.state.current_state}!")

if __name__ == "__main__":
    main()

