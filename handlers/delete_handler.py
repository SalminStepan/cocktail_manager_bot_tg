import logging
from aiogram import Router, types
from aiogram.filters.command import Command
from services.cocktail_services import delete_cocktail_by_name
from config import ADMIN_IDS

logger = logging.getLogger(__name__)
delete_router = Router()

@delete_router.message(Command("delete"))
async def delete_cocktail_handler(message: types.Message):
    user_id = message.from_user.id

    if user_id not in ADMIN_IDS:
        logger.warning("Unauthorized /delete attempt by user %s", user_id)
        await message.answer("Access denied")
        return

    parts = message.text.split()
    if len(parts) < 2:
        await message.answer("Usage: /delete <cocktail name>")
        return

    name = " ".join(parts[1:])
    logger.info("User %s requested delete for '%s'", user_id, name)

    try:
        cocktail_id = delete_cocktail_by_name(name)
    except Exception:
        logger.error(
            "Delete failed for user %s (name='%s')",
            user_id,
            name,
            exc_info=True
        )
        await message.answer("Delete failed")
        return

    if cocktail_id is None:
        logger.warning(
            "User %s tried to delete non-existing cocktail '%s'",
            user_id,
            name,
        )
        await message.answer("Cocktail not found")
        return

    logger.info(
        "User %s deleted cocktail '%s' (id=%s)",
        user_id,
        name,
        cocktail_id
    )

    await message.answer(f"Cocktail deleted (id: {cocktail_id})")