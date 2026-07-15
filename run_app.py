import os
import sys
import multiprocessing
import streamlit.web.cli as stcli
import webview

def run_streamlit():
    if getattr(sys, 'frozen', False):
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
    multiprocessing.freeze_support()
    
    p = multiprocessing.Process(target=run_streamlit)
    p.start()
    
    try:
        webview.create_window(
            "Система диагностики QDA", 
            "http://localhost:8501", 
            width=1200, 
            height=850
        )
        webview.start()
    finally:
        p.terminate()
        p.join()
