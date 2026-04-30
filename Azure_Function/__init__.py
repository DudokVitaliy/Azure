import logging
import azure.functions as func
import random

def generate_color():
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Generate random colors function processed a request.")

    try:
        count = int(req.params.get("count", 1))
    except ValueError:
        return func.HttpResponse("Invalid count parameter", status_code=400)

    colors = [generate_color() for _ in range(count)]

    return func.HttpResponse(
        str(colors),
        status_code=200,
        mimetype="application/json"
    )