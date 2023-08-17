import time
from os import system, name
import datetime
from pygame import mixer

class Clock:
    
    def _realtime_display(self, hours=0, minutes=0, seconds=0, milliseconds=0):
        print(datetime.time(hours, minutes, seconds,milliseconds))
    

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
            try:
                self._dis_cls_slp(hours,minutes,seconds)
            except ValueError:
                return True
            

    def alarm(self, hours, minutes):
        now = datetime.datetime.now()
        alarm_time = now.replace(hour=hours, minute=minutes, second=0)
        remained_time = abs(alarm_time - now)

        while remained_time.total_seconds() > 0:
            self._clear_terminal()
            print(f'Remainig Time --> {remained_time}')
            remained_time -= datetime.timedelta(seconds=1)
            time.sleep(1)
        self._clear_terminal()
        return True
    

    def stop_watch(self, elps_time):
        minutes = int(elps_time // 60)
        seconds = int(elps_time % 60)
        milliseconds = int((elps_time % 1) * 1000)
        
        self._realtime_display(minutes=minutes,seconds=seconds,milliseconds=milliseconds)

        print(f"\nElapsed Time: {minutes} minutes, {seconds} seconds, {milliseconds} milliseconds")


def commands():
    print('------------- Welcome to Clock Program -------------')
    print('1.Timer\n2.Alarm\n3.Stop Watch\n4.Exit')
    return input('select an option: ')


def play_sound():
    mixer.init()
    mixer.music.load("sound.mp3")
    mixer.music.play()
    print('Tap enter to stop...', end='')
    if input() or True:
        mixer.music.stop()


def main():

    while True:
        user_input = commands()
        match user_input:
            case '1':
                while True:
                    h = int(input('Hours: '))
                    m = int(input('Minutes: '))
                    s = int(input('Seconds: '))

                    c = Clock()  
                    try:
                        if c.timer(h,m,s):
                            play_sound()
                            break

                    except ValueError:
                        print('ValueError: enter in this scale:\n0 <= hour < 24\n0 <= minute < 60\n0 <= second < 60')
                    
                
            case '2':
                h, m = list(map(lambda x: int(x),input('Enter desire time (in 24h format --> HH:MM): ').split(':')))
                c = Clock()
                if c.alarm(h, m):
                    play_sound()
                print('-' * 52)


            case '3':
                start_time = time.time()
                input("Press Enter to stop the stopwatch...")
                end_time = time.time()
                elapsed_time = end_time - start_time
                c = Clock()
                c.stop_watch(elapsed_time)
                print('-' * 52)
            case '4':
                print('exiting...')   
                print('-' * 52)
                break

            case other:
                print('Invalid...')
                print('-' * 52)


if __name__ == '__main__':
    main()
