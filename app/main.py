import random

import discord

from discord import Message, VoiceChannel, Member

from modules.Command import Command, Function

TOKEN = "NzI1NTg0NjQ2OTAwODA5ODI4.XvQ4ng.kSJg3R7j2gciWPmjTuoJifMip0Q"
client = discord.Client()


@client.event
async def on_message(message: Message):
    if message.author != client.user and message.content.startswith('$'):
        try:
            command = Command.instantiate(message.content)
        except ValueError as e:
            await message.channel.send(f'パラメータの変換に失敗しました:man_bowing::man_bowing::man_bowing:\n```${e}```')
            return

        weapons = command.execute()

        if command.func is Function.give_me:
            weapon = weapons[random.randrange(0, len(weapons) - 1)]
            await message.channel.send(f'{message.author.mention} （っ\'-\')╮ =͟͟͞͞ **{weapon.name}** ﾌﾞｫﾝ')
        elif command.func is Function.give:
            for channel in message.guild.voice_channels:  # type: VoiceChannel
                for member in channel.members:  # type: Member
                    weapon = weapons[random.randrange(0, len(weapons) - 1)]
                    await message.channel.send(f'{member.mention}（っ\'-\')╮ =͟͟͞͞ **{weapon.name}** ﾌﾞｫﾝ')
        elif command.func is Function.help:
            await message.channel.send(f'ブキくじ\n'
                                       f'---- commands ----\n'
                                       f'`$give` : ボイスチャンネル接続中の全員に武器をわたす\n'
                                       f'`$give-me` : 自分にだけ武器をわたす\n'
                                       f'`$help` : ヘルプの表示\n'
                                       f'---- options ----\n'
                                       f'`--cat` , `--category` : 武器種をきめる ex: `$give --cat=シューター` \n'
                                       f'`--sub` : サブウェポンをきめる ex: `$give --sub=スプラッシュボム` \n'
                                       f'`--special` : スペシャルウェポンをきめる ex: `$give --special=スーパーチャクチ` \n'
                                       f':warning: いずれも正式名称じゃないと動かないので注意 :warning:\n'
                                       f':heart: オプションは併用できます :heart:')


client.run(TOKEN)
