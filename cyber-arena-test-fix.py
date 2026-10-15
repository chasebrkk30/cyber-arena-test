is_approved = None
final_entry_cost = None
fighter_class = None
fighter_name = input('What is your name?')
age = int(input('How old are you?'))
if age < 18:
    is_approved = False
    print(f"You are too young to fight in the Cyber Arena! {age} does not meet the age requirement of 18!")
else:
    is_approved = True
if is_approved:
    strength_rating = float(input('What is your current CSRA (Cyber Strength Rating Association) strength rating?'))
    agility_rating = float(input('What is your current CSRA agility rating?'))
    vip_pass_status = input('Do you have a VIP pass? (Yes/No)')
    entry_fee = 150.0


if is_approved:
    if strength_rating >= 80.0 and agility_rating <= 60.0:
        fighter_class = 'Juggernaut'
    elif agility_rating >= 80.0 and strength_rating <= 60.0:
        fighter_class = 'Shadow Rouge'
    elif 75.0 <= strength_rating <= 100.0 and 75.0 <= agility_rating <= 100.0:
        fighter_class = 'Apex Cyber-Warrior'
    elif strength_rating + agility_rating >= 100.0:
        fighter_class = 'Well Rounded'
    else:
        fighter_class = 'Scrapper'

if is_approved and vip_pass_status == 'Yes':
    final_entry_cost = (entry_fee / 2)
else:
    final_entry_cost = entry_fee

if is_approved:
    print(f"Name: {fighter_name}")
    print(f"Combat Class: {fighter_class}")
    print("Power Score:",(strength_rating + agility_rating) / 2)
    print(f"Entry Fee: {final_entry_cost}")


