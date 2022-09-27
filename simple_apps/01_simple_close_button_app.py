# CLOSEボタンだけのシンプルなアプリ

# 公式ドキュメント
# https://www.pysimplegui.org/en/latest/readme%20Japanese/
# https://www.pysimplegui.org/en/latest/
# https://www.pysimplegui.org/en/latest/call%20reference/

# パッケージのインポート
import PySimpleGUI as sg

# ウィンドウのカラーテーマ設定
sg.theme("DefaultNoMoreNagging") 

# 部品を作成
## CLOSEボタン
close_button_element = sg.Button(
                                button_text="CLOSE",    # 表示するテキスト
                                button_color="blue",    # ボタンの色
                                size=(10,3),            # サイズ
                                key="CLOSE"             # キー：イベントの判定に必要
                                )

# アプリのレイアウトを設定，部品を2次元配列で配置
layout = [[close_button_element]]

# ウィンドウを設定
window = sg.Window(
                    title="My App",  # ウィンドウのタイトル
                    layout=layout,              # レイアウト
                    size=(300, 300)             # ウィンドウの大きさ
                    )

# 無限ループ
while True:
    
    # アプリ内で発生したイベントを読み取る
    event, values = window.read(timeout=20)
    
    # アプリの終了判定，CLOSEボタンが押される，または×ボタンが押される
    if event == "CLOSE" or event == sg.WIN_CLOSED:
        break

# アプリを終了（ウィンドウを閉じる）
window.close()