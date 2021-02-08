import json

with open("task_7.txt","r") as file_read:
    with open("task_7_result.txt", "w") as file_write:
        data = {line.split()[0]: int(line.split()[2]) - int(line.split()[3]) for line in file_read}
        summa = 0
        i= 0
        result = [{}]
        for key in data:
            if data[key] > 0:
                summa += data[key]
                result[0].update({key: data[key]})
            i += 1
        result.append({"average_profit": summa/i})
        file_write.write(json.dumps(result))