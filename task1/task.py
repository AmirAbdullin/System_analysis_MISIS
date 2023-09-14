import sys
import pandas as pd

csv_file = sys.argv[1]
search_string = sys.argv[2]
column_name = sys.argv[3]


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


filtered_df = df[df[column_name].str.contains(search_string, case=False, na=False)]


print("Результат:")
print(filtered_df)




