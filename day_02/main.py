def main():
    f = open('input.txt')

    spreadsheet = []

    for line in f:
        spreadsheet.append(line.strip().split('\t'))

    f.close()

    spreadsheet = [[int(cell) for cell in row] for row in spreadsheet]

    checksum = 0

    for row in spreadsheet:
        checksum += max(row) - min(row)

    print(f'Spreadsheet checksum (1): { checksum }')

    checksum = 0

    for row in spreadsheet:
        row.sort()
        left, right = 0, len(row) - 1

        while row[right] % row[left] != 0:
            left += 1

            if right == left:
                right -= 1
                left = 0

        checksum += row[right] // row[left]

    print(f'Spreadsheet checksum (2): { checksum }')


if __name__ == '__main__':
    main()
