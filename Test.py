# Testing ground for lesson
# for i in range(1,11,1):
#     print("A"*i)

# def Attack():
#     DMG = 10
# def Player_Health():
#     HP = 100

# for i in range(1,3,1):
#     Hurt = Attack() - Player_Health()
#     print(Hurt)
# def display_info():
#     print("Hello")
#     print()
#     print("I bi-")
#     print()
#     print("myself")
#     print()
#     return "Split Screen Gooning Tech", "Playing Both Sides", "Double The fish zero pull"
# Tech, Sides, Sea = display_info()
# print(Tech)
# print(Sides)
# print(Sea)
# Taon_Today = 2025
# def Compute_Age(Birth_Year, Year_Today):
#     global Taon_Today
#     Taon_Today = 6767
#     print(f"Taon Noon: {Taon_Today}")
#     print(f"Taon Ngayon: {Year_Today}")
#     return Year_Today - Birth_Year
# print(Compute_Age(1992, 2026))
# print(Taon_Today)
# def Compute_Age(Birth_Year:int, Year_Today:int):
#     '''This makes you gae'''
#     return Year_Today - Birth_Year

# print(Compute_Age(2007, 2026))
# def count(limit, num = 1):
#     print(num)
#     if num < limit:
#         num += 1
#         count(limit, num)
# count(100)
# def Pyramid(amount, max_letters = 0, index = 0):
#     max_letters = len(amount) - 1
#     print(amount[index])
#     if index < max_letters:
#         index += 1
#         Pyramid(amount, max_letters, index)

# amount = input("How large will this pyramid be? ")
# Pyramid(amount,max_letters,index)
# def Pyramid(base, max_size = 0, index = 0):
#     global base_global
#     max_size = len(base_global[index]) - 1
#     if index < max_size:
#         index += 1
#         print("*"*base_global)
#         Pyramid(base, max_size, index)
base = int(input("Base of a Pyramid "))
def pyramid(base, max_stars = 0, index = 1):
    max_stars = base
    print(f"{'* '*index:^100}")
    if index < max_stars:
        index += 1
        pyramid(base, max_stars, index)
    else:
        print(f"Done! Pyramid with {base} * Base")
pyramid(base)