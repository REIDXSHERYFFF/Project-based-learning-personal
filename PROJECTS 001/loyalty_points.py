# ☕️ Loyalty Points Engine Challenge
#
# RULES:
# • Each whole dollar spent earns 3 points
# • Tiers:
#     < 100 pts   →  Bronze
#     100-499 pts → Silver
#     ≥ 500 pts   →  Gold
#
# STEPS:
# 1. Define earn_points(price) → returns points for one purchase
# 2. Define tier_label(points) → returns "Bronze" / "Silver" / "Gold"
# 3. Given the hard-coded list `purchases`,
#    loop through it, call earn_points() for each amount,
#    and add the result to total_points.
# 4. After the loop, call tier_label(total_points)
# 5. Print 'Loyalty Summary':
#       • Total dollars spent
#       • Total points earned
#       • Final tier




purchases = [12.50, 34.20, 200]

def earn_points(price): 
    whole_dollar = int(price)
    return whole_dollar * 3

def tier_label(points):
    if points >= 500:
        return "Gold"
    elif points >= 100:
        return "Silver"
    else:
        return "Bronze"
    
total_dollars_spent = 0
total_points_earned = 0


for every_purchase in purchases:
    total_dollars_spent += every_purchase
    total_points_earned += earn_points(every_purchase)

final_tier = tier_label(total_points_earned)    

print("===Loyalty summary===")
print(f'total dollars spent: {total_dollars_spent:.2f}')
print(f'total points earned: {total_points_earned}')
print(f'final tier: {final_tier}')