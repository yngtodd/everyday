import os
import argparse

from everyday.calendar import EverydayCalendar


def main():
    parser = argparse.ArgumentParser(description='Saving progress!...')
    parser.add_argument('--title', type=str, help='Name of the calendar.')
    args = parser.parse_args()

    savepath = os.path.join(os.getcwd(), 'calendar/saves')
    savefile = os.path.join(savepath, args.title)

    calendar = EverydayCalendar(title=args.title)

    try:
        calendar.load(savefile)
    except FileNotFoundError:
        print('Starting new calendar!\n')

    calendar.update()
    calendar.progress()
    calendar.save()


if __name__=='__main__':
    main()
