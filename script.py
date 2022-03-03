import json
import os


def file_read(thing):
    with open(rf'/sys/bus/i2c/devices/i2c-1/1-0018/iio:device0/{thing}') as files:
        string = files.read()
        string1 = string[0:(len(string)-1)]
        return string1


if __name__ == '__main__':
    dataframe = {}
    folder_list = ('in_accel_x_raw', 'in_accel_x_scale', 'in_accel_y_raw', 'in_accel_y_scale', 'in_accel_z_raw', 'in_accel_z_scale', 'name', 'sampling_frequency')
    for folders in folder_list:
        dataframe[folders] = file_read(folders)

    print(json.dumps(dataframe, indent=2))



