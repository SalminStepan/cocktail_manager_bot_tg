from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

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
        text=f"Page:{page}",
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