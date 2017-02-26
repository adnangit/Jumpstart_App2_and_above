def main():
    display_header()
    run_loop()


def display_header():
    print('--------------------')
    print('     JOURNAL')
    print('--------------------')


def run_loop():
    cmd = None

    journal_data = []

    while cmd != 'x':
        cmd = input('What would you like to do? [L]ist, [A]dd, E[x]it: ')
        cmd = cmd.lower().strip()
        if cmd == 'l':
            list_entries(journal_data)
        elif cmd == 'a':
            add_entry(journal_data)
        elif cmd != 'x':
            print("Sorry, I don't understand")

    print('Goodbye')


def list_entries(data):

    entries = reversed(data)
    for index, entry in enumerate(entries, 1):
        print('{} - {}'.format(index, entry))



def add_entry(data):
    entry = input('Type your journal data: ')
    data.append(entry)


main()
