# Этот файл содержит сервисную обертку для записи событий аналитики.
# Он нужен, чтобы handlers не работали напрямую с SQL и не падали, если логирование события временно недоступно.

from repositories.analytics_repository import insert_bot_event
from db.connection import get_connection
from typing import Any
import logging

logger = logging.getLogger(__name__)

# Безопасно логирует событие бота и не роняет основной сценарий.
def log_bot_event(
    *,
    event_type: str,
    telegram_user_id: int | None = None,
    chat_id: int | None = None,
    chat_type: str | None = None,
    command: str | None = None,
    callback_type: str | None = None,
    query: str | None = None,
    cocktail_id: int | None = None,
    cocktail_name: str | None = None,
    status: str = "ok",
    duration_ms: int | None = None,
    error_type: str | None = None,
    error_message: str | None = None,
    metadata: dict[str, Any] | None = None) -> int | None:
    try:
        with get_connection() as conn:
            event_id = insert_bot_event(
                conn,
                event_type=event_type,
                telegram_user_id=telegram_user_id,
                chat_id=chat_id,
                chat_type=chat_type,
                command=command,
                callback_type=callback_type,
                query=query,
                cocktail_id=cocktail_id,
                cocktail_name=cocktail_name,
                status=status,
                duration_ms=duration_ms,
                error_type=error_type,
                error_message=error_message,
                metadata=metadata
            )
            conn.commit()
            return event_id
    except Exception as e:
        logger.warning("Bot event logging failed: %s", e)
        return None
