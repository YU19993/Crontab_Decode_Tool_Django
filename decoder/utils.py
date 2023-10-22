def decode_crontab(expression):
    fields = expression.split()
    if len(fields) != 5:
        return "Invalid crontab expression. Ensure you have 5 time scheduling fields."

    field_names = ['minute', 'hour', 'day of the month', 'month', 'day of the week']
    field_ranges = [(0, 59), (0, 23), (1, 31), (1, 12), (0, 6)]
    field_values = ['0-59', '0-23', '1-31', '1-12 or JAN-DEC', '0-6 or SUN-SAT']

    decoded_expression = []

    for idx, field in enumerate(fields):
        # Range validation
        if not field == "*":
            if "," in field:
                values = field.split(',')
                for val in values:
                    if not val.isdigit() or not field_ranges[idx][0] <= int(val) <= field_ranges[idx][1]:
                        return f"Value {val} for {field_names[idx]} is out of range ({field_values[idx]})."
            elif "-" in field:
                start, end = field.split('-')
                if not (start.isdigit() and end.isdigit()) or not (field_ranges[idx][0] <= int(start) <= field_ranges[idx][1] and field_ranges[idx][0] <= int(end) <= field_ranges[idx][1]):
                    return f"Range {start}-{end} for {field_names[idx]} is out of range ({field_values[idx]})."
            elif "/" in field:
                value, step = field.split('/')
                if not (value.isdigit() and step.isdigit()) or not (field_ranges[idx][0] <= int(value) <= field_ranges[idx][1]):
                    return f"Step value {value}/{step} for {field_names[idx]} is out of range ({field_values[idx]})."
            elif not field.isdigit() or not field_ranges[idx][0] <= int(field) <= field_ranges[idx][1]:
                return f"Value {field} for {field_names[idx]} is out of range ({field_values[idx]})."

        # Decode special characters
        decoded = field
        if '*' in field:
            decoded = decoded.replace('*', 'every')
        if ',' in field:
            decoded = decoded.replace(',', ' and ')
        if '-' in field:
            start, end = field.split('-')
            decoded = f"from {start} to {end}"
        if '/' in field:
            value, step = field.split('/')
            decoded = f"every {step} starting from {value}"
        if 'L' in field:
            decoded = decoded.replace('L', 'last')
        if 'W' in field:
            decoded = decoded.replace('W', 'nearest weekday')

        decoded_expression.append(f"For {field_names[idx]}, it's set to: {decoded} ({field_values[idx]})")

    return '. '.join(decoded_expression)
