from src.utils.c_log import log


async def on_ready(bot):
    print(f"We have logged in as {bot.user}")


def should_log(bot, message):
    return "hi bot" == message.content.lower()


@log("saying hello to user", log_condition=should_log)
async def on_message(bot, message):
    if "hi bot" == message.content.lower():
        channel = message.channel
        await channel.send(f"hi {message.author}")
    await bot.process_commands(message)
