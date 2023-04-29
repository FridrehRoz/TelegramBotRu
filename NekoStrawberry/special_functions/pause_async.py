"""
Используется для погружения корутинов в сон
"""

import asyncio


async def pause(delay: int = 1) -> None:
    """
    Приостанавливает активный корутин.

    :param delay: Длительность паузы
    """
    await asyncio.sleep(delay)
