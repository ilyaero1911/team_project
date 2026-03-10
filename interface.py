from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.progress import track
import time

console = Console()

def show_banner():
    """Показывает красивый баннер при запуске"""
    console.print(Panel.fit(
        "[bold cyan]Командный проект[/]\n[green]Git и Python[/]",
        border_style="bright_blue"
    ))

def show_menu():
    """Показывает меню в виде таблицы"""
    table = Table(title="Доступные команды")
    table.add_column("№", style="cyan")
    table.add_column("Действие", style="green")
    table.add_column("Описание", style="white")
    
    table.add_row("1", "Информация", "Показать информацию о проекте")
    table.add_row("2", "Статус", "Проверить статус")
    table.add_row("3", "Выход", "Завершить программу")
    
    console.print(table)

def show_loading(message="Загрузка", seconds=2):
    """Показывает анимированную загрузку"""
    with console.status(f"[bold green]{message}..."):
        time.sleep(seconds)
    console.print("[bold green]✓ Готово![/]")

def show_progress():
    """Показывает прогресс-бар"""
    for step in track(range(100), description="[cyan]Выполнение..."):
        time.sleep(0.02)
