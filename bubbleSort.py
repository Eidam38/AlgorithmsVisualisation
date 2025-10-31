import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

COLOR_BASE: str = "green"
COLOR_COMPARE: str = "orange"
COLOR_SWAP: str = "red"

class Frame:
    def __init__(self, values: list[int], colors: list[str]) -> None:
        self.values = values
        self.colors = colors       

def _snapshot(frames: list[Frame], lst: list[int],
              idxs: list[int] = None,
              color: str = COLOR_BASE) -> None:
    colors = [COLOR_BASE] * len(lst)
    if idxs:
        for k in idxs:
            colors[k] = color
    frames.append(Frame(lst.copy(), colors))

def bubbleSort(list_to_sort: list[int], frames: list[Frame]) -> list[int]:
    sorted_flag: bool = False
    list_length: int = len(list_to_sort) - 1
    while not sorted_flag:
        sorted_flag = True
        for i in range(list_length):
            if frames is not None:
                _snapshot(frames, list_to_sort, [i, i + 1], COLOR_COMPARE)

            if list_to_sort[i] > list_to_sort[i + 1]:
                list_to_sort[i], list_to_sort[i + 1] = list_to_sort[i + 1], list_to_sort[i]
                sorted_flag = False
                list_length = i + 1
                _snapshot(frames, list_to_sort, [i, i + 1], COLOR_SWAP)


    
    _snapshot(frames, list_to_sort)
    return list_to_sort

def animate_bubble_sort(frames: list[Frame], interval: int, repeat: bool = False):
    fig, ax = plt.subplots()

    n = len(frames[0].values)          
    x = list(range(len(frames[0].values)))
    bars = ax.bar(x, frames[0].values, color=COLOR_BASE)
    ax.set_title("Bubble Sort Visualization")
    ax.set_xlim(-0.5, len(x) - 0.5)
    ax.set_ylim(0, max(max(f.values) for f in frames) * 1.1)
    ax.set_xticks(range(n))        
    ax.set_xticklabels(range(n))    
    ax.yaxis.set_visible(False)
    ax.set_yticks([])
    for side in ("left", "right", "top"):
        ax.spines[side].set_visible(False)

    texts = []
    for rect, val in zip(bars, frames[0].values):
        x = rect.get_x() + rect.get_width() / 2
        y = rect.get_height()
        t = ax.text(x, y, f"{val}", ha="center", va="bottom", fontsize=9)
        texts.append(t)

    def update(frame: Frame):
        for rect, val, col, txt in zip(bars, frame.values, frame.colors, texts):
            rect.set_height(val)
            rect.set_color(col)
            txt.set_y(val)
            txt.set_text(f"{val}")
        return list(bars) + texts   

    anim = FuncAnimation(fig, update, frames=frames, interval=interval, blit=False, repeat=repeat)
    plt.show()

if __name__ == "__main__":
    random_list: list[int] = np.random.randint(1, 100, size=30)
    #test_list: list[int] = [0, 1, 2, 3, 4, 6, 7, 5, 8, 9, 10, 11, 12, 13, 15, 14, 16, 17, 18, 19, 20]

    frames: list[Frame] = []
    sorted_list = bubbleSort(random_list.copy(), frames=frames)

    animate_bubble_sort(frames, interval=100)





