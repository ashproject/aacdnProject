import logging
import asyncio

from aiocoap import *

logging.basicConfig(level=logging.INFO)

async def main():
    """Perform a single PUT request to localhost on the default port, URI
    "/other/block".
    The payload is bigger than 1kB, and thus sent as several blocks."""

    context = await Context.create_client_context()

    payload = b"Hello.\n"
    request = Message(code=PUT, payload=payload)
    # These direct assignments are an alternative to setting the URI like in
    # the GET example:
    request.opt.uri_host = '10.0.0.101'
    request.opt.uri_path = ("other","block")

    response = await context.request(request).response

    print('Result: %s\n%r'%(response.code, response.payload))

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
