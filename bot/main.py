#!/usr/bin/env python
# coding: utf-8

# In[3]:


import database
import discord
import os
from discord.ext import commands
from discord.ext.tasks import loop

#cmd.exe /c C:/Users/User/Python/Projects/Discord_bot/botrun.bat


bot = commands.Bot(command_prefix='?', intents=discord.Intents.all())


@bot.event
async def on_ready():
    global df_manager
    print("I am Squee! I'm Spleen! And I'm Spoon!")
    df_manager = database.DatabaseManager()
    Save.start()
        
@bot.command()
async def test(ctx):
    await ctx.send('я в тильте')


@bot.command()
async def Book_of_knowledge(ctx, *arg):
    arg = ' '.join(arg)
    print(arg)
    author = ctx.message.author
    comands = {'': f'{author.mention} :Напиши в чат:\n?Book_of_knowledge о боте\n?Book_of_knowledge команды',
                'о боте':f"{author.mention} I am Squee! I'm Spleen! And I'm Spoon! Чекай трон",
                'команды':f"{author.mention}\n ?test - Тест состояния\n ?Book_of_knowledge - Базовая информация"}
    
    
    await ctx.send(comands.get(arg, f"{author.mention} Такой команды нет"))
    
     
"""@bot.command()
async def Stats(ctx, *arg):          
    if arg[0] == 'добавить':
        if arg[1] == 'выиграли' or arg[1] == 'проиграли':
            df_manager.add_match(arg[1])
        else:
            await ctx.send('попробуйте добавить выиграли или добавить проиграли')
    elif arg[0] == 'удалить':
        df_manager.remove_match()
    elif arg[0] == 'показать':
        await ctx.send(df_manager.get_stats(arg[1]))
    else:
        await ctx.send('Неизвестная команда')"""

@bot.command()
async def Stats(ctx, *arg):
    emb = discord.Embed(title = 'Текущая статистика', colour = discord.Color.green())
    emb.set_author(name = bot.user.name, icon_url= bot.user.avatar_url)
    emb.set_footer(text = ctx.author.name, icon_url= ctx.author.avatar_url)
    if arg[0] == 'добавить':
        if arg[1] == 'выиграли' or arg[1] == 'проиграли':
            df_manager.add_match(arg[1])
        else:
            await ctx.send('попробуйте добавить выиграли или добавить проиграли')
    elif arg[0] == 'удалить':
        df_manager.remove_match()
    elif arg[0] == 'показать':
        emb.add_field(name='Статистика', value='Статистика:\n```{}```'.format(df_manager.table_print(arg[1])))
        await ctx.send(embed = emb)
    else:
        await ctx.send('Неизвестная команда')
        
        

@loop(seconds=5)
async def Save():
    df_manager.save_data()

    
    
                     
bot.run(os.getenv('TOKEN'))


# In[ ]:




