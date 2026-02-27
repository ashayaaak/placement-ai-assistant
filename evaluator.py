def evaluate_response(response):
    if len(response) < 20:
        return "Response too short"
    return "Response looks good"