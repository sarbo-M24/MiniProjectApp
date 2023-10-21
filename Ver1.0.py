habit1 = {'valid': False,
          'complete': False,
          'name': "",
          'exp': '',
          'gold': ''}
habit2 = {'valid': False,
          'complete': False,
          'name': "",
          'exp': '',
          'gold': ''}
habit3 = {'valid': False,
          'complete': False,
          'name': "",
          'exp': '',
          'gold': ''}


def add_habit():
    if (habit1['valid'] == False):
        habit1['name'] = input("Enter the name of the habit :  ")
        habit1['exp'] = input("Enter the amt of exp you will get:  ")
        habit1['gold'] = input("Enter the amt of gold you will get:  ")
        habit1['valid'] = True

    elif (habit2['valid'] == False):
        habit2['name'] = input("Enter the name of the habit :  ")
        habit2['exp'] = input("Enter the amt of exp you will get:  ")
        habit2['gold'] = input("Enter the amt of gold you will get:  ")
        habit2['valid'] = True

    elif (habit3['valid'] == False):
        habit3['name'] = input("Enter the name of the habit :  ")
        habit3['exp'] = input("Enter the amt of exp you will get:  ")
        habit3['gold'] = input("Enter the amt of gold you will get:  ")
        habit3['valid'] = True

    print("yess")


def complete_habit():
    if (habit1['complete'] == False):
        habit1['complete'] = True
    elif (habit2['complete'] == False):
        habit2['complete'] = True
    elif (habit3['complete'] == False):
        habit3['complete'] = True
    else:
        print('No habits are completed')


def display_habit():
    if (habit1['valid'] == True):
        if (habit1['complete'] == False):
            print(habit1['name'], 'habit not completed')
        if (habit1['complete'] == True):
            print(habit1['name'], 'habit completed')

    elif (habit2['valid'] == True):
        if (habit2['complete'] == False):
            print(habit2['name'], 'habit not completed')
        if (habit2['complete'] == True):
            print(habit2['name'], 'habit completed')

    elif (habit3['valid'] == True):
        if (habit3['complete'] == False):
            print(habit3['name'], 'habit1 not completed')
        if (habit3['complete'] == True):
            print(habit3['name'], 'habit completed')
    else:
        print('No habits are added')


while True:
    print("\nHabit Tracker Menu:")
    print("1. Add a new habit")
    print("2. Mark a habit as completed")
    print("3. Display habit tracker")
    print("4. Add rewards for habits")
    print("5. Quit")

    choice = input("Enter your choice (1/2/3/4/5): ")
    if choice == "1":
        add_habit()
    elif choice == "2":
        complete_habit()
    elif choice == "3":
        display_habit()

    elif choice == "5":
        break

    else:
        print("Invalid choice. Please select a valid option (1/2/3/4/5).")
