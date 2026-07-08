# Этот файл собирает inline-клавиатуры для списка, поиска и возврата назад.
# Он вынесен в utils, чтобы handlers не смешивали бизнес-логику с ручной сборкой Telegram-кнопок.

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# Собирает inline-клавиатуру списка коктейлей с пагинацией.
def get_cocktail_list_keyboard(cocktails: list[dict], page: int) -> InlineKeyboardMarkup:
    if page == 1:
        prev_callback = "noop"
    else:
        prev_callback = f"list:{page - 1}"
    
    current_callback = "noop"
    next_callback = f"list:{page + 1}"

    rows = []

    for cocktail in cocktails:
        cocktail_button = InlineKeyboardButton(
            text=cocktail["name"],
            callback_data=f"cocktail:{cocktail['id']}:{page}"    
        )
        rows.append([cocktail_button])

    prev_button = InlineKeyboardButton(
        text="<< Prev", 
        callback_data=prev_callback
    )

    current_button =InlineKeyboardButton(
        text=f"Page {page}",
        callback_data=current_callback,
    )

    next_button = InlineKeyboardButton(
        text="Next >>",
        callback_data=next_callback,
    )
    
    rows.append([
        prev_button, 
        current_button, 
        next_button,
    ])

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=rows
    )

    return keyboard

# Собирает кнопку возврата к странице списка.
def back_to_list_keyboard(page: int)-> InlineKeyboardMarkup:
    back_button = InlineKeyboardButton(
        text="<< Back to list",
        callback_data=f"list:{page}",
    )
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [back_button]
        ]
    )
    return keyboard

# Собирает inline-клавиатуру результатов поиска с пагинацией.
def search_results_keyboard(cocktails: list[dict], page: int, query: str) -> InlineKeyboardMarkup:
    query = " ".join(query.strip().replace(":", " ").split())[:20]

    if page == 1:
        prev_callback = "noop"
    else:
        prev_callback = f"s_p:{page - 1}:{query}"
    
    current_callback = "noop"
    next_callback = f"s_p:{page + 1}:{query}"

    rows = []

    for cocktail in cocktails:
        cocktail_button = InlineKeyboardButton(
            text=cocktail["name"],
            callback_data=f"s_c:{cocktail['id']}:{page}:{query}"    
        )
        rows.append([cocktail_button])

    prev_button = InlineKeyboardButton(
        text="<< Prev", 
        callback_data=prev_callback
    )

    current_button =InlineKeyboardButton(
        text=f"Page {page}",
        callback_data=current_callback,
    )

    next_button = InlineKeyboardButton(
        text="Next >>",
        callback_data=next_callback,
    )
    
    rows.append([
        prev_button, 
        current_button, 
        next_button,
    ])

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=rows
    )
    return keyboard

# Собирает кнопку возврата к странице результатов поиска.
def back_to_search_keyboard(page:int, query: str) -> InlineKeyboardMarkup:
    query = " ".join(query.strip().replace(":", " ").split())[:20]

    back_button = InlineKeyboardButton(
        text="<< Back to search",
        callback_data=f"s_p:{page}:{query}",
    )
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [back_button]
        ]
    )
    return keyboard
