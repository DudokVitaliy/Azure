import azure.functions as func
import logging
import random

app = func.FunctionApp()

def generate_color():
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))

@app.route(route="colors", auth_level=func.AuthLevel.ANONYMOUS)
def http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Generating random colors')

    # беремо count з query string
    count = req.params.get('count')

    try:
        count = int(count) if count else 1
    except ValueError:
        return func.HttpResponse("count must be a number", status_code=400)

    colors = [generate_color() for _ in range(count)]

    return func.HttpResponse(
        body=str(colors),
        mimetype="application/json"
    )