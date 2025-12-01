import argparse
import os
import shutil


def copy_files_recursive(src_dir, dst_dir):
    """
    Рекурсивно читає директорії, знаходить файли та копіює їх y dst_dir,
    сортує за розширеннями.
    """
    try:
        for entry in os.scandir(src_dir):
            # Якщо елемент  директорія: рекурсивно заходимо
            if entry.is_dir():
                copy_files_recursive(entry.path, dst_dir)

            # Якщо елемент  файл: копіюємо
            elif entry.is_file():
                try:
                    # Отримуємо розширення файлу
                    ext = os.path.splitext(entry.name)[1].lower().lstrip(".")
                    if not ext:
                        ext = "no_extension"

                    # Створюємо піддиректорію за розширенням
                    ext_dir = os.path.join(dst_dir, ext)
                    os.makedirs(ext_dir, exist_ok=True)

                    # Копіюємо файл
                    shutil.copy2(entry.path, ext_dir)
                    print(f"Copied: {entry.path} -> {ext_dir}")

                except Exception as e:
                    print(f"Помилка копіювання файлу {entry.path}: {e}")

    except Exception as e:
        print(f"Помилка доступу до директорії {src_dir}: {e}")


def main():
    parser = argparse.ArgumentParser(description="Recursive file copier & sorter.")
    parser.add_argument("src", help="Шлях до вихідної директорії")
    parser.add_argument(
        "dst",
        nargs="?",
        default="dist",
        help="Шлях до директорії призначення (за замовчуванням 'dist')"
    )

    args = parser.parse_args()

    src_dir = args.src
    dst_dir = args.dst

    if not os.path.isdir(src_dir):
        print(f"Помилка: директорія {src_dir} не існує.")
        return

    os.makedirs(dst_dir, exist_ok=True)
    copy_files_recursive(src_dir, dst_dir)


if __name__ == "__main__":
    main()
