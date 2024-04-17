#Today i am going to create the restuarent software design how to handle food methods
import textwrap
class Menu:
    def __init__(self, name, items, start_time, end_time, season):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time
        self.season = season

    def __repr__(self):
        ls = []
        for lse in self.items.keys():
            ls.append(lse)
        print(ls)
        huu =  """
        Hello {}! 
        it was a nice experience with You
        Could u please see the menu item Timing's Before Ordering the Item 
        {} menu available from {} to {}
        The available {} Items are {}""".strip("/n").format(self.season, self.name, self.start_time, self.end_time, self.name, ', '.join(ls,))
        bh = textwrap.dedent(huu)
        return bh
    def average_cal(self, select_items1):
        sum = 0
        for tem in select_items1:
            if tem in self.items.keys():
                print("the item name ".upper() + tem + ": " + str(self.items[tem]))
                sum += self.items[tem]

        gst = 7.88
        other_taxes = 2.12
        sum1 = gst + other_taxes
        sum += sum1
        print("Other taxes: ".upper() + str(sum1))
        print("Total bill for your Order".upper() + ": " + str(sum))


break_fast = {"dosa": 40, "idli": 30, "Bacon and eggs": 60, "Oatmeal": 50, "Fruit salad": 65, "Yogurt parfait": 78}
dinner = {"Grilled salmon with roasted vegetables": 300, "Biryani": 350, "Hyderabad biryani": 400,
          "Chicken stir-fry with rice": 589, "Beef stew with mashed potatoes": 555,
          "Margherita pizza with a side salad": 856}
lunch = {"Turkey sandwich with avocado and lettuce": 352, "Caesar salad with grilled chicken": 825,
         "Veggie wrap with hummus and assorted vegetables": 789, "Quinoa salad with black beans and feta cheese": 1253,
         "Sushi rolls with miso soup": 456, "Grilled cheese sandwich with tomato soup": 258}
cool_drinks = {"thumsup": 220, "Maaza": 56, "Watermelon Wonder Cooler": 125, "Tropical Sunrise Cooler": 358,
               "Iced Vanilla Latte": 256, "Berry Bliss Smoothie": 256}
all_stuff = {"dosa": 40, "idli": 30, "Bacon and eggs": 60, "Oatmeal": 50, "Fruit salad": 65, "Yogurt parfait": 78, "Grilled salmon with roasted vegetables": 300, "Biryani": 350, "Hyderabad biryani": 400,
          "Chicken stir-fry with rice": 589, "Beef stew with mashed potatoes": 555,
          "Margherita pizza with a side salad": 856, "Turkey sandwich with avocado and lettuce": 352, "Caesar salad with grilled chicken": 825,
         "Veggie wrap with hummus and assorted vegetables": 789, "Quinoa salad with black beans and feta cheese": 1253,
         "Sushi rolls with miso soup": 456, "Grilled cheese sandwich with tomato soup": 258, "thumsup": 220, "Maaza": 56, "Watermelon Wonder Cooler": 125, "Tropical Sunrise Cooler": 358,
               "Iced Vanilla Latte": 256, "Berry Bliss Smoothie": 256}
break_menu = Menu("break_fast", break_fast, "8:00AM", "11:30AM", "Good Morning")
dinner_menu = Menu("dinner", dinner, "12:00PM", "16:00PM", "Good Afternoon")
lunch_menu = Menu("lunch", lunch, "19:00PM", "22:00PM", "Good Evening")
cool_menu = Menu("cool_drinks", cool_drinks, "8:00AM", "24:00AM", "Everyone")
all_menu = Menu("all_items", all_stuff, "8:00AM", "24:00AM", "Everyone")
print("Welcome to Bharathmulti Food Restaurant".upper())
new_list = [break_menu, dinner_menu, lunch_menu, cool_menu, all_menu]
h = int(input("enter the number: "))
ol = new_list[h]
print(ol)
item_list = []
slots = [break_fast, dinner, lunch, cool_drinks]
for i in range(1):
    lse = []
    for slot in slots:
        for ls in slot.keys():
            lse.append(ls)
    #print(lse)
    n = int(input("The number of items has been selectedclas:"))
    select_item = []
    while n > 0:
        #print(b)
        lg = input("Enter the item name: ")
        #print(lg)
        selected_item = [ls for ls in lse if ls.startswith(lg)]
        for ls in selected_item:
            select_item.append(ls)
        n -= 1
    print(textwrap.dedent(" Your order has been selected. Please wait a moment."))
    hot_list = [break_menu, dinner_menu, lunch_menu, cool_menu, all_menu]
    l = int(input("enter the number: "))
    new = hot_list[l]
    if new == break_menu:
        break_menu.average_cal(select_item)
        break
    elif new == dinner_menu:
        dinner_menu.average_cal(select_item)
        break
    elif new == lunch_menu:
        lunch_menu.average_cal(select_item)
        break
    elif new == cool_menu:
        cool_menu.average_cal(select_item)
        break
    elif new == all_menu:
        all_menu.average_cal(select_item)
        break
    else:
        print("Sorry sir, Menu is closed Now.")


print(textwrap.dedent("Thank You! Have a Nice Day!"))
print(textwrap.dedent("Enjoy Yourself! 😄❤️"))








