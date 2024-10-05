import asyncio
import aiohttp


async def main():

    async with aiohttp.ClientSession() as session:
        # response = await session.post(
        #     "http://localhost:8080/advertisement/",
        #     json={"title": "Перфоратор",
        #           "description": "Продаю срочно",
        #           "creator_email": "vkorsh456@mail.ru"},
        # )
        # print(response.status)
        # print(await response.text())

        # response = await session.patch(
        #     "http://localhost:8080/advertisement/1/",
        #     json={"title": "Дрель"},
        # )
        # print(response.status)
        # print(await response.text())

        response = await session.delete(
            "http://localhost:8080/advertisement/1/",
        )
        print(response.status)
        print(await response.text())

        response = await session.get(
            "http://localhost:8080/advertisement/1/",
        )
        print(response.status)
        print(await response.text())


asyncio.run(main())
