import uuid
import logging
import datetime
from pytz import timezone


async def service_dummy(request):

    # get hash id
    id = str(uuid.uuid1().hex)

    # datetime local
    now = datetime.datetime.now(timezone("America/Sao_Paulo")).isoformat()

    try:
        a = request.number1
        b = request.number2

        if request.operator == "soma":
            soma = a + b

        msg = "Operation " + str(request.operator) + " done!"

        response = {
            "id": id,
            "datetime": now,
            "soma": soma,
            "msg": msg
        }

        return response

    except Exception as e:
        msg = "API Error " + str(e)
        logging.error(msg)
        response.update({"msg": msg})

        return None