name=input("Hi what's your name:")
dob=input("Hi "+name+"Enter your date of birth:")
print(name,dob)
sum=0
for digit in dob:
    sum=sum+int(digit)
if sum>9:
    final_number = 0
    while  sum>0:
        final_number=final_number+sum%10
        sum=sum//10
else:
    final_number=sum
number = {
    1: "Independence, New Beginnings, leaderships",
    2: "Balance, Duality, Cooperation",
    3: "Creativity, Communication, Self-Expression",
    4: "Stability, Organization, Discipline",
    5: "Change, Adventure, Freedom",
    6: "Love, Nurturing, Responsibility",
    7: "Inner Wisdom, Spirituality, Knowledge",
    8: "Abundance, Power, Achievement",
    9: "Humanitarianism, Compassion, Universality"
}
print("You are of type:",final_number)
print("Your properties are:",number[final_number])