import webbrowser
from win10toast_click import ToastNotifier

page_url = 'https://github.com/esdrasribas'
# page_url2 = 'Digite a URL para abrir na notificação'
# page_url3 = 'Digite a URL para abrir na notificação'


def open_url():
    try:
        webbrowser.open_new(page_url)
        print('Abrindo GitHub')
    except:
        print("Falha ao tentar abrir URL's.")

notification = ToastNotifier()

notification.show_toast(
    "Notificação GitHub",
    "Click na notificação para abrir o GitHub",
    # icon_path='Report.ico',
    duration=10,
    threaded=True,
    callback_on_click=open_url
)