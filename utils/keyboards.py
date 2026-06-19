from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def get_list_keyboard(page: int) -> InlineKeyboardMarkup:
    if page == 1:
        prev_callback = "noop"
    else:
        prev_callback = f"list:{page - 1}"
    
    current_callback = "noop"
    next_callback = f"list:{page + 1}"

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
    
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                prev_button,
                current_button,
                next_button,
            ]
        ]
    )

    return keyboard
