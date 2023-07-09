from datetime import datetime
from Incaps import Incapsyl

def run():
    while True:
        choice = int(input('Choice method:'
                       '\n1.отримати публічний атрибут'
                       '\n2.отримати захищенний атрибут'
                       '\n3.отримати приватний атрибут'
                       '\n4.використати сеттер '
                       '\n5.використати делеттер:\n'))


        n = Incapsyl(12, 54, 3)

        if choice == 1:
            el = n.x
            print(el)
            with open('text_time.txt', 'a') as file:
                file.write(f'\nattribute_public = {str(el)} , date = {str(datetime.time(datetime.now()))}\n')
                file.close()

        elif choice == 2:
            el = n._y
            print(el)
            with open('text_time.txt', 'a') as file:
                file.write(f'\nattribute_protected = {str(el)} , date = {str(datetime.time(datetime.now()))}\n')
                file.close()

        elif choice == 3:
            el = n.three
            print(el)
            with open('text_time.txt', 'a') as file:
                file.write(f'\nattribute_private = {str(el)} , date = {str(datetime.time(datetime.now()))}\n')
                file.close()

        elif choice == 4:
            new_el = input('print new attribute: ')
            n.three = new_el
            print(n.three)
            with open('text_time.txt', 'a') as file:
                file.write(f'\nsetter = {n.three} , date = {str(datetime.time(datetime.now()))}\n')
                file.close()

        elif choice == 5:
            el = n.three
            print(el)
            del n.three
            print(n.__dict__)
            with open('text_time.txt', 'a') as file:
                file.write(f'\ndeletter = {el} , date = {str(datetime.time(datetime.now()))}\n')
                file.close()



run()
