import time
from os import system, name

class Clock:
    
    def timer(self, hours, minutes, seconds):
        self.total = hours * 3600 + minutes * 60 + seconds

        while self.total >= 0:
            if name == 'nt':
                system('cls')
            else:
                system('clear')

            print(self.total)
            time.sleep(1)
            self.total -= 1

def commands():
    print('------------- Welcome to Clock Program -------------')
    print('1.Timer\n2.Alarm\n3.Stop Watch\n4.Exit')
    return input('select an option: ')

def main():

    while True:
        user_input = commands()
        match user_input:
            case '1':
                h = int(input('Hours: '))
                m = int(input('Minutes: '))
                s = int(input('Seconds: '))

                c = Clock()  
                c.timer(h,m,s)
                
            case '2':
                print('this feature will be add soon')
                print('-' * 52)
            case '3':
                print('this feature will be add soon')
                print('-' * 52)
            case '4':
                print('exiting...')   
                print('-' * 52)
                break

if __name__ == '__main__':
    main()
