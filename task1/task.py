import sys
import pandas as pd


if len(sys.argv) != 4:
    print("Использование: python script.py <csv файл> <номер строки> <номер столбца>")
    sys.exit(1)


csv_file = sys.argv[1]
row_index = int(sys.argv[2])
column_index = int(sys.argv[3])


try:
    df = pd.read_csv(csv_file)
except FileNotFoundError:
    print(f"Файл '{csv_file}' не найден.")
    sys.exit(1)
except pd.errors.EmptyDataError:
    print(f"Файл '{csv_file}' пуст.")
    sys.exit(1)
except pd.errors.ParserError:
    print(f"Ошибка при чтении файла '{csv_file}'. Убедитесь, что это CSV-файл.")
    sys.exit(1)


try:
    cell_value = df.iloc[row_index, column_index]
    print(f"Значение в ячейке ({row_index}, {column_index}): {cell_value}")
except IndexError:
    print("Некорректные индексы строки и столбца. Убедитесь, что они существуют в таблице.")
