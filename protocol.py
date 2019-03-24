sigfox_hexa = 0x21134464D0A00500C01C8C01
lenght = 96
bin_host, bin_network = '', ''

def bin_format(sigfox_hexa, lenght):
    return f'{sigfox_hexa:0>{lenght}b}'

# def bin_protocol('sigfox_bin'):
#     for i in range(96):
#         if i <= 3:
#             bin_host = bin_host + sigfox_bin[i]
#         elif i <= 7:
#             bin_network = bin_network + sigfox_bin[i]
#         elif i <= 11:
#             sensor_1 = sensor_1 + sigfox_bin[i]
#         elif i <= 18:
#             env_tempeture = env_tempeture + sigfox_bin[i]
#         elif i <= 22:
#             sensor_2 = sensor_2 + sigfox_bin[i]
#         elif i <= 29:
#              obj_tempeture = obj_tempeture + sigfox_bin[i]
#         elif i <= 33:
#             sensor_3 = sensor_3 + sigfox_bin[i]
#         elif i <= 40:
#             env_humidity = env_humidity + sigfox_bin[i]
#         elif i <= 44:
#             sensor_4 = sensor_4 + sigfox_bin[i]
#         elif i <= 51:
#             soil_moisture_1 = soil_moisture_1 + sigfox_bin[i]
#         elif i <= 55:
#             sensor_5 = sensor_5 + sigfox_bin[i]
#         elif i <= 62:
#             soil_moisture_2 = soil_moisture_2 + sigfox_bin[i]
#         elif i <= 66:
#             sensor_6 = sensor_6 + sigfox_bin[i]
#         elif i <= 73:
#             soil_moisture_3 = soil_moisture_3 + sigfox_bin[i]
#         elif i <= 77:
#             sensor_7 = sensor_7 + sigfox_bin[i]
#         elif i <= 84:
#             sunlight = sunlight + sigfox_bin[i]
#         elif i <= 88:
#             sensor_8 = sensor_8 + sigfox_bin[i]
#         else:
#             uv = uv + sigfox_bin[i]


if __name__ == '__main__':
    sigfox_bin = bin_format(sigfox_hexa, lenght)
    bin_host = sigfox_bin[0:4]
    bin_network = sigfox_bin[4:8]
    bin_env_temp = sigfox_bin[12:19]
    bin_obj_temp = sigfox_bin[23:30]
    bin_env_humidity = sigfox_bin[34:41]
    bin_soil_moisture_1 = sigfox_bin[45:52]
    bin_soil_moisture_2 = sigfox_bin[56:63]
    bin_soil_moisture_3 = sigfox_bin[67:74]
    bin_sunlight = sigfox_bin[78:85]
    bin_uv = sigfox_bin[89:-1]

    print(bin_host, bin_network)
