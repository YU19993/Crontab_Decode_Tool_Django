def validate_field(field, valid_range):
    # Handle wildcard
    if field == "*":
        return True

    # Handle comma-separated lists
    if "," in field:
        return all(validate_field(subfield, valid_range) for subfield in field.split(","))

    # Handle range with step values
    if "/" in field:
        range_part, step_part = field.split("/")
        if not validate_field(range_part, valid_range):
            return False
        if not step_part.isdigit() or int(step_part) < 1:
            return False
        return True

    # Handle range
    if "-" in field:
        start, end = field.split("-")
        if not start.isdigit() or not end.isdigit():
            return False
        if not valid_range[0] <= int(start) <= valid_range[1] or not valid_range[0] <= int(end) <= valid_range[1]:
            return False
        return True

    # Handle individual values
    if field.isdigit():
        return valid_range[0] <= int(field) <= valid_range[1]

    # Handle special characters L and W
    if field in ["L", "W"]:
        return True

    return False

def decode_crontab(expression):
    fields = expression.split()
    if len(fields) != 5:
        return "Invalid crontab expression. Ensure you have 5 time scheduling fields."

    field_names = ['minute', 'hour', 'day of the month', 'month', 'day of the week']
    field_ranges = [(0, 59), (0, 23), (1, 31), (1, 12), (0, 6)]

    for field, valid_range in zip(fields, field_ranges):
        if not validate_field(field, valid_range):
            return f"Invalid value in {field}. It doesn't match the allowed range or format."

    decoded_expression = [f"{name}: {value}" for name, value in zip(field_names, fields)]
    return ', '.join(decoded_expression)
