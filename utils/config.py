from nonebot import get_driver, logger
import nonebot

Bot_NICKNAME: str = list(nonebot.get_driver().config.nickname)[0]
Bot_MASTER: str = list(nonebot.get_driver().config.master)[0]
Bot_ID: int = list(nonebot.get_driver().config.bot_id)[0]
COMMAND_START: str = list(nonebot.get_driver().config.command_start)[0]

config = get_driver().config.dict()

if 'pictures_number' not in config.keys():
    logger.warning('[初号姬] 未发现配置项 `PICTURES_NUMBER` , 将采用默认值：5')
    pictures_number = config.get('pictures_number', 5)
else:
    pictures_number = config.get('pictures_number')

if 'sauce_key' not in config.keys():
    logger.warning('[初号姬] 未发现配置项 `SAUCE_KEY` , 请在env中配置')
else:
    sauce_key = config.get('sauce_key')

if 'num_res' not in config.keys():
    logger.warning('[初号姬] 未发现配置项 `NUM_RES` , 将采用默认值：5')
    num_res = config.get('num_res', 5)
else:
    num_res = config.get('num_res')

if 'over_list' not in config.keys():
    logger.warning('[初号姬] 未发现配置项 `OVER_LIST` , 采用默认值: 20')
    over_list = config.get('over_list', 20)
else:
    over_list = config.get('over_list')
