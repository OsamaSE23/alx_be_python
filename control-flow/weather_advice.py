ask_user = input("What's the weather like today? (sunny/rainy/cold): ")

if ask_user == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif ask_user == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif ask_user == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")
