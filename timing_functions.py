from datetime import datetime


def calculate_seconds_to_send_message(future_time: str) -> float:
    now = datetime.today()
    future_time = datetime.strptime(future_time, "%d/%m/%Y %H:%M:%S")
    time_differance = future_time - now
    return time_differance.total_seconds()
