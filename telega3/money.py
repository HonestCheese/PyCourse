import sqlite3
import datetime
import random
import string

class PlayerDatabase:
    def __init__(self, db_name='players.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS players (
                telegram_id INTEGER PRIMARY KEY,
                nickname TEXT UNIQUE,
                balance REAL DEFAULT 0,
                vip_until TEXT,
                referrer_id INTEGER,
                referral_earnings REAL DEFAULT 0,
                FOREIGN KEY(referrer_id) REFERENCES players(telegram_id)
            )
        ''')
        self.conn.commit()

    def get_referrer(self, user_id):
        self.cursor.execute('SELECT referrer_id FROM players WHERE telegram_id = ?', (user_id,))
        result = self.cursor.fetchone()
        return result[0] if result else None

    def register_player(self, telegram_id, nickname, referrer_id=None):
        try:
            self.cursor.execute('''
                INSERT INTO players (telegram_id, nickname, balance, vip_until, referrer_id)
                VALUES (?, ?, 0, NULL, ?)
            ''', (telegram_id, nickname, referrer_id))
            self.conn.commit()
            
            if referrer_id:
                self.add_balance(referrer_id, 100)  # Бонус за приглашённого
            return f"✅ Вы успешно зарегистрировались\nВаш ник: {nickname}"
        except sqlite3.IntegrityError:
            return "❌ Игрок с таким ником уже существует, попробуйте другой"
    def get_balance_info(self, telegram_id):
        self.cursor.execute('''
            SELECT balance FROM players WHERE telegram_id = ?
        ''', (telegram_id,))
        player_info = self.cursor.fetchone()
        balance = player_info
        print(balance)
        return int(balance[0])
    def add_referral(self, referrer_id, user_id):
        try:
            self.cursor.execute('SELECT telegram_id FROM players WHERE telegram_id = ?', (user_id,))
            if not self.cursor.fetchone():
                self.cursor.execute('''
                    UPDATE players SET referrer_id = ? WHERE telegram_id = ?
                ''', (referrer_id, user_id))
                self.conn.commit()
                return "Реферал успешно добавлен"
            else:
                return "Пользователь уже существует"
        except Exception as e:
            return f"Ошибка при добавлении реферала: {e}"
    
    def perform_transaction(self, telegram_id, amount):
        try:
            if self.get_balance_info(telegram_id) > 0:
                self.cursor.execute('''
                    UPDATE players SET balance = balance - ? WHERE telegram_id = ?
                ''', (amount, telegram_id))
                self.conn.commit()
                return "Баланс успешно обновлён"
            else:
                return "Нет денег"
                
        except Exception as e:
            return f"Ошибка при обновлении баланса: {e}"
    def add_balance(self, telegram_id, amount):
        try:
            self.cursor.execute('''
                UPDATE players SET balance = balance + ? WHERE telegram_id = ?
            ''', (amount, telegram_id))
            self.conn.commit()
            return "Баланс успешно обновлён"
        except Exception as e:
            return f"Ошибка при обновлении баланса: {e}"

    def get_player_info(self, telegram_id):
        self.cursor.execute('''
            SELECT nickname, balance, vip_until, referral_earnings FROM players WHERE telegram_id = ?
        ''', (telegram_id,))
        player_info = self.cursor.fetchone()
        print(player_info)
        if player_info:
            nickname, balance, vip_until_str, referral_earnings = player_info
            vip_status = "Обычный"
            if vip_until_str == 'навсегда':
                vip_status = "Premium 🎰"
            elif vip_until_str:
                try:
                    vip_until = datetime.datetime.fromisoformat(vip_until_str)
                    if vip_until > datetime.datetime.now():
                        vip_status = "Premium 🎰"
                except ValueError:
                    return {"error": "Ошибка в формате даты VIP-статуса"}

            self.cursor.execute('SELECT COUNT(*) FROM players WHERE referrer_id = ?', (telegram_id,))
            referral_count = self.cursor.fetchone()[0]

            return {
                "telegram_id": telegram_id,
                "nickname": nickname,
                "vip_status": vip_status,
                "balance": balance,
                "referral_count": referral_count,
                "referral_earnings": referral_earnings
            }
        else:
            return None

    def give_vip(self, telegram_id, duration):
        try:
            if duration == "Неделя - 100₽":
                vip_until = (datetime.datetime.now() + datetime.timedelta(weeks=1)).isoformat()
            elif duration == "Месяц - 200₽":
                vip_until = (datetime.datetime.now() + datetime.timedelta(days=30)).isoformat()
            elif duration == "Всегда - 300₽":
                vip_until = 'навсегда'
            else:
                return "Некорректная длительность"

            self.cursor.execute('UPDATE players SET vip_until = ? WHERE telegram_id = ?', (vip_until, telegram_id))
            self.conn.commit()
            
            if vip_until == 'навсегда':
                return "VIP-статус предоставлен навсегда"
            else:
                return f"VIP-статус предоставлен до {vip_until}"
        except Exception as e:
            return f"Ошибка при назначении VIP-статуса: {e}"

    def remove_vip(self, telegram_id):
        try:
            self.cursor.execute('UPDATE players SET vip_until = NULL WHERE telegram_id = ?', (telegram_id,))
            self.conn.commit()
            return "VIP-статус удален"
        except Exception as e:
            return f"Ошибка при удалении VIP-статуса: {e}"
    def give_vipmoney(self):
        self.cursor.execute('SELECT telegram_id, vip_until FROM players')
        players = self.cursor.fetchall()

        for telegram_id, vip_until in players:
            if vip_until:
                self.add_balance(telegram_id, 100)
    def check_vip_time(self):
        try:
            self.cursor.execute('SELECT telegram_id, vip_until FROM players')
            players = self.cursor.fetchall()

            for telegram_id, vip_until in players:
                if vip_until and vip_until != 'навсегда':
                    vip_until_date = datetime.datetime.fromisoformat(vip_until)
                    if vip_until_date <= datetime.datetime.now():
                        self.remove_vip(telegram_id)

            self.conn.commit()
        except Exception as e:
            return f"Ошибка при проверке времени VIP-статуса: {e}"

    def close(self):
        self.conn.close()
