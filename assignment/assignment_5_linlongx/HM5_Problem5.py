def main():
    args = sys.argv[1:]
    if not args:
        print("Usage: [--summaryfile] file [file ...]")
        sys.exit(1)

    summary = False
    if args[0] == '--summaryfile':
        summary = True
        del args[0]

    for filename in args:
        names = extract_names(filename)
        text = '\n'.join(names) + '\n'

        if summary:
            with open(filename + '.summary', 'w') as out_file:
                out_file.write(text)
        else:
            print(text)