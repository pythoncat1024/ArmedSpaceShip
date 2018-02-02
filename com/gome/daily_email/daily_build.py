# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     daily_build
   Description :
   Author :       cat
   date：          2018/2/2
-------------------------------------------------
   Change Activity:
                   2018/2/2:
-------------------------------------------------
"""


# -*- coding: utf-8 -*-
def scheduler_build(delay, cmd):
    def build_inner():
        import os
        import threading
        print('execute==> ', delay, cmd)
        os.system(cmd)
        threading.Timer(delay, build_inner).start()

    build_inner()


if "__main__" == __name__:
    cmd = r'source build/envsetup.sh && lunch full_gm12b-userdebug && repo sync -j8 && make clean && source build/envsetup.sh && lunch full_gm12b-userdebug && make update-api && make -j8 2>&1 | tee build.log'


    # cmd = r'source build/envsetup.sh && lunch full_gm12b-userdebug'
    def f():
        scheduler_build(1 * 60 * 60 * 24, cmd)


    import threading

    threading.Timer(1, f).start()
    pass
