HELP_TEXT = """__**I Can Play Music In The Voice Chat**__

**/start** __To Start The bot.__
**/help** __To Show This Message.__
**/skip** __To Skip The Current Playing Music.__
**/play** __<youtube/saavn/deezer> <Song_Name>__
**/joinvc** __To Join A Voice Chat.__
**/leavevc** __To Leave A Voice Chat.__
**/telegram** __To Play From Telegram Audio.__

__**NOTE: Do Not Assign These Commands To Bot Via BotFather.**__"""

START_TEXT = "f"""<b>👋🏻 Hi {message.from_user.first_name}!</b>
I am Swifties Music Bot, a bot that lets you play music in @Swiftiesworld voice chat.
This bot is created by @TayLife. 
Use the buttons below to know more about me.""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⚒ Creator", url="https://t.me/taylife"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "💬 Group", url="https://t.me/swiftiesworld"
                    ),
                    InlineKeyboardButton(
                        "Channel 🔈", url="https://t.me/taylorswift13fanpage"
                    ),
                    InlineKeyboardButton(
                        "Discography 😈", url="https://t.me/taylorflac"

                    )
                ]
            ]
        )
    )"

REPO_TEXT = "[Group](t.me/swiftiesworld)" \
            + " | [Group](t.me/taylorswift13fanpage)"
