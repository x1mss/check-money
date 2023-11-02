import PySimpleGUI as sg
import time

sell_file = open('sell.txt','r', encoding='UTF-8')
sell_data =  sell_file.readlines()
buy_file = open('buy.txt','r', encoding='UTF-8')
buy_data =  buy_file.readlines()
sell_or_buy = "Доход"
sg.theme("LightBrown3")

buy_list = sg.Listbox(values=buy_data, key='buy', size=[20,5], enable_events=True, select_mode=sg.LISTBOX_SELECT_MODE_EXTENDED)
sell_list = sg.Listbox(values=sell_data, key='sell', size=[20,5], enable_events=True, select_mode=sg.LISTBOX_SELECT_MODE_EXTENDED)
income = sg.Button("Доход")
expenses = sg.Button("Расход")
imput_money = sg.InputText(key = 'money')
imput_source = sg.InputText(key = 'source')
label_source = sg.Text("Источник")
label_money = sg.Text("Деньги")
add = sg.Button("Добавить")
del_ = sg.Button("Удалить")
exit = sg.Button("Выход")

window = sg.Window("Контроль расходов/доходов", layout=[
    [buy_list ,sell_list],
    [income ,expenses],
    [label_money],
    [imput_money],
    [label_source],
    [imput_source],
    [add],
    [del_ , exit]],
    font=("Impact", 15),
)
while True:
    event, values = window.read(timeout=10)
    if event== sg.WIN_CLOSED:
            break
    elif event == "Добавить":
        if sell_or_buy == 'Доход':
            file = open('buy.txt','a', encoding="utf-8")
            file.write(values['money'] + ' руб ' + ' - ' + values['source']  + '\n')
            file.close()
            file = open('buy.txt','r', encoding="utf-8")
            a = file.readlines()
            window['buy'].update(values=a)
            file.close()
        elif sell_or_buy == 'Расход':
            file = open('sell.txt','a', encoding="utf-8")
            file.write(values['money'] + ' руб ' + ' - ' + values['source']  + '\n')
            file.close()
            file = open('sell.txt','r', encoding="utf-8")
            a = file.readlines()
            window['sell'].update(values=a)
            file.close()
    elif event == 'Доход':
        sell_or_buy = 'Доход'
    elif event == 'Расход':
        sell_or_buy = 'Расход'
    elif event == "Удалить":
        try:
            if values["buy"][0] != None:
                file = open('buy.txt','r', encoding="utf-8")
                a = file.readlines()
                a.remove(values["buy"][0])
                file.close()
                file = open('buy.txt', 'w', encoding="utf-8")
                file.writelines(a)
                window['buy'].update(values=a)
                file.close()
        except IndexError:
            pass
        try:
            if values["sell"][0] != None:
                file = open('sell.txt','r', encoding="utf-8")
                a = file.readlines()
                a.remove(values["sell"][0])
                file.close()
                file = open('sell.txt', 'w', encoding="utf-8")
                file.writelines(a)
                window['sell'].update(values=a)
                file.close()
        except IndexError:
            pass
    elif event == 'buy':
        sell_list.update(set_to_index=[])
    elif event == 'sell':
        buy_list.update(set_to_index=[])

window.close()