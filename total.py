def total_salary(path):
    try:
        with open(path, 'r') as file:
            total = 0
            count = 0
            for line in file:
                line = line.strip()
                parts = line.split(",")
                try:
                    part = int(parts[-1])
                except ValueError:
                    print(f"У рядку '{line}' зарплата некоректна: '{parts[-1]}'")
                    continue
                total += part
                count += 1
                print(line)
            average = total // count
            return total, average    
    except FileNotFoundError:
        print("Файл не знайдено. Перевірте шлях до файлу.")
        return
    except IOError:
        print("Сталася помилка при читанні файлу.")
        return


