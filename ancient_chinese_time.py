import tkinter as tk

window = tk.Tk()
window.title('古代時間換算')
window.geometry('800x600')
window.configure(background='#FF8099')

def get_time():
    hour = int(hour_entry.get())
    minute = int(minute_entry.get())
    if hour > 24 or hour < 1:
        result = '時間有誤，請重新輸入'
        result_label.configure(text=result)
    if minute > 59 or minute < 0:
        result = '分鐘有誤，請重新輸入' 
        result_label.configure(text=result)
    else:
        result = '時間：{}時 {}分 , 古時說法是：{}{}'.format(hour, minute, hour_description(hour),minute_description(minute))
        result_label.configure(text=result)


def hour_description(hour):  
    if hour == 23:
      return '子初'
    elif hour == 24:
      return '子正'
    elif hour == 1:
      return '丑初'
    elif hour == 2:
      return '丑正'
    elif hour == 3:
      return '寅初'
    elif hour == 4:
      return '寅正'
    elif hour == 5:
      return '卯初'
    elif hour == 6:
      return '卯正'
    elif hour == 7:
      return '辰初'
    elif hour == 8:
      return '辰正'
    elif hour == 9:
      return '巳初'
    elif hour == 10:
      return '巳正'
    elif hour == 11:
      return '午初'
    elif hour == 12:
      return '午正'
    elif hour == 13:
      return '未初'
    elif hour == 14:
      return '未正'
    elif hour == 15:
      return '申初'
    elif hour == 16:
      return '申正'
    elif hour == 17:
      return '酉初'
    elif hour == 18:
      return '酉正'
    elif hour == 19:
      return '戌初'
    elif hour == 20:
      return '戌正'
    elif hour == 21:
      return '亥初'
    elif hour == 22:
      return '亥正'


def minute_description(minute):
    if minute < 15:
        return ' '
    elif minute >= 15 and minute < 30:
        return '一刻'
    elif minute >= 30 and minute < 45:
        return '二刻'
    elif minute >= 45 and minute <= 59:
        return '三刻'


header_label = tk.Label(window, text='古代時間換算(24HR制)')
header_label.pack()

hour_frame = tk.Frame(window)
hour_frame.pack(side=tk.TOP)
hour_label = tk.Label(hour_frame, text='時(幾點)')
hour_label.pack(side=tk.LEFT)
hour_entry = tk.Entry(hour_frame)
hour_entry.pack(side=tk.LEFT)

minute_frame = tk.Frame(window)
minute_frame.pack(side=tk.TOP)
minute_label = tk.Label(minute_frame, text='分(幾分)')
minute_label.pack(side=tk.LEFT)
minute_entry = tk.Entry(minute_frame)
minute_entry.pack(side=tk.LEFT)

result_label = tk.Label(window)
result_label.pack()

calculate_btn = tk.Button(window, text='開始換算', command=get_time)
calculate_btn.pack()

window.mainloop()