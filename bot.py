import os
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

# TOKEN Railway Variables'dan олади
API_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# 🔥 Каналлар
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

# 🔴 АСОСИЙ КАНАЛ (сен пост ташлайдиган)
SOURCE_CHANNEL = -1003003013714  # ← буни ўзингни канал ID билан алмаштир

@dp.channel_post_handler()
async def repost(message: types.Message):
    text = (message.text or message.caption or "").lower()

    # Фақат асосий каналдан келса ишлайди
    if message.chat.id != SOURCE_CHANNEL:
        return

    for tag, channel_id in channels.items():
        if tag in text:
            await bot.copy_message(
                chat_id=channel_id,
                from_chat_id=message.chat.id,
                message_id=message.message_id
            )

# 🚀 START
if __name__ == "__main__":
    executor.start_polling(dp)
