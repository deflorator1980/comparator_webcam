# Разпознавание человека по видео

```bash
    python3 webcam3.py # Postgres
    python3 webcam.py  # Mongo
    python3 webcams.py # SQLite
```
### Заполнить базу, распознать по фото (закомментировать ненужное):
```bash    
        python3 fr3.py <file>.jpg # Postgres
        python3 fr.py <file>.jpg  # Mongo
        python3 frs.py <file>.jpg  # SQLite
```
### Распознать по фото + возраст, пол (Python 3.6)*
```bash
        pip install py-agender[cpu]
        python frs_ag.py <file>.jpg
```
*при ошибке см. https://github.com/deflorator1980/comparator_webcam/wiki

## Installation on Ubuntu 17.10 and higher:
```bash
    sudo apt install cmake -y
    sudo -H pip3 install -r requirements.txt
    [sudo apt install libpython3.6-dev]
```    

![](gif.gif)

