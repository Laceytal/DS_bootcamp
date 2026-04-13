import sys

def call_center(clients, recipients):
    return list(set(clients) - set(recipients))

def potential_clients(clients, participants):
    return list(set(participants) - set(clients))

def loyalty_program(clients, participants):
    return list(set(clients) - set(participants))

def markeeting(task):
    if task == "call_center":
        result = call_center(clients, recipients)
    elif task == "potential_clients":
        result = potential_clients(clients, participants)
    elif task == "loyalty_program":
        result = loyalty_program(clients, participants)
    else:
        raise ValueError("Unknown task name. Use: call_center, potential_clients, loyalty_program")

    print(result)


if __name__ == "__main__":
    clients = [
        'andrew@gmail.com', 'jessica@gmail.com', 'ted@mosby.com',
        'john@snow.is', 'bill_gates@live.com', 'mark@facebook.com',
        'elon@paypal.com', 'jessica@gmail.com'
    ]
    participants = [
        'walter@heisenberg.com', 'vasily@mail.ru',
        'pinkman@yo.org', 'jessica@gmail.com', 'elon@paypal.com',
        'pinkman@yo.org', 'mr@robot.gov', 'eleven@yahoo.com'
    ]
    recipients = [
        'andrew@gmail.com', 'jessica@gmail.com', 'john@snow.is'
    ]
    if len(sys.argv) != 2:
        print("Usage: python3 marketing.py <task>")
        sys.exit(1)
    task_name = sys.argv[1]
    markeeting(task_name)
