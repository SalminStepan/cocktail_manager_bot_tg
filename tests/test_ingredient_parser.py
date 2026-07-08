# Этот файл проверяет поведение парсера ингредиентов.
# Он фиксирует правила разбора текстового ввода, чтобы legacy FSM-flow не принимал некорректные ингредиенты.

from utils.ingredient_parser import parse_ingredient_input
import pytest

# Проверяет разбор ингредиента без комментария.
def test_parse_ingredient_without_comment():
    row_without_cmnt = "Gin 30 ml"

    result = parse_ingredient_input(row_without_cmnt)

    assert result == {
        "name": "gin",
        "amount": 30,
        "unit": "ml",
        "comment": None,
    }

# Проверяет разбор ингредиента с названием из нескольких слов.
def test_parse_ingr_long_name():
    row = "Fresh Lemon Juice 20 ml"

    res = parse_ingredient_input(row)

    assert res == {
        "name": "fresh lemon juice",
        "amount": 20,
        "unit": "ml",
        "comment": None,
    }

# Проверяет прием единицы измерения из whitelist.
def test_parse_unit_from_white_list():
    row = "Ice 2 cube"

    res = parse_ingredient_input(row)

    assert res == {
        "name": "ice",
        "amount": 2,
        "unit": "cube",
        "comment": None,
    }

# Проверяет разбор ингредиента с текстовым комментарием.
def test_parse_ingredient_with_cmnt():
    row_with_cmnt = "Tonic 80 ml on top"

    result = parse_ingredient_input(row_with_cmnt)

    assert result == {
        "name": "tonic",
        "amount": 80,
        "unit": "ml",
        "comment": "on top",
    }

# Проверяет ошибку, когда в строке нет количества.
def test_parse_ingredient_without_amount_rais_err():
    row = "Gin ml"

    with pytest.raises(ValueError):
        parse_ingredient_input(row)

# Проверяет ошибку для единицы измерения вне whitelist.
def test_parse_ingredient_with_invalid_unit_rais_err():
    row = "Gin 30 bottle"

    with pytest.raises(ValueError):
        parse_ingredient_input(row)

# Проверяет ошибку для нулевого количества ингредиента.
def test_parse_ingredient_with_zero_amount_rais_err():
    row = "Gin 0 ml"

    with pytest.raises(ValueError):
        parse_ingredient_input(row)
