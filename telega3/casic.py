import random
import money

db = money.PlayerDatabase()

class Crash:
    @staticmethod
    def crash(money, stavka, user):
        # Определяем диапазоны и соответствующие им вероятности
        ranges = [   
            (0.00, 0.00),   
            (1.00, 2.00),
            (2.01, 3.50),
            (3.51, 5.00),
            (5.01, 10.00),
            (10.01, 25.00),
            (25.01, 50.00),
            (50.01, 250.00),
            (250.01, 500.00),
            (500.01, 1000.00)
        ]
        
        probabilities = [1,60, 15, 10, 2, 2, 2, 1, 1, 1]

        probabilities = [p / 100 for p in probabilities]

        cumulative_probabilities = []
        cumulative_sum = 0
        for p in probabilities:
            cumulative_sum += p
            cumulative_probabilities.append(cumulative_sum)
        
        def simulate_x():
            rnd = random.random()
            for i, cumulative_probability in enumerate(cumulative_probabilities):
                if rnd <= cumulative_probability:
                    selected_range = ranges[i]
                    return random.uniform(*selected_range)
            # Этот случай никогда не должен произойти, если вероятности правильно заданы
        if money < 1:
            return "Минимальная ставка в монетах 1 💲"
        if db.get_balance_info(user) >= money:
            x = simulate_x()
            if x is not None:
                # Ваш код, который выполняется, если x >= stavka

                if x >= stavka:
                    m = money*stavka
                    db.add_balance(user,(m-money))
                    return f"✅ВАША СТАВКА УДАЧНАЯ✅\n✅Ставка - {money} 💲 - x{stavka:.2f}✅\nЛЕТЕЛО ДО🚀 : {x:.2f}\nВЫИГРЫШ : {m} 💲"
                else:
                    db.perform_transaction(user, money)
                    return f"❌ВАША СТАВКА НЕУДАЧНАЯ❌\n❌Ставка - {money} 💲 - x{stavka:.2f}❌\nЛЕТЕЛО ДО🚀 : {x:.2f}"
            else: 
                return f"Ошибка средства не были забраны"
        else:
            return f"Недостаточно средств"

class Randomgame:
    def __init__(self) -> None:
        pass
    def game(self, userid, money, stavka):
        randomchic = random.randint(1,6)
        if db.get_balance_info(userid) >= money:
            if stavka == "1-3" and randomchic <= 3:
                m = (money*5) - money
                db.add_balance(userid,(m))
                return f"✅ВАША СТАВКА УДАЧНАЯ✅\n✅Ставка - {money} 💲 - На половину 1-3✅\nВЫИГРЫШ : {m} 💲"
            elif stavka == "3-6" and randomchic >= 3:
                m = (money*5) - money
                db.add_balance(userid,(m))
                return f"✅ВАША СТАВКА УДАЧНАЯ✅\n✅Ставка - {money} 💲 - На половину 3-6✅\nВЫИГРЫШ : {m} 💲"
            elif stavka == "polovinka1" and randomchic >= 3:
                db.perform_transaction(userid, 20)
                return f"❌ВАША СТАВКА НЕУДАЧНАЯ❌\n❌Ставка - {money} 💲 - На половину 1-3❌"
            elif stavka == "polovinka2" and randomchic <= 3:
                db.perform_transaction(userid, money)
                return f"❌ВАША СТАВКА НЕУДАЧНАЯ❌\n❌Ставка - {money} 💲 - На половину 3-6❌"
            if str(stavka) == str(randomchic):
                m = (money*1.80) - money
                db.add_balance(userid,(m))
                return f"✅ВАША СТАВКА УДАЧНАЯ✅\n✅Ставка - {money} 💲 - На Одно из чисел✅\nВЫИГРЫШ : {m} 💲"
            else:
                db.perform_transaction(userid, money)
                return f"❌ВАША СТАВКА НЕУДАЧНАЯ❌\n❌Ставка - {money} 💲 - На Одно из чисел❌"
        else:
            return f"Недостаточно средств"

class Slotsgame:
    def __init__(self, slot=5):
        self.slot_num = slot
        self.result = []
        self.slots = {
            "🍌": 1, "🍊": 1, "🍒": 1, "🍍": 1, "🍓": 1,
            "🥝": 1, "🍐": 1, "🍑": 1, "🍏": 1,
            "🍇": 2, "🥭": 2, "🍎": 2, "🍋": 2, "🍉": 2,
            "😺": 3, "💥": 3, "💯": 3, "💫": 3,
            "🔥": 4, "🎁": 4, "💵": 4,
            "🎰": 5
        }
        self.weights = {
            "🍌": 10, "🍊": 10, "🍒": 10, "🍍": 10, "🍓": 10,
            "🥝": 10, "🍐": 10, "🍑": 10, "🍏": 10,
            "🍇": 8, "🥭": 8, "🍎": 8, "🍋": 8, "🍉": 8,
            "😺": 5, "💥": 5, "💯": 5, "💫": 5,
            "🔥": 3, "🎁": 3, "💵": 3,
            "🎰": 1
        }
        self.payouts = {
            1: {3: 1.50, 4: 2.00, 5: 5.00},  # Обычные
            2: {3: 2.50, 4: 3.50, 5: 10.00},  # Редкие
            3: {2: 2.50, 3: 5.00, 4: 7.50, 5: 10.50},  # Сверхредкие
            4: {1: 5.00, 2: 7.50, 3: 10.50, 4: 25.00, 5: 100.00},  # Легендарные
            5: {1: 10.00, 2: 25.00, 3: 100.00, 4: 250.00, 5: 1000.00}  # Именные
        }

    def play(self, bet, user):
        self.result = random.choices(list(self.slots.keys()), weights=list(self.weights.values()), k=self.slot_num)
        sc = self.calculate_score(bet)
        if sc != 0:
            db.add_balance(user, int(sc))
            return f"✅ВЫ выйграли. Результат: |{'|'.join(self.result)}|\nВыигрыш: {int(sc)} 💲✅"
        else:
            return f"❌ВЫ проиграли. Результат: |{'|'.join(self.result)}❌"
    
    def calculate_score(self, bet):
        score = 0
        for emoji, rarity in self.slots.items():
            count = self.result.count(emoji)
            if count in self.payouts[rarity]:
                score += self.payouts[rarity][count] * bet
        return score

