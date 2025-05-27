import tkinter as tk

# 윈도우 생성 및 설정
window = tk.Tk() 
window.title('계산기')
window.geometry('350x500')

# 프레임 생성: upperFrame
upperFrame = tk.Frame(window, width=400, height=70)
upperFrame.pack(pady=40)

# 엔트리 생성 및 화면 표시
entry = tk.Entry(upperFrame, width=20, font=('Courier',18), borderwidth=5)
entry.pack()
entry.insert(0,'')     # entry.insert(0,'0')

# 프레임 생성: downFrame
downFrame = tk.Frame(window, width=400, height=100)
downFrame.pack(padx=10, pady=10)

# 버튼 리스트 객체 생성
buttonList = [
    'C', '+/-', '%', '/',
    '7', '8', '9', 'X',
    '4', '5', '6', '-',
    '1', '2', '3', '+',
    '0', '.', '=']

# 버튼 생성 및 격자 모양으로 배치
rowIndex, colIndex = 0, 0
for buttonText in buttonList :
    def process(t=buttonText):
        click(t)
    if buttonText in ['C', '+/-', '%']:    # 버튼 색깔(white) 지정: 'C', '+/-', '%'
        btn=tk.Button(downFrame, text=buttonText, padx=15, pady=10, width=2, font=('Courier',15), bg='white', command=process)
        btn.grid(row=rowIndex, column=colIndex, padx=5, pady=5)
    elif colIndex == 3:         # 버튼 색깔(orange) 지정: 연산자
        btn=tk.Button(downFrame, text=buttonText, padx=15, pady=10, width=2, font=('Courier',15), bg='orange', command=process)
        btn.grid(row=rowIndex, column=colIndex, padx=5, pady=5)
    elif buttonText=='0':       # 버튼 셀 병합(columnspan=2): '0'
        btn=tk.Button(downFrame, text=buttonText, padx=15, pady=10, width=8, font=('Courier',15), command=process)
        btn.grid(row=rowIndex, column=colIndex, columnspan=2, padx=5, pady=5)
        colIndex += 1
    else : 
        btn=tk.Button(downFrame, text=buttonText, padx=15, pady=10, width=2, font=('Courier',15), command=process)
        btn.grid(row=rowIndex, column=colIndex, padx=5, pady=5)
    colIndex += 1
    if colIndex > 3:
        rowIndex += 1
        colIndex = 0

# 버튼 이벤트 처리 함수 구현
def click(key):
    pass

window.mainloop()
