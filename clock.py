import time
from os import system, name
import datetime
from playsound import playsound

class Clock:
    
    def _realtime_display(self, hours, minutes, seconds):
        print(datetime.time(hours, minutes, seconds))
    
    def _clear_terminal(self):
        if name == 'nt':
            system('cls')
        else:
            system('clear')

    def _dis_cls_slp(self,hours,minutes,seconds):
        time.sleep(1)
        self._clear_terminal()
        self._realtime_display(hours,minutes,seconds)

    def timer(self, hours, minutes, seconds):

        # self.total = hours * 3600 + minutes * 60 + seconds

        self._clear_terminal()
        self._realtime_display(hours,minutes,seconds)
        while hours >= 0:
            while minutes >= 0:
                while seconds > 0:
                    seconds -= 1
                    self._dis_cls_slp(hours,minutes,seconds)
                minutes -= 1
                seconds = 59
                if minutes >= 0:
                    self._dis_cls_slp(hours,minutes,seconds)

            hours -= 1
            minutes = 59
            self._dis_cls_slp(hours,minutes,seconds)



# c = Clock()
# c.timer(2,2,20)




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
                try:
                    c.timer(h,m,s)
                except ValueError:
                    start_time = time.time()
                    end_time = start_time + 5
                    while time.time() < end_time:
                        playsound('Alarm-Sound.mp3')
    

                
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
