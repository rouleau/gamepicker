from src.gamepicker.quotidienne import *


def test_constructor():
    lottery_ticket = Quotidienne(4)
    assert lottery_ticket.name == "Quotidienne 4"
