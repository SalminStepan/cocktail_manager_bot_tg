CREATE TABLE IF NOT EXISTS cocktails (
    id BIGSERIAL PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,
    glass TEXT NOT NULL, 
    garnish TEXT NOT NULL,
    method TEXT NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS ingredients (
    id SERIAL PRIMARY KEY,
    cocktail_id BIGINT NOT NULL,
    name TEXT NOT NULL,
    amount_ml INT NOT NULL CHECK (amount_ml > 0),
    FOREIGN KEY (cocktail_id) REFERENCES cocktails(id) ON DELETE CASCADE
);