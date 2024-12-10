
def calculate_discount(total_amount, num_items, day_of_week):

    if day_of_week.lower() in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']:
        total_amount *= 90/100  # 10% discount
   
    elif day_of_week.lower() in ['saturday', 'sunday']:
        total_amount *= 80/100  # 20% discount

    if num_items > 5:
        total_amount *= 95/100  # 5% discount

    return total_amount


def verify_week_day():
    daysOfTheWeek = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    while True:
        day_of_week = input("Day of the week: ").strip()
        if day_of_week.lower() in daysOfTheWeek:
            return day_of_week
        else:
            print("Please enter a correct day of the week.")


total_amount = float(input("Total amount: "))
num_items = int(input("Number of items: "))
day_of_week = verify_week_day()

total_price_after_discount = calculate_discount(total_amount, num_items, day_of_week)
print(f"Total price after discount: {total_price_after_discount:.1f} dinars")


