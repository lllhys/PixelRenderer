import os
import pkgutil
from renderer.abstract_effectors.abstract_effector import AbstractEffector
from renderer.abstract_effectors.abstract_threading_effector import AbstractThreadingEffector


_has_init = False
_effectors = {}


def init_effectors():
    """
    动态加载效果器
    """

    global _has_init
    print()
    # os.path.normpath()
    # locations = [config.get_effector_path()]
    locations = ["./effectors"]
    print("检查效果器目录：{}".format(locations))

    global _effectors
    nameSet = set()

    for finder, name, ispkg in pkgutil.walk_packages(locations):
        try:
            loader = finder.find_module(name)
            mod = loader.load_module(name)
        except Exception:
            print("效果器 {} 加载出错，跳过".format(name))
            continue

        effector_name = mod.Effector.name

        # check conflict
        if effector_name in nameSet:
            print("效果器 {} 名称({}) 重复，跳过".format(name,
                                                         effector_name))
            continue
        nameSet.add(effector_name)


        if issubclass(mod.Effector, AbstractEffector) or issubclass(mod.Effector, AbstractThreadingEffector):
            print("效果器 {} 加载成功 ".format(name))
            _effectors[effector_name] = mod.Effector
    _has_init = True



def get_effector(effector_name):
    if _has_init == False:
        init_effectors()
    # 效果器存在时返回对应效果器，效果器不存在则返回默认。
    if _effectors.get(effector_name) is not None:
        return _effectors[effector_name]
    else:
        print("效果器{}不存在，使用Default效果器".format(effector_name))
        return _effectors['Default']


