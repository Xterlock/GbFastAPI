import enum


class OrderStatus(enum.StrEnum):
    ready = "Готов"
    issued = "Выдан"
    paid = "Оплачен"
    awaiting_payment = "Ожидает оплаты"