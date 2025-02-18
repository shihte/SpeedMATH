import matplotlib.pyplot as plt
import numpy as np

class StatFreqAnalyzer:
    def __init__(self):
        self.list = []
        self.total = 0
        self.CFlist = []
        self.RFlist = []
        self.CRFlist = []
        self.start_x = 0  # 新增：x軸起始值
        self.bin_size = 0 # 新增：組距

    def inputList(self):
        input_str = input("Please enter list (You can do number separation by typing half &):")
        # 將輸入轉換為整數並排序
        self.list = sorted([int(x.strip()) for x in input_str.split("&") if x.strip().isdigit()])
        self.total = sum(self.list)

    def calculateCF(self):
        for i in range(len(self.list)):
            if i == 0:
                self.CFlist.append(self.list[i])
            else:
                self.CFlist.append(self.list[i] + self.CFlist[i-1])
    
    def calculateRF(self):
        for nowINT in self.list:
            # 計算百分比並四捨五入到5位小數
            percentage = round((nowINT / self.total) * 100, 5)
            self.RFlist.append(percentage)
    
    def calculateCRF(self):
        for nowINT in range(len(self.RFlist)):
            if nowINT == 0:
                self.CRFlist.append(self.RFlist[nowINT])
            else:
                self.CRFlist.append(self.RFlist[nowINT] + self.CRFlist[nowINT - 1])

    def output(self):
        print("原始數據 : ", end="")
        for NOWVariable in self.list:
            print(f"{NOWVariable}", end=" ")

        print("\n累積次數 : ", end="")
        for NOWVariable in self.CFlist:
            print(f"{NOWVariable}", end=" ")

        print("\n相對次數 : ", end="")
        for NOWVariable in self.RFlist:
            print(f"{NOWVariable}%", end=" ")

        print("\n累積相對次數 : ", end="")
        for NOWVariable in self.CRFlist:
            print(f"{NOWVariable}%", end=" ")

    def plot_graphs(self):
        self.bin_size = int(input("Enter bin size: "))
        
        # 自動計算起始值
        min_value = min(self.list)
        self.start_x = min_value - (min_value % self.bin_size)
        if self.start_x > 0:
            self.start_x -= self.bin_size
            
        # 計算x軸範圍
        max_value = max(self.list)
        num_bins = len(self.list)  # 修改這裡，確保有足夠的bins
        x_values = [self.start_x + i * self.bin_size for i in range(num_bins)]
        
        fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 8))
        plt.subplots_adjust(left=0.725)
        
        y_ticks = np.arange(0, 101, 20)
        
        # 確保有足夠的x軸標籤
        x_ticks = range(len(self.list))
        x_labels = [str(x_values[i]) for i in range(len(self.list))]
        
        # Cumulative Frequency
        ax1.plot(x_ticks, self.CFlist, marker='o')
        ax1.set_title('Cumulative Frequency')
        ax1.grid(True)
        ax1.set_ylim(0, max(self.CFlist) * 1.1)
        for i, v in enumerate(self.CFlist):
            ax1.text(i, v, f'{v}', ha='right', va='bottom')
        
        # Relative Frequency
        ax2.plot(x_ticks, self.RFlist, marker='o')
        ax2.set_title('Relative Frequency')
        ax2.set_yticks(y_ticks)
        ax2.grid(True)
        ax2.set_ylim(0, 100)
        for i, v in enumerate(self.RFlist):
            ax2.text(i, v, f'{v:.2f}%', ha='right', va='bottom')
        
        # Cumulative Relative Frequency
        ax3.plot(x_ticks, self.CRFlist, marker='o')
        ax3.set_title('Cumulative Relative Frequency')
        ax3.set_yticks(y_ticks)
        ax3.grid(True)
        ax3.set_ylim(0, 100)
        for i, v in enumerate(self.CRFlist):
            ax3.text(i, v, f'{v:.2f}%', ha='right', va='bottom')
        
        # 設置所有子圖的x軸
        for ax in [ax1, ax2, ax3]:
            ax.set_xticks(x_ticks)
            ax.set_xticklabels(x_labels)
            ax.set_xlabel('Original Data')
        
        plt.tight_layout(pad=1.5)
        plt.show()

def main():
    SFA = StatFreqAnalyzer()
    SFA.inputList()
    SFA.calculateCF()
    SFA.calculateRF()
    SFA.calculateCRF()
    SFA.output()
    SFA.plot_graphs()

if __name__ == "__main__":
    main()