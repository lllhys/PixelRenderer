import os
import pkgutil
from renderer.abstract_effectors.abstract_effector import AbstractEffector
from renderer.abstract_effectors.abstract_threading_effector import AbstractThreadingEffector
from component import loggers

logger = loggers.get_logger()

_has_init = False
_effectors = {}

def init_effectors():
    """
    动态加载效果器
    """

    global _has_init
    locations = [os.path.abspath(os.path.dirname(__file__))+"/effectors"]
    logger.info("检查效果器目录：{}".format(locations))

    global _effectors
    nameSet = set()

    for finder, name, ispkg in pkgutil.walk_packages(locations):
        try:
            loader = finder.find_module(name)
            mod = loader.load_module(name)
        except Exception:
            logger.info("效果器 {} 加载出错，跳过".format(name))
            continue

        effector_name = mod.Effector._name_

        # check conflict
        if effector_name in nameSet:
            logger.info("效果器 {} 名称({}) 重复，跳过".format(name,
                                                         effector_name))
            continue


        if issubclass(mod.Effector, AbstractEffector) or issubclass(mod.Effector, AbstractThreadingEffector):
            nameSet.add(effector_name)
            func = mod.Effector._func_
            _effectors[effector_name] = {'func':func,'effector':mod.Effector}
            logger.info("{} 效果器加载成功".format(effector_name))
    _has_init = True



def get_effector(effector_name,func_name):
    if _has_init == False:
        init_effectors()
    # 效果器存在时返回对应效果器，效果器不存在则返回默认。
    if _effectors.get(effector_name) is not None:
        # 操作支持时返回对应的效果器，操作不支持时返回默认效果器
        effector_desc = _effectors[effector_name]
        if func_name in effector_desc['func']:
            return effector_desc['effector']
        else:
            logger.info("效果器{}不支持{}方法，使用Default效果器".format(effector_name,func_name))
            return _effectors['default']['effector']
    else:
        logger.info("效果器{}不存在，使用Default效果器".format(effector_name))
        return _effectors['default']['effector']


