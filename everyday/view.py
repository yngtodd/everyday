import os
import argparse

from everyday import EverydayCalendar


def main():
    parser = argparse.ArgumentParser(description='Saving progress!...')
    parser.add_argument('--title', type=str, help='Name of the calendar.')
    args = parser.parse_args()

    savepath = os.path.join(os.getcwd(), 'cal/saves')
    savefile = os.path.join(savepath, args.title)

    calendar = EverydayCalendar(title=args.title)

    try:
        calendar.load(savefile)
        calendar.progress()
    except FileNotFoundError:
        print(f'No saved file for {args.title}!\n')


if __name__=='__main__':
    main()