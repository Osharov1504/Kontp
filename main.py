import json
import os
from datetime import datetime

class NotesApp:
    def __init__(self):
        self.notes = []
        self.data_file = "notes.json"
        self.load_data()

    def load_data(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as file:
                self.notes = json.load(file)

    def save_data(self):
        with open(self.data_file, 'w') as file:
            json.dump(self.notes, file, indent=2)

    def add_note(self, title, message):
        note = {
            "id": len(self.notes) + 1,
            "title": title,
            "message": message,
            "timestamp": str(datetime.now())
        }
        self.notes.append(note)
        self.save_data()
        print("Заметка успешно добавлена.")

    def read_notes(self, filter_date=None):
        if not self.notes:
            print("Список заметок пуст.")
            return

        if filter_date:
            filtered_notes = [note for note in self.notes if filter_date in note["timestamp"]]
            if not filtered_notes:
                print(f"Заметок с датой {filter_date} не найдено.")
                return
            else:
                self._print_notes(filtered_notes)
        else:
            self._print_notes(self.notes)

    def edit_note(self, note_id, new_title, new_message):
        for note in self.notes:
            if note["id"] == note_id:
                note["title"] = new_title
                note["message"] = new_message
                note["timestamp"] = str(datetime.now())
                self.save_data()
                print("Заметка успешно отредактирована.")
                return

        print(f"Заметка с ID {note_id} не найдена.")

    def delete_note(self, note_id):
        for note in self.notes:
            if note["id"] == note_id:
                self.notes.remove(note)
                self.save_data()
                print("Заметка успешно удалена.")
                return

        print(f"Заметка с ID {note_id} не найдена.")

    def _print_notes(self, notes_list):
        for note in notes_list:
            print(f"ID: {note['id']}")
            print(f"Заголовок: {note['title']}")
            print(f"Тело: {note['message']}")
            print(f"Дата/Время: {note['timestamp']}")
            print("-" * 30)

if __name__ == "__main__":
    app = NotesApp()

    while True:
        print("1. Добавить заметку")
        print("2. Просмотреть заметки")
        print("3. Редактировать заметку")
        print("4. Удалить заметку")
        print("5. Выход")

        choice = input("Введите номер команды: ")

        if choice == "1":
            title = input("Введите заголовок заметки: ")
            message = input("Введите тело заметки: ")
            app.add_note(title, message)
        elif choice == "2":
            filter_date = input("Введите дату для фильтрации (YYYY-MM-DD): ")
            app.read_notes(filter_date)
        elif choice == "3":
            note_id = int(input("Введите ID заметки для редактирования: "))
            new_title = input("Введите новый заголовок заметки: ")
            new_message = input("Введите новое тело заметки: ")
            app.edit_note(note_id, new_title, new_message)
        elif choice == "4":
            note_id = int(input("Введите ID заметки для удаления: "))
            app.delete_note(note_id)
        elif choice == "5":
            print("Выход из программы.")
            break
        else:
            print("Некорректная команда. Пожалуйста, выберите номер команды из списка.")






 


