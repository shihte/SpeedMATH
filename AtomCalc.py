"""

開發者：羅盤 lwopan

開發日期：2025/02/18

版本：1.0.0
Python版本：3.12.4
Pipenv版本：24.3.1
Visual Studio Code版本：1.97.0

描述：計算化學式的原子量計算器

"""

import re

class AtomCalc:
    def __init__(self):
        # 初始化原子量字典
        self.AtomicMass = {
            'H': 1,      # Hydrogen
            'He': 4,     # Helium
            'Li': 7,     # Lithium
            'Be': 9,     # Beryllium
            'B': 11,     # Boron
            'C': 12,     # Carbon
            'N': 14,     # Nitrogen
            'O': 16,     # Oxygen
            'F': 19,     # Fluorine
            'Ne': 20,    # Neon
            'Na': 23,    # Sodium
            'Mg': 24,    # Magnesium
            'Al': 27,    # Aluminum
            'Si': 28,    # Silicon
            'P': 31,     # Phosphorus
            'S': 32,     # Sulfur
            'Cl': 35,    # Chlorine
            'Ar': 40,    # Argon
            'K': 39,     # Potassium
            'Ca': 40,    # Calcium
            'Sc': 45,    # Scandium
            'Ti': 48,    # Titanium
            'V': 51,     # Vanadium
            'Cr': 52,    # Chromium
            'Mn': 55,    # Manganese
            'Fe': 56,    # Iron
            'Co': 59,    # Cobalt
            'Ni': 59,    # Nickel
            'Cu': 64,    # Copper
            'Zn': 65,    # Zinc
            'Ga': 70,    # Gallium
            'Ge': 73,    # Germanium
            'As': 75,    # Arsenic
            'Se': 79,    # Selenium
            'Br': 80,    # Bromine
            'Kr': 84,    # Krypton
            'Rb': 85,    # Rubidium
            'Sr': 88,    # Strontium
            'Y': 89,     # Yttrium
            'Zr': 91,    # Zirconium
            'Nb': 93,    # Niobium
            'Mo': 96,    # Molybdenum
            'Tc': 98,    # Technetium
            'Ru': 101,   # Ruthenium
            'Rh': 103,   # Rhodium
            'Pd': 106,   # Palladium
            'Ag': 107,   # Silver
            'Cd': 112,   # Cadmium
            'In': 115,   # Indium
            'Sn': 119,   # Tin
            'Sb': 122,   # Antimony
            'Te': 128,   # Tellurium
            'I': 127,    # Iodine
            'Xe': 131,   # Xenon
            'Cs': 133,   # Cesium
            'Ba': 137,   # Barium
            'La': 139,   # Lanthanum
            'Ce': 140,   # Cerium
            'Pr': 141,   # Praseodymium
            'Nd': 144,   # Neodymium
            'Pm': 145,   # Promethium
            'Sm': 150,   # Samarium
            'Eu': 152,   # Europium
            'Gd': 157,   # Gadolinium
            'Tb': 159,   # Terbium
            'Dy': 163,   # Dysprosium
            'Ho': 165,   # Holmium
            'Er': 167,   # Erbium
            'Tm': 169,   # Thulium
            'Yb': 173,   # Ytterbium
            'Lu': 175,   # Lutetium
            'Hf': 178,   # Hafnium
            'Ta': 181,   # Tantalum
            'W': 184,    # Tungsten
            'Re': 186,   # Rhenium
            'Os': 190,   # Osmium
            'Ir': 192,   # Iridium
            'Pt': 195,   # Platinum
            'Au': 197,   # Gold
            'Hg': 201,   # Mercury
            'Tl': 204,   # Thallium
            'Pb': 207,   # Lead
            'Bi': 209,   # Bismuth
            'Po': 209,   # Polonium
            'At': 210,   # Astatine
            'Rn': 222,   # Radon
            'Fr': 223,   # Francium
            'Ra': 226,   # Radium
            'Ac': 227,   # Actinium
            'Th': 232,   # Thorium
            'Pa': 231,   # Protactinium
            'U': 238,    # Uranium
            'Np': 237,   # Neptunium
            'Pu': 244,   # Plutonium
            'Am': 243,   # Americium
            'Cm': 247,   # Curium
            'Bk': 247,   # Berkelium
            'Cf': 251,   # Californium
            'Es': 252,   # Einsteinium
            'Fm': 257,   # Fermium
            'Md': 258,   # Mendelevium
            'No': 259,   # Nobelium
            'Lr': 262,   # Lawrencium
            'Rf': 267,   # Rutherfordium
            'Db': 268,   # Dubnium
            'Sg': 269,   # Seaborgium
            'Bh': 270,   # Bohrium
            'Hs': 269,   # Hassium
            'Mt': 278,   # Meitnerium
            'Ds': 281,   # Darmstadtium
            'Rg': 282,   # Roentgenium
            'Cn': 285,   # Copernicium
            'Nh': 286,   # Nihonium
            'Fl': 289,   # Flerovium
            'Mc': 290,   # Moscovium
            'Lv': 293,   # Livermorium
            'Ts': 294,   # Tennessine
            'Og': 294    # Oganesson
        }
        
        # 初始化類別變數
        self.Q = ""            # 使用者輸入
        self.Element = []      # 元素符號列表
        self.INTelement = []   # 元素數量列表
        
        # 初始化錯誤訊息模板
        self.ERROR_TEMPLATE = """
╔════════════════════════ ERROR ════════════════════════╗
║ {error_msg}
║ 
║ 問題輸入: {input_value}
║ 問題位置: {position}
║ 
║ 如果您認為這是程式的問題，請回報給開發者：
║ 1. 截圖此錯誤信息
║ 2. 記錄您的輸入內容
╚═══════════════════════════════════════════════════════╝
"""

    def PrintError(self, error_msg, input_value, position):
        """打印格式化的錯誤信息"""
        print(self.ERROR_TEMPLATE.format(
            error_msg=error_msg,
            input_value=input_value,
            position=position
        ))

    def UserQuery(self):
        """接收使用者輸入"""
        print("\n範例輸入 碳酸鈣： Ca1/C1/O3 或 Ca/C/O3")
        self.Q = input("請輸入化學式：")
        return self.Q

    def CleanInput(self):
        """清理輸入字符串"""
        if not self.Q:
            self.PrintError("輸入不能為空", "<空>", "整個輸入")
            return False
        
        # 移除所有空格和特殊字符
        self.Q = re.sub(r'[^a-zA-Z0-9/]', '', self.Q)
        
        if not self.Q:
            self.PrintError("清理後的輸入為空", "<空>", "整個輸入")
            return False
        
        return True

    def SplitTheQ(self):
        """分析化學式"""
        # 先清理輸入
        if not self.CleanInput():
            return False

        # 分割化學式
        parts = self.Q.split("/")
        
        # 重置列表
        self.Element = []
        self.INTelement = []

        try:
            for idx, part in enumerate(parts):
                # 檢查部分是否為空
                if not part:
                    self.PrintError(
                        "分隔符號之間不能為空",
                        self.Q,
                        f"第 {idx+1} 個分隔區段"
                    )
                    return False

                # 分離元素和數字
                i = len(part)
                while i > 0 and part[i-1].isdigit():
                    i -= 1

                element = part[:i]
                number = part[i:] if i < len(part) else '1'

                # 檢查元素
                if element not in self.AtomicMass:
                    self.PrintError(
                        f"未知元素：{element}",
                        self.Q,
                        f"第 {idx+1} 個元素"
                    )
                    return False

                # 檢查數字
                try:
                    num = int(number)
                    if num <= 0:
                        self.PrintError(
                            "元素數量必須大於0",
                            f"{element}{number}",
                            f"第 {idx+1} 個元素的數量"
                        )
                        return False
                except ValueError:
                    self.PrintError(
                        "無效的數字格式",
                        number,
                        f"第 {idx+1} 個元素的數量部分"
                    )
                    return False

                # 添加到列表
                self.Element.append(element)
                self.INTelement.append(num)

            # 檢查重複元素
            seen_elements = set()
            for idx, elem in enumerate(self.Element):
                if elem in seen_elements:
                    self.PrintError(
                        f"元素重複出現：{elem}",
                        self.Q,
                        f"第 {idx+1} 個元素"
                    )
                    return False
                seen_elements.add(elem)

            return True

        except Exception as e:
            self.PrintError(
                f"未預期的錯誤：{str(e)}",
                self.Q,
                "解析過程中"
            )
            return False

    def CalculateMass(self):
        """計算總原子量"""
        if not self.Element or not self.INTelement:
            self.PrintError(
                "尚未輸入或解析化學式",
                "<空>",
                "無"
            )
            return False

        try:
            total_mass = 0
            print("\n計算結果:")
            
            # 計算並顯示每個元素的資訊
            for i in range(len(self.Element)):
                element = self.Element[i]
                count = self.INTelement[i]
                element_mass = self.AtomicMass[element]
                total_element_mass = element_mass * count
                total_mass += total_element_mass
                
                # 輸出格式：元素: 原子序 數值, 數量 數值, 原子量 數值
                print(f"{element}: 原子量 {element_mass}, 數量 {count}, 元素總原子量 {total_element_mass}")
            
            # 顯示總原子量
            print(f"\n分子總原子量: {total_mass:.3f}")
            return True

        except Exception as e:
            self.PrintError(
                f"計算原子量時發生錯誤：{str(e)}",
                str(self.Element),
                "計算過程"
            )
            return False

def main():
    """主程式"""
    calc = AtomCalc()
    while True:
        calc.UserQuery()
        if calc.SplitTheQ():
            calc.CalculateMass()
        
        # 詢問是否繼續
        cont = input("\n是否繼續？(y/n): ")
        if cont.lower() != 'y':
            break

    print("程式結束")

if __name__ == "__main__":
    main()