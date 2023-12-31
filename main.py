# -*- coding: utf-8 -*-
"""Data App AZ1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ro1VAamaA-eTRRD60kpNxiGqmt2eajT8
"""



"""# Data app **Shimoku**"""

!pip install shimoku-api-python

#Code
#enviroments

import os

os.environ['SHIMOKU_TOKEN'] = '096740ae-9d8c-47c6-975d-b11d062c6aae'
os.environ['UNIVERSE_ID'] = '6431886e-6dec-4eae-98aa-d0aae0a6e1d0'
os.environ['WORKSPACE_ID'] = '5c9f5204-4852-4f02-9d85-e28b35648def'



import os
import shimoku_api_python as Shimoku

from shimoku_components_catalog.html_components import (
    create_h1_title, button_click_to_new_tab, beautiful_indicator,
    box_with_button, panel,
)

access_token = os.getenv('SHIMOKU_TOKEN')
universe_id = os.getenv('UNIVERSE_ID')
workspace_id = os.getenv('WORKSPACE_ID')

# Verifica si las variables de entorno son None o están vacías
if not access_token or not universe_id or not workspace_id:
    raise ValueError('Falta configurar las variables de entorno correctamente.')



# Crea la instancia del cliente Shimoku
s = Shimoku.Client(
    access_token=access_token,
    universe_id=universe_id,
)
s.set_workspace(uuid=workspace_id)

s.set_board('BARRA PERSONALIZADA')

s.set_menu_path('catalog', 'bAR app 1')

s.plt.html(
    order=0,
    html=s.html_components.box_with_button(
        title='Datta APP',
        line='integrated in the SDK with the power of Data Analytics & AI',
        href='https://shimoku.com',
        background="https://res.cloudinary.com/tecnologi-zifrikc/image/upload/v1699236503/791931e49d02961ab9588885981e6d0f_mb6lt5.gif",
    ),
)
s.plt.html(
    order=1,
    html=s.html_components.panel(
        href='https://docs.shimoku.com/development/',
        text='Attention, this is highly adictive content ',
        button_panel='Read more',
        symbol_name='insights'
    )
)
s.plt.html(
    order=2,
    cols_size=4,
    padding='1,8,0,0',
    html=s.html_components.create_h1_title(
        title='Happy Holy days',
        subtitle='New campaign 2023!'
    )
)
s.set_menu_path('catalog', 'bAR app 4')


s.plt.html(
    order=6, rows_size=1, cols_size=6,
    html=s.html_components.beautiful_indicator(

        title='cHARMANDER',
        background_url='https://res.cloudinary.com/tecnologi-zifrikc/image/upload/v1685116663/charmander_qykdci.gif',
        href='https://res.cloudinary.com/tecnologi-zifrikc/image/upload/v1685116663/charmander_qykdci.gif'
    )
)


s.set_menu_path('catalog', 'bAR app 5')


data = [
    {'date': dt.date(2021, 1, 1), 'gas': 4, 'oil': 5},
    {'date': dt.date(2021, 1, 2), 'gas': 7, 'oil': 6},
    {'date': dt.date(2021, 1, 3), 'gas': 4, 'oil': 7},
    {'date': dt.date(2021, 1, 4), 'gas': 9, 'oil': 5},
    {'date': dt.date(2021, 1, 5), 'gas': 3, 'oil': 9},
    {'date': dt.date(2021, 1, 6), 'gas': 6, 'oil': 5},
    {'date': dt.date(2021, 1, 7), 'gas': 8, 'oil': 6},
]

s.plt.predictive_line(
    data=data, x='date', order=2,
    min_value_mark=3, max_value_mark=4,
    rows_size=2, cols_size=12, padding='0,0,0,1',
    title='Fossil price evolution - first days 2023.'
)

s.plt.html(
    order=6, rows_size=1, cols_size=4,
    html=s.html_components.beautiful_indicator(
        title='Blastoise',
        background_url='https://res.cloudinary.com/tecnologi-zifrikc/image/upload/v1685116664/blastoise_tw4vpj.gif',
        href='https://res.cloudinary.com/tecnologi-zifrikc/image/upload/v1685116664/blastoise_tw4vpj.gif'

    )
)

s.plt.html(
    order=6, rows_size=1, cols_size=5,
    html=s.html_components.beautiful_indicator(

        title='Bulbasaur',
        background_url='https://res.cloudinary.com/tecnologi-zifrikc/image/upload/v1685116664/bulbasaur_pz7osp.gif',
        href='https://res.cloudinary.com/tecnologi-zifrikc/image/upload/v1685116664/bulbasaur_pz7osp.gif'
    )
)

!pip install flask

!pip install pyngrok

!pip install flask-ngrok

!ngrok config add-authtoken 2Z3lZKAisoWqdBey824F7z6Q0He_5Pma8wN4PfZAs6873cu5J

!python app.py