CREATE SCHEMA IF NOT EXISTS analytics;

CREATE TABLE IF NOT EXISTS analytics.bot_events (
    id BIGSERIAL PRIMARY KEY,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),

    event_type TEXT NOT NULL,

    telegram_user_id BIGINT,
    chat_id BIGINT,
    chat_type TEXT,

    command TEXT,
    callback_type TEXT,

    query TEXT,
    cocktail_id INTEGER,
    cocktail_name TEXT,

    status TEXT NOT NULL DEFAULT 'ok',
    duration_ms INTEGER,

    error_type TEXT,
    error_message TEXT,

    metadata JSONB NOT NULL DEFAULT '{}'::jsonb
);

CREATE INDEX IF NOT EXISTS idx_bot_events_created_at
    ON analytics.bot_events (created_at);

CREATE INDEX IF NOT EXISTS idx_bot_events_event_type
    ON analytics.bot_events (event_type);

CREATE INDEX IF NOT EXISTS idx_bot_events_telegram_user_id
    ON analytics.bot_events (telegram_user_id);

CREATE INDEX IF NOT EXISTS idx_bot_events_command
    ON analytics.bot_events (command);

CREATE INDEX IF NOT EXISTS idx_bot_events_cocktail_id
    ON analytics.bot_events (cocktail_id);