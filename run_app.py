import os
import sys
import multiprocessing
import streamlit.web.cli as stcli
import webview

def run_streamlit():
    # Указываем путь к интерфейсу ui.py, который лежит внутри сборки
    if getattr(sys, 'frozen', False):
        # Если запущено как .exe, берем из временной папки сборки
        base_dir = sys._MEIPASS
    else:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        
    script_path = os.path.join(base_dir, "ui.py")
    
    sys.argv = [
        "streamlit", 
        "run", 
        script_path, 
        "--server.headless=true", 
        "--server.port=8501"
    ]
    stcli.main()

if __name__ == "__main__":
    # Защита мультипроцессорности для скомпилированных программ
    multiprocessing.freeze_support()
    
    # Запускаем локальный веб-сервер Streamlit в фоновом процессе
    p = multiprocessing.Process(target=run_streamlit)
    p.start()
    
    # Открываем чистое окно программы без браузерных строк адреса
    try:
        webview.create_window(
            "Система диагностики QDA", 
            "http://localhost:8501", 
            width=1200, 
            height=850
        )
        webview.start()
    finally:
        # При закрытии окна принудительно гасим сервер Streamlit
        p.terminate()
        p.join()
