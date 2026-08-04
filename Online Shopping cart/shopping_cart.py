'''
Create a shopping cart.
Products: Laptop,Phone,Mouse,Keyboard,Monitor,Speaker

Prices:
Laptop : 65000
Phone : 25000
Mouse : 800
Keyboard : 1200
Monitor : 9000
Speaker : 2500

Features:
Add multiple products
Prevent invalid products
Quantity should be entered
Calculate subtotal
Discount Rules
Above ₹10,000 → 5%
Above ₹30,000 → 10%
Above ₹60,000 → 15%

Generate invoice
Item
Quantity
Price
Total
Subtotal
Discount
Final Amount
'''
# Product details

products_data={
    "laptop":{
        "price":65000,
        "quantity":5,
    },
    "phone":{
        "price":25000,
        "quantity":3,
    },
    "mouse":{
        "price":800,
        "quantity":4,
    },
    "keyboard":{
        "price":1200,
        "quantity":8,
    },
    "monitor":{
        "price":9000,
        "quantity":2,
    },
    "speaker":{
        "price":2500,
        "quantity":7,
    },
    "headphone":{
        "price":1500,
        "quantity":9,
    },
    "pendrive":{
        "price":2500,
        "quantity":4,
    },

}
# discount data {amount:percentage}
discount_data={
    10000:5,
    30000:10,
    60000:15
}

print("*"*50)
print("**********Welcome to Royal Electronics Market************")

# cart stores all the item purchased by customer
cart={}
# main loop
while True:
    print("1.Shpop\n2.Check Offers\n3.Exit")
    choice= int(input("Enter your choice: "))  # choice for menu
    # -------------------shop-----------------------------
    if choice == 1:
        while True:
            product_name= input("Product Name: ").lower().strip()
            if product_name not in products_data:
                print(f"{product_name} in not available in our supermarket")
                continue

            if product_name in products_data:
                # show the product price and stocks available 
                print(f"Price of {product_name} : ₹{products_data[product_name]['price']}\nAvilable Stocks: {products_data[product_name]['quantity']}")
                print("")

                quantity= int(input("Quantity: "))
                print(f"{product_name} price: {products_data[product_name]['price']}")
                print(" ")


                # cheking the quantity should be greater than 0 show message
                if quantity<=0:
                    print("Quantity should be greater than 0")
                    continue

                # checking if the quantity is greater than 0 and it should be less than equal to stock available 
                if quantity <= products_data[product_name]['quantity']:
                    print(" ")

                    print(f"{quantity} {product_name} is added to the cart succesfully")

                    # reduce the stock in product data
                    products_data[product_name]['quantity']-=quantity
                    print(" ")

                    # add item to the cart
                    if product_name in cart:
                        cart[product_name]["quantity"]+=quantity
                    else:
                        cart[product_name]={
                            "quantity":quantity,
                            "price":products_data[product_name]['price'],
                        }
                    # just for reference item added to the cart
                    print(cart)

                    # continue shopping
                    answer= input("\nDo  you want to continue shopping?(Y/N):  ").strip().lower()
                    if answer== "y":
                        continue

                    print('=============Kindly Check Your cart  before Payment ===================')
                    subtotal=0
                    total=0
                    for product,details in cart.items():
                        quantity= details["quantity"]
                        price=details['price']
                        item_total= quantity*price
                        subtotal+=item_total

                    print(" ")
                    print("****Customer We Special Discount Running in Our Super market****")

                    discount_percentage=0
                    print("*"*50)

                    print(f"Amount    Discount")
                    print("="*20)
                    for amount,discount in discount_data.items():
                        print(f"₹{amount}    {discount}%")
                        if subtotal >= amount:
                                discount_percentage = discount 

                    # after applying discount amount
                    discount_amount= subtotal* ( discount_percentage/100)
                    print("="*20)
                    print(f"{discount_percentage}% is applied on your subtotal {subtotal} & discount amount ₹{discount_amount}")
                    print(" ")

                    # final amount
                    total=subtotal-discount_amount


                    # final invoice
                    print("\n")
                    print("=" * 65)
                    print("                    FINAL INVOICE")
                    print("=" * 65)
                    print(f"{'Item':<15}{'Quantity':<10}{'Price':<15}{'Total':<15}")
                    for item,details in cart.items():
                        quantity= details["quantity"]
                        price=details['price']
                        item_total= quantity*price
                        print(
                            f"{item.capitalize():<15}"
                            f"{quantity:<10}"
                            f"₹{price:<14}"
                            f"₹{item_total:<15}"
                        )
                    print("-" * 65)   
                    print(f"Subtotal: ₹{subtotal}")
                    print(f"Discount {discount_percentage}% Discount Amount ₹{discount_amount}")
                    print("-"*65)
                    print(f"Final Amount: ₹{total}")

                    print("If the invoice is correct click Yes to do payment and to generate the bill")
                    print(" ")


                    confirm=input("Enter Y/N/Exit:  ").strip().lower()
                    # if confirm to exit and collect invoice
                    if confirm =="y":
                        print("************Thanks for shopping in Royal Electronics Market 😀,Collect the invoice****************")
                        cart.clear()
                        break
                    # if confirm is no empty cart, start shopping from again
                    elif confirm == "n":
                        print(f"We emptyed your cart, Add items to cart")
                        cart.clear()
                        continue
                    # exit from the cart
                    elif confirm == "exit":
                        print("************Thanks for Visiting Royal Electronics Market 😀 **********")
                        break
                # product is not available in super market
                else:
                    print(f"Sorry, {products_data[product_name]['quantity']} {product_name} is available in the stock")
                    continue
        
    #------------------Offers----------------------
    elif choice ==2:
        print("="*20)
        print(f"Amount    Discount")
        for amount,discount in discount_data.items():
            print(f"₹{amount}    {discount}%")
        print("="*20)
        continue

    elif choice==3:
        print("Thanks for visiting Royal Electronics Market 🥰")
        break

    else:
        print("Enter the correct choice.. Try Again!!")
        continue

