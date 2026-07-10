SELECT
    created_at::date AS day,
    COUNT(*) AS events,
    COUNT(DISTINCT telegram_user_id) AS unique_users
FROM analytics.bot_events
GROUP BY created_at::date
ORDER BY day DESC;

SELECT
    command,
    COUNT(*) AS uses
FROM analytics.bot_events
WHERE command IS NOT NULL
  AND status = 'ok'
GROUP BY command
ORDER BY uses DESC;

SELECT
    query,
    COUNT(*) AS searches
FROM analytics.bot_events
WHERE event_type = 'search'
  AND status = 'ok'
  AND query IS NOT NULL
GROUP BY query
ORDER BY searches DESC, query
LIMIT 20;

SELECT
    query,
    COUNT(*) AS attempts
FROM analytics.bot_events
WHERE event_type = 'search'
  AND status = 'not_found'
  AND query IS NOT NULL
GROUP BY query
ORDER BY attempts DESC, query
LIMIT 20;

SELECT
    cocktail_id,
    cocktail_name,
    COUNT(*) AS views
FROM analytics.bot_events
WHERE event_type = 'cocktail_view'
  AND status = 'ok'
  AND cocktail_id IS NOT NULL
GROUP BY cocktail_id, cocktail_name
ORDER BY views DESC, cocktail_name
LIMIT 20;

SELECT
    COALESCE(command, callback_type) AS source,
    COUNT(*) AS views
FROM analytics.bot_events
WHERE event_type = 'cocktail_view'
  AND status = 'ok'
GROUP BY COALESCE(command, callback_type)
ORDER BY views DESC;

SELECT
    event_type,
    command,
    callback_type,
    status,
    COUNT(*) AS events
FROM analytics.bot_events
WHERE status <> 'ok'
GROUP BY event_type, command, callback_type, status
ORDER BY events DESC;

SELECT
    event_type,
    command,
    callback_type,
    status,
    COUNT(*) AS events
FROM analytics.bot_events
WHERE created_at >= now() - INTERVAL '24 hours'
GROUP BY event_type, command, callback_type, status
ORDER BY events DESC;

