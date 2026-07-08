# Этот файл отправляет карточку коктейля в Telegram как фото с caption или как обычный текст.
# Он нужен для image fallback: если URL невалидный или Telegram не принял фото, пользователь все равно получает рецепт.

from urllib.parse import urlparse

from aiogram.exceptions import TelegramBadRequest
from aiogram.types import InlineKeyboardMarkup, Message

from schemas.cocktail import CocktailRead


# Проверяет, что image_url похож на HTTP/HTTPS-ссылку.
def is_valid_http_url(url: str | None) -> bool:
    if not url:
        return False

    parsed_url = urlparse(url.strip())

    return (
        parsed_url.scheme in ("http", "https")
        and bool(parsed_url.netloc)
    )


# Отправляет карточку коктейля с фото или fallback-текстом.
async def send_cocktail_card(
    message: Message,
    cocktail: CocktailRead,
    text: str,
    reply_markup: InlineKeyboardMarkup | None = None,
) -> None:
    if is_valid_http_url(cocktail.image_url):
        try:
            await message.answer_photo(
                photo=cocktail.image_url.strip(),
                caption=text,
                reply_markup=reply_markup,
            )
            return
        except TelegramBadRequest:
            pass

    await message.answer(
        text,
        reply_markup=reply_markup,
    )
