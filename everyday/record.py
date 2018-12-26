import os
import argparse

from everyday import EverydayCalendar


def main():
    parser = argparse.ArgumentParser(description='Saving progress!...')
    parser.add_argument('-t', '--title', type=str, help='Name of the calendar.')
    args = parser.parse_args()

    savepath = os.path.join(os.getcwd(), 'cal/saves')
    savefile = os.path.join(savepath, args.title)

    calendar = EverydayCalendar(title=args.title)

    try:
        calendar.load(savefile)
    except FileNotFoundError:
        print('Starting new calendar!\n')

    calendar.update()
    calendar.progress()
    calendar.save(savepath)


if __name__=='__main__':
    main()
