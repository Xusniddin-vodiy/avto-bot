import os
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

API_TOKEN = os.getenv("8668632754:AAEXGwJZB4pVuEdPgjELvJiB1PBlBoc9K98")

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

channels = {
    "#tahoe": -1003904657707,
    "#equinox": -1003539247125,
    "#malibu": -1003752675712,
    "#onix": -1003973192547,
    "#captiva": -1003827894357,
    "#nexia": -1003975266175,
    "#gentra": -1003989860274,
    "#matiz": -1003878990621,
    "#spark": -1003738707897,
    "#damas": -1003809354458,
    "#labo": -1003809354458,
    "#monza": -1003797749107,
    "#tracker": -1003972713851,
    "#orlando": -1003850462605,
    "#trailblazer": -1003806863783,
    "#tico": -1003877691183,
    "#fura": -1003993025292,
    "#inomarka": -1003666897042,
    "#cobalt": -1001484563003,
}

# 🔴 ASOSIY KANAL (shu eng muhim!)
SOURCE_CHANNEL = -1001437422385

@dp.channel_post_handler()
async def repost(message: types.Message):
    text = (message.text or message.caption or "").lower()

    if message.chat.id != SOURCE_CHANNEL:
        return

    for tag, channel_id in channels.items():
        if tag in text:
            await bot.copy_message(
                chat_id=channel_id,
                from_chat_id=message.chat.id,
                message_id=message.message_id
            )

if __name__ == "__main__":
    executor.start_polling(dp)
