from googletrans import Translator

translator = Translator()

with open("task_4.txt", "r") as file_read:
    with open("task_4_result.txt", "w") as file_write:
        for line in file_read:
            file_write.write(f"{translator.translate(f'{line}', dest='ru').text}\n")

