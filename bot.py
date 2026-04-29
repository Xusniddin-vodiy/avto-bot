import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

API_TOKEN = os.getenv("BOT_TOKEN")

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
    "фаргона": -1002103035302,
    "андижон": -1002963143087,
    "наманган": -1003032467221,
    
}

SOURCE_CHANNEL = -1003003013714

# 🔥 group storage
media_groups = {}

@dp.channel_post_handler(content_types=types.ContentTypes.ANY)
async def repost(message: types.Message):

    text = (message.caption or message.text or "").lower()

    if message.chat.id != SOURCE_CHANNEL:
        return

    for tag, channel_id in channels.items():
        if tag in text:

            # 🔥 агар альбом бўлса
            if message.media_group_id:

                group_id = message.media_group_id

                if group_id not in media_groups:
                    media_groups[group_id] = []

                media_groups[group_id].append(message)

                # 🔥 ҳамма расм келишини кутиш
                await asyncio.sleep(1.5)

                # фақат 1 марта юбориш учун
                if len(media_groups[group_id]) > 0:

                    for msg in media_groups[group_id]:
                        await bot.copy_message(
                            chat_id=channel_id,
                            from_chat_id=msg.chat.id,
                            message_id=msg.message_id
                        )

                    media_groups[group_id] = []

            else:
                # оддий пост
                await bot.copy_message(
                    chat_id=channel_id,
                    from_chat_id=message.chat.id,
                    message_id=message.message_id
                )


if __name__ == "__main__":
    executor.start_polling(dp)
