"""
Module for security dependencies bot
"""

import asyncio

from functools import wraps

import discord
from discord.ext import commands

from setup import setup


def verify_owner_bot(func):
    """
    Decorator for verify owner bot
    """

    @wraps(func)
    async def wrapper(ctx: commands.Context, *args, **kwargs):
        """Wrapper for verify owner bot"""
        if ctx.author.id == setup.BOT_OWNER_ID:
            return await func(ctx, *args, **kwargs)
        else:

            embed = discord.Embed(
                title="Aviso",
                description="Comando apenas para o dono do bot",
                color=discord.Color.red()
            )

            message = await ctx.send(embed=embed)
            await asyncio.sleep(3)
            await message.delete()
            await ctx.message.delete()

    return wrapper
