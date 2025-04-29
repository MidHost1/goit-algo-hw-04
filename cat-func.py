#Завдання №2
def get_cats_info(path):
    cats_list = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) != 3:
                    continue
                cat_dict = {
                    "id": parts[0],
                    "name": parts[1],
                    "age": parts[2]
                }
                cats_list.append(cat_dict)
    except FileNotFoundError:
        print ("Файл не знайдено!")
    except IOError:
        print("Помилка при зчитуванні файлу.")
    return cats_list
cats = get_cats_info("cat-list.txt")
output = ""
for cat in cats:
    output += f"{cat}\n"
print(output)
