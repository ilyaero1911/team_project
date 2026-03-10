from utils import greet
from config import APP_NAME
from interface import show_banner, show_menu, show_loading, show_progress
import sys

def main():
    # 1. Сначала показываем красивый баннер (rich)
    show_banner()
    
    # 2. Показываем информацию из config.py
    print(f"\n[bold yellow]Приложение:[/] {APP_NAME}")
    
    # 3. Используем существующую функцию greet из utils.py
    from utils import greet
    greet("Student")  # Это уже было
    
    # 4. Добавляем новое интерактивное меню
    while True:
        show_menu()
        
        try:
            choice = input("\nВыберите действие (1-3): ")
            
            if choice == "1":
                show_loading("Загружаем информацию")
                print("\nИнформация о проекте:")
                print(f"   - Название: {APP_NAME}")
                print("   - Версия: 1.0")
                print("   - Статус: В разработке\n")
                
            elif choice == "2":
                show_progress()
                print("\nВсё работает отлично!\n")
                
            elif choice == "3":
                print("\nДо свидания!\n")
                break
            else:
                print("\nНеверный выбор. Попробуйте снова.\n")
                
        except KeyboardInterrupt:
            print("\n\nПрограмма завершена\n")
            break

if __name__ == "__main__":
    main()
