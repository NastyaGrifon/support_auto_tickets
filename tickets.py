import datetime

tickets = [
    {"id": 1, "category": "customer_service", "status": "open"},
    {"id": 2, "category": "technical", "status": "closed"},
    {"id": 3, "category": "customer_service", "status": "open"},
    {"id": 4, "category": "technical", "status": "open"},
    {"id": 5, "category": "customer_service", "status": "open"},
]

report = []

# Считаем открытые
def get_unresolved_tickets(tickets):
    unresolved_ids = []
    for ticket in tickets:
        if ticket["status"] == "open":
            unresolved_ids.append(ticket["id"])
    unresolved_count = len(unresolved_ids)
    return unresolved_count, unresolved_ids

# Считаем по категориям
def count_tickets_by_category(tickets):
    category_count = {}
    for ticket in tickets:
        category = ticket["category"]
        if category in category_count:
            category_count[category] += 1
        else:
            category_count[category] = 1
    return category_count

# Записываем в файл
def write_report(report_lines, filename):
    with open(filename, "w", encoding="utf-8") as file:
        for line in report_lines:
            file.write(line + "\n")


# 1. Количество нерешённых тикетов и выдаст их список.
unresolved_count, unresolved_ids = get_unresolved_tickets(tickets)
report.append("Открытых тикетов: " + str(unresolved_count))
report.append("Список ID открытых тикетов: " + str(unresolved_ids))

# 2. Количество тикетов по каждой категории.
category_count = count_tickets_by_category(tickets)
report.append("Количество тикетов по категориям: " + str(category_count))

now = datetime.datetime.now()
report_name = "ticket_report_" + now.strftime("%Y%m%d_%H%M%S") + ".txt"

# Вывод report в консоль
for report_line in report:
    print(report_line)

# Запись report в файл
write_report(report, report_name)
print("Отчёт записан в файл:", report_name)
