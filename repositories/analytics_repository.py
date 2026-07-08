# Этот файл содержит низкоуровневую запись событий бота в analytics-схему PostgreSQL.
# Он находится в repositories, потому что работает напрямую с SQL и не принимает продуктовых решений об аналитике.

from typing import Any
from psycopg.types.json import Jsonb


# Вставляет одно событие бота в analytics.bot_events и возвращает id.
def insert_bot_event(
    conn,
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
    metadata: dict[str, Any] | None = None,
) -> int :
    with conn.cursor() as cur:
        cur.execute(
            """
            INSERT INTO analytics.bot_events (
                event_type,
                telegram_user_id,
                chat_id,
                chat_type,
                command,
                callback_type,
                query,
                cocktail_id,
                cocktail_name,
                status,
                duration_ms,
                error_type,
                error_message,
                metadata
            )
            VALUES (
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
            )
            RETURNING id;
            """,
            (
                event_type,
                telegram_user_id,
                chat_id,
                chat_type,
                command,
                callback_type,
                query,
                cocktail_id,
                cocktail_name,
                status,
                duration_ms,
                error_type,
                error_message,
                Jsonb(metadata or {}),
            ),
        )
        row = cur.fetchone()
        return row["id"]
