import argparse
    
def main(argv=None):
    parser = argparse.ArgumentParser(description="A sample command-line application.")
    parser.add_argument('-h', '--help', action='help', help='Show this help message and exit')
    parser.add_argument('-v', '--version', action='version', version='1.0.0', help='Show program version and exit')
    parser.add_argument('--option1', action='store_true', help='Execute option 1 functionality')
    parser.add_argument('--option2', action='store_true', help='Execute option 2 functionality')
    parser.add_argument('--option3', action='store_true', help='Execute option 3 functionality')

    args = parser.parse_args(argv)

    if args.option1:
        print("[+] Analyze Images")
        # Add functionality for option 1 here

    if args.option2:
        print("Option 2 selected.")
        # Add functionality for option 2 here

    if args.option3:
        print("Option 3 selected.")
        # Add functionality for option 3 here

    if not (args.option1 or args.option2 or args.option3):
        parser.print_help()