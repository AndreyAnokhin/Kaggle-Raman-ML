# Модуль для подготовки данных
# Функция txt_to_pd - Загрузка файлов со спектрами. Преобразовывает набор txt файлов в один DataFrame.


import glob, os
import re
import pandas as pd


def txt_to_pd(path, pattern = '\d\d\dK'):
    '''
    Преобразует набор txt файлов со спектрами в один DataFrame.
    Извлекает значение температуры из названия файла и добавляет как название колонки.
    Первая колонка ("Wavenumber") должна быть одиаковой во всех файлах.
    Входные параметры:
    path - пусть к папке с файлами
    pattern - шаблон для поиска значения температуры в название файла, по умолчанию 'xxxK'

    '''
    os.chdir(path)
    file_names = glob.glob("*.txt")
    spectra = pd.DataFrame()
    for file_name in file_names:
        temp = int(re.search(pattern, file_name).group()[:3])
        spectrum = pd.read_csv(file_name, sep="\t", header=None, names=["Wavenumber", temp])
        if not("Wavenumber" in spectra.columns):
            spectra["Wavenumber"] = spectrum["Wavenumber"]
        spectra[temp] = spectrum[temp]
    return spectra

def main():
    path = 'datasets/Raman-SBN-50-Pt-Si/txt/'
    spectra = txt_to_pd(path)


if __name__ == '__main__':
    main()