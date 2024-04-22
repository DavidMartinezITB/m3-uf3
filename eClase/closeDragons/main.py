def main():
    try:
        with open('Dragon.in', 'r') as inp:
            data = inp.read().replace('0', 'x')
            with open('Dragon.out', 'w') as out:
                out.write(data)
    except:
        print('ERROR')

if __name__ == '__main__':
    main()