import sys
import time
from yoctopuce.yocto_api import YAPI, YRefParam
from yoctopuce.yocto_tilt import YTilt
from yoctopuce.yocto_accelerometer import YAccelerometer


def main():
    errmsg = YRefParam()
    if YAPI.RegisterHub("usb", errmsg) != YAPI.SUCCESS:
        print('Unable to init accelerometer')
        sys.exit()

    any_tilt = YTilt.FirstTilt()
    if not (any_tilt.isOnline()):
        print('Module not connected (check identification and USB cable)')
        YAPI.FreeAPI()
        sys.exit()

    module = any_tilt.get_module()
    sn = module.get_serialNumber()
    accelerometer = YAccelerometer.FindAccelerometer(sn + ".accelerometer")
    count = 0
    while True:
        try:
            value = accelerometer.get_currentValue()
            x_value = accelerometer.get_xValue()
            y_value = accelerometer.get_yValue()
            z_value = accelerometer.get_zValue()
            print(f'{count}: common: {value}, x: {x_value}, y: {y_value}, z: {z_value}')
            count += 1
            time.sleep(1)
        except KeyboardInterrupt:
            YAPI.FreeAPI()
            break


if __name__ == '__main__':
    print(f'To stop processing type Ctrl+C')
    main()
