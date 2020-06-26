import json
import random

import discord
from discord import Message, VoiceChannel, Member

from modules.Command import Command, Function
from modules.SplatoonWeapon import SubWeapon, SpecialWeapon, Custom, Category

with open('config.json', 'r') as file:
    config = json.load(file)

TOKEN = config['token']
client = discord.Client()


@client.event
async def on_message(message: Message):
    if message.author != client.user and message.content.startswith('$'):
        try:
            command = Command.instantiate(message.content)

        except ValueError as e:
            if str(e).endswith('SubWeapon'):
                text = ''
                for it in SubWeapon:
                    text += str(it.value) + '\n'
                await message.channel.send(f'サブウェポンの名前が違うかも:thinking:\n```{text}```')

            elif str(e).endswith('Category'):
                text = ''
                for it in Category:
                    text += str(it.value) + '\n'
                await message.channel.send(f'ブキ種の名前が違うかも:thinking:\n```{text}```')

            elif str(e).endswith('SpecialWeapon'):
                text = ''
                for it in SpecialWeapon:
                    text += str(it.value) + '\n'
                await message.channel.send(f'スペシャルウェポンの名前が違うかも:thinking:\n```{text}```')

            elif str(e).endswith('Custom'):
                text = ''
                for it in Custom:
                    text += str(it.value) + '\n'
                await message.channel.send(f'そのカスタムは知らないです...\n```{text}```')

            else:
                await message.channel.send(f'パラメータの変換に失敗しました:man_bowing::man_bowing::man_bowing:\n```{e}```')

            return

        weapons = command.execute()

        if len(weapons) <= 0:
            await message.channel.send(f'{message.author.mention} ｿﾝﾅﾌﾞｷ(ヾﾉ･∀･`)ﾅｲﾅｲ')

        elif command.func is Function.give_me:
            if len(weapons) <= 1:
                await message.channel.send(f'{message.author.mention} （っ\'-\')╮ =͟͟͞͞    **{weapons[0].name}**    ﾌﾞｫﾝ')
            else:
                weapon = weapons[random.randrange(0, len(weapons) - 1)]
                await message.channel.send(f'{message.author.mention} （っ\'-\')╮ =͟͟͞͞    **{weapon.name}**    ﾌﾞｫﾝ')

        elif command.func is Function.give:
            for channel in message.guild.voice_channels:  # type: VoiceChannel
                for member in channel.members:  # type: Member
                    if len(weapons) <= 1:
                        await message.channel.send(
                            f'{message.author.mention} （っ\'-\')╮ =͟͟͞͞    **{weapons[0].name}**    ﾌﾞｫﾝ')
                    else:
                        weapon = weapons[random.randrange(0, len(weapons) - 1)]
                        await message.channel.send(f'{member.mention}（っ\'-\')╮ =͟͟͞͞     **{weapon.name}**    ﾌﾞｫﾝ')
        elif command.func is Function.help:
            await message.channel.send(f'ブキくじ\n'
                                       f'---- commands ----\n'
                                       f'`$give` : ボイスチャンネル接続中の全員に武器をわたす\n'
                                       f'`$give-me` : 自分にだけ武器をわたす\n'
                                       f'`$help` : ヘルプの表示\n\n'
                                       f'---- options ----\n'
                                       f'`--cat` , `--category` : 武器種をきめる ex: `$give --cat=シューター` \n'
                                       f'`--sub` : サブウェポンをきめる ex: `$give --sub=スプラッシュボム` \n'
                                       f'`--special` : スペシャルウェポンをきめる ex: `$give --special=スーパーチャクチ` \n'
                                       f'`--custom` : カスタムをきめる ex: `$give --custom=ブキチセレクション` `$give --custom=無印`\n\n'
                                       f':warning: いずれも正式名称じゃないと動かないので注意 :warning:\n'
                                       f':heart: オプションは併用できます（同一オプションはOR、他オプションはAND） :heart:')


client.run(TOKEN)
