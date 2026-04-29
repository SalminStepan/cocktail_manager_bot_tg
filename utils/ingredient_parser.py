def parse_ingredient_input(text: str) -> dict:
    
    ALLOWED_UNITS = {"ml", "dash", "pcs", "g", "cube", "bspn"}
    
    parts = text.split()

    idx = None
    for i, part in enumerate(parts):
        if part.isdigit():
            idx = i
            break

    if idx is None:
        raise ValueError("Invalid format. Example: Gin 30 ml or Tonic 80 ml on_top")                    
        
    amount = int(parts[idx])

    if amount <= 0:
        raise ValueError("Amount must be greater than 0")
        
    name = " ".join(parts[:idx]).strip().lower()
    if not name:
        raise ValueError("Ingredient name is required")
    if idx + 1 >= len(parts):
        raise ValueError("Unit is required")

    unit_part = parts[idx + 1].strip().lower()
    if unit_part not in ALLOWED_UNITS:
        raise ValueError(f"Invalid unit. Allowed units: {', '.join(ALLOWED_UNITS)}")
    
    unit = unit_part

    comment_parts = parts[idx + 2:]
    comment = " ".join(comment_parts).strip() or None
    return{
        "name": name,
        "amount": amount,
        "unit": unit,
        "comment": comment,
    }
