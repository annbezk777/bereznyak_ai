#!/usr/bin/env python3
"""
Генератор профессиональной PDF презентации для Bereznyak AI
"""

from reportlab.lib.pagesizes import landscape, A4
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, white, black
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# Размеры страницы
PAGE_WIDTH, PAGE_HEIGHT = landscape(A4)

# Цветовая схема
BLUE_PRIMARY = HexColor('#1e40af')
BLUE_LIGHT = HexColor('#3b82f6')
BLUE_LIGHTER = HexColor('#eff6ff')
GRAY_DARK = HexColor('#1e293b')
GRAY_LIGHT = HexColor('#64748b')
GREEN = HexColor('#16a34a')
RED = HexColor('#dc2626')
YELLOW = HexColor('#eab308')

def draw_cover(c):
    """Слайд 1: Обложка"""
    # Градиентный фон (симуляция через прямоугольники)
    c.setFillColor(BLUE_PRIMARY)
    c.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, fill=1, stroke=0)

    # Заголовок
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 72)
    c.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT*0.65, "BEREZNYAK AI")

    c.setFont("Helvetica-Bold", 36)
    c.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT*0.55, "Боты-калькуляторы")
    c.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT*0.48, "для автоматизации продаж")

    # Тэглайн
    c.setFont("Helvetica", 28)
    c.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT*0.35, "Превращаем сложные расчёты")
    c.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT*0.29, "в 2 минуты диалога")

    # Контакты
    c.setFont("Helvetica", 20)
    y = PAGE_HEIGHT*0.15
    c.drawCentredString(PAGE_WIDTH/2, y, "hello@bezk.pro  •  +7 (931) 287-79-10")
    c.drawCentredString(PAGE_WIDTH/2, y-30, "bereznyak-ai.ru  •  @ann_bezk")

def draw_problem(c):
    """Слайд 2: Проблема"""
    c.setFillColor(white)
    c.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, fill=1, stroke=0)

    # Заголовок
    c.setFillColor(RED)
    c.setFont("Helvetica-Bold", 56)
    c.drawString(60, PAGE_HEIGHT - 100, "ПРОБЛЕМА")

    # Большая цифра
    c.setFont("Helvetica-Bold", 120)
    c.setFillColor(RED)
    c.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT - 280, "30-40%")

    c.setFont("Helvetica-Bold", 36)
    c.setFillColor(GRAY_DARK)
    c.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT - 340, "лидов теряется")
    c.setFont("Helvetica", 28)
    c.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT - 380, "из-за долгого ответа")

    # Блоки проблем
    y = PAGE_HEIGHT - 480
    c.setFont("Helvetica-Bold", 24)
    c.setFillColor(GRAY_DARK)

    problems = [
        "Расчёт занимает 20-40 минут",
        "Ошибки в расчётах",
        "Менеджеры перегружены рутиной"
    ]

    for problem in problems:
        c.setFillColor(HexColor('#fef2f2'))
        c.rect(80, y-10, PAGE_WIDTH-160, 50, fill=1, stroke=0)
        c.setFillColor(RED)
        c.circle(120, y+15, 8, fill=1, stroke=0)
        c.setFillColor(GRAY_DARK)
        c.setFont("Helvetica", 22)
        c.drawString(150, y+5, problem)
        y -= 70

def draw_solution(c):
    """Слайд 3: Решение"""
    c.setFillColor(white)
    c.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, fill=1, stroke=0)

    # Заголовок
    c.setFillColor(GREEN)
    c.setFont("Helvetica-Bold", 56)
    c.drawString(60, PAGE_HEIGHT - 100, "РЕШЕНИЕ")

    # Центральный блок
    c.setFillColor(BLUE_LIGHTER)
    c.rect(100, PAGE_HEIGHT - 400, PAGE_WIDTH-200, 220, fill=1, stroke=0)

    c.setFillColor(BLUE_PRIMARY)
    c.setFont("Helvetica-Bold", 44)
    c.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT - 240, "БОТ-КАЛЬКУЛЯТОР")
    c.setFont("Helvetica", 28)
    c.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT - 280, "Автоматический расчёт за 90 секунд")

    # 4 блока преимуществ
    y = PAGE_HEIGHT - 470
    boxes = [
        ("5-7 вопросов", "клиенту"),
        ("90 секунд", "на расчёт"),
        ("PDF-смета", "на почту"),
        ("Лид в CRM", "автоматически")
    ]

    box_width = (PAGE_WIDTH - 160) / 4 - 20
    x = 80

    for num, desc in boxes:
        c.setFillColor(HexColor('#f0fdf4'))
        c.rect(x, y, box_width, 100, fill=1, stroke=0)
        c.setFillColor(GREEN)
        c.setFont("Helvetica-Bold", 32)
        c.drawCentredString(x + box_width/2, y+60, num)
        c.setFillColor(GRAY_DARK)
        c.setFont("Helvetica", 18)
        c.drawCentredString(x + box_width/2, y+30, desc)
        x += box_width + 20

def draw_pricing_lite(c):
    """Слайд 4: Тариф LITE"""
    c.setFillColor(white)
    c.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, fill=1, stroke=0)

    # Заголовок
    c.setFillColor(BLUE_PRIMARY)
    c.setFont("Helvetica-Bold", 48)
    c.drawString(60, PAGE_HEIGHT - 90, "ТАРИФ LITE")

    # Цена
    c.setFont("Helvetica-Bold", 80)
    c.setFillColor(BLUE_PRIMARY)
    c.drawString(60, PAGE_HEIGHT - 200, "45-60K ₽")
    c.setFont("Helvetica", 32)
    c.setFillColor(GRAY_LIGHT)
    c.drawString(400, PAGE_HEIGHT - 185, "7-10 дней")

    # Что входит
    y = PAGE_HEIGHT - 280
    c.setFont("Helvetica-Bold", 28)
    c.setFillColor(GRAY_DARK)
    c.drawString(60, y, "Что входит:")

    y -= 50
    features = [
        "Простая логика расчёта (2-3 параметра)",
        "Отправка результата в Telegram",
        "Уведомление менеджеру",
        "Базовая аналитика",
        "Гарантия 3 месяца"
    ]

    c.setFont("Helvetica", 22)
    for feature in features:
        c.setFillColor(GREEN)
        c.setFont("Helvetica-Bold", 24)
        c.drawString(80, y, "✓")
        c.setFillColor(GRAY_DARK)
        c.setFont("Helvetica", 22)
        c.drawString(120, y, feature)
        y -= 40

    # Для кого
    c.setFillColor(BLUE_LIGHTER)
    c.rect(60, 80, 350, 120, fill=1, stroke=0)
    c.setFillColor(BLUE_PRIMARY)
    c.setFont("Helvetica-Bold", 24)
    c.drawString(80, 170, "Для кого:")
    c.setFillColor(GRAY_DARK)
    c.setFont("Helvetica", 20)
    c.drawString(80, 135, "• Небольшой бизнес")
    c.drawString(80, 105, "• До 50 заявок/месяц")

    # Пример
    c.setFillColor(HexColor('#fef3c7'))
    c.rect(PAGE_WIDTH-470, 80, 410, 120, fill=1, stroke=0)
    c.setFillColor(YELLOW)
    c.setFont("Helvetica-Bold", 24)
    c.drawString(PAGE_WIDTH-450, 170, "Пример:")
    c.setFillColor(GRAY_DARK)
    c.setFont("Helvetica", 20)
    c.drawString(PAGE_WIDTH-450, 125, "Расчёт доставки по городу")
    c.drawString(PAGE_WIDTH-450, 95, "(вес + расстояние)")

def draw_pricing_pro(c):
    """Слайд 5: Тариф PRO"""
    c.setFillColor(white)
    c.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, fill=1, stroke=0)

    # Заголовок
    c.setFillColor(BLUE_PRIMARY)
    c.setFont("Helvetica-Bold", 48)
    c.drawString(60, PAGE_HEIGHT - 90, "ТАРИФ PRO")
    c.setFillColor(YELLOW)
    c.circle(420, PAGE_HEIGHT - 65, 15, fill=1, stroke=0)
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 14)
    c.drawCentredString(420, PAGE_HEIGHT - 72, "HIT")

    # Цена
    c.setFont("Helvetica-Bold", 80)
    c.setFillColor(BLUE_PRIMARY)
    c.drawString(60, PAGE_HEIGHT - 200, "120-180K ₽")
    c.setFont("Helvetica", 32)
    c.setFillColor(GRAY_LIGHT)
    c.drawString(520, PAGE_HEIGHT - 185, "14-21 день")

    # Что входит
    y = PAGE_HEIGHT - 280
    c.setFont("Helvetica-Bold", 28)
    c.setFillColor(GRAY_DARK)
    c.drawString(60, y, "Что входит:")

    y -= 50
    features = [
        "Сложная логика расчёта (4-7 параметров)",
        "Генерация PDF-сметы с печатью",
        "Интеграция с CRM (AmoCRM/Bitrix24)",
        "Панель управления для изменения цен",
        "Аналитика и отчёты",
        "Гарантия 3 месяца"
    ]

    c.setFont("Helvetica", 22)
    for feature in features:
        c.setFillColor(GREEN)
        c.setFont("Helvetica-Bold", 24)
        c.drawString(80, y, "✓")
        c.setFillColor(GRAY_DARK)
        c.setFont("Helvetica", 22)
        c.drawString(120, y, feature)
        y -= 36

    # Для кого
    c.setFillColor(BLUE_LIGHTER)
    c.rect(60, 60, 350, 120, fill=1, stroke=0)
    c.setFillColor(BLUE_PRIMARY)
    c.setFont("Helvetica-Bold", 24)
    c.drawString(80, 150, "Для кого:")
    c.setFillColor(GRAY_DARK)
    c.setFont("Helvetica", 20)
    c.drawString(80, 115, "• Средний бизнес")
    c.drawString(80, 85, "• 50-200 заявок/месяц")

    # Пример
    c.setFillColor(HexColor('#fef3c7'))
    c.rect(PAGE_WIDTH-510, 60, 450, 120, fill=1, stroke=0)
    c.setFillColor(YELLOW)
    c.setFont("Helvetica-Bold", 24)
    c.drawString(PAGE_WIDTH-490, 150, "Пример:")
    c.setFillColor(GRAY_DARK)
    c.setFont("Helvetica", 19)
    c.drawString(PAGE_WIDTH-490, 115, "Международная логистика")
    c.drawString(PAGE_WIDTH-490, 85, "(вес + маршрут + таможня + НДС)")

def draw_roi(c):
    """Слайд 6: ROI"""
    c.setFillColor(white)
    c.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, fill=1, stroke=0)

    # Заголовок
    c.setFillColor(BLUE_PRIMARY)
    c.setFont("Helvetica-Bold", 56)
    c.drawString(60, PAGE_HEIGHT - 100, "ЭКОНОМИКА")

    # Большая цифра ROI
    c.setFont("Helvetica-Bold", 140)
    c.setFillColor(GREEN)
    c.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT - 260, "5 МЕС")
    c.setFont("Helvetica", 36)
    c.setFillColor(GRAY_DARK)
    c.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT - 310, "срок окупаемости")

    # ДО и ПОСЛЕ
    y = PAGE_HEIGHT - 420
    box_width = (PAGE_WIDTH - 180) / 2

    # ДО
    c.setFillColor(HexColor('#fef2f2'))
    c.rect(60, y-150, box_width, 150, fill=1, stroke=0)
    c.setFillColor(RED)
    c.setFont("Helvetica-Bold", 32)
    c.drawString(90, y-30, "❌ ДО")
    c.setFillColor(GRAY_DARK)
    c.setFont("Helvetica", 22)
    c.drawString(90, y-70, "Менеджер: 30 мин на расчёт")
    c.drawString(90, y-100, "Затраты: 36 000₽/мес")
    c.setFont("Helvetica-Bold", 26)
    c.setFillColor(RED)
    c.drawString(90, y-135, "= 432 000₽/год")

    # ПОСЛЕ
    c.setFillColor(HexColor('#f0fdf4'))
    c.rect(60 + box_width + 20, y-150, box_width, 150, fill=1, stroke=0)
    c.setFillColor(GREEN)
    c.setFont("Helvetica-Bold", 32)
    c.drawString(90 + box_width + 20, y-30, "✓ ПОСЛЕ")
    c.setFillColor(GRAY_DARK)
    c.setFont("Helvetica", 22)
    c.drawString(90 + box_width + 20, y-70, "Бот: 2 минуты автоматически")
    c.drawString(90 + box_width + 20, y-100, "Затраты: 0₽/расчёт")
    c.setFont("Helvetica-Bold", 26)
    c.setFillColor(GREEN)
    c.drawString(90 + box_width + 20, y-135, "= 432 000₽ экономия")

    # Бонусы
    c.setFillColor(BLUE_LIGHTER)
    c.rect(60, 60, PAGE_WIDTH-120, 80, fill=1, stroke=0)
    c.setFillColor(BLUE_PRIMARY)
    c.setFont("Helvetica-Bold", 24)
    c.drawCentredString(PAGE_WIDTH/2, 110, "+ Рост конверсии на 40%  •  Работа 24/7  •  Репутация")

def draw_case_study(c):
    """Слайд 7: Кейс"""
    c.setFillColor(white)
    c.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, fill=1, stroke=0)

    # Заголовок
    c.setFillColor(BLUE_PRIMARY)
    c.setFont("Helvetica-Bold", 56)
    c.drawString(60, PAGE_HEIGHT - 100, "КЕЙС: PRIME SHIFT")
    c.setFont("Helvetica", 28)
    c.setFillColor(GRAY_LIGHT)
    c.drawString(60, PAGE_HEIGHT - 140, "Международная логистика")

    # Результаты в 4 блоках
    y = PAGE_HEIGHT - 240
    results = [
        ("20x", "быстрее", "40 мин → 2 мин"),
        ("+87%", "конверсии", "15% → 28%"),
        ("126 ч", "экономия", "в месяц"),
        ("4 мес", "окупаемость", "ROI")
    ]

    box_width = (PAGE_WIDTH - 200) / 4
    x = 60

    for big_num, label, desc in results:
        c.setFillColor(BLUE_LIGHTER)
        c.rect(x, y-180, box_width-10, 180, fill=1, stroke=0)

        c.setFillColor(BLUE_PRIMARY)
        c.setFont("Helvetica-Bold", 56)
        c.drawCentredString(x + (box_width-10)/2, y-50, big_num)

        c.setFillColor(GRAY_DARK)
        c.setFont("Helvetica-Bold", 22)
        c.drawCentredString(x + (box_width-10)/2, y-85, label)

        c.setFont("Helvetica", 16)
        c.setFillColor(GRAY_LIGHT)
        c.drawCentredString(x + (box_width-10)/2, y-110, desc)

        x += box_width + 10

    # Отзыв
    c.setFillColor(HexColor('#f8fafc'))
    c.rect(60, 60, PAGE_WIDTH-120, 180, fill=1, stroke=0)

    c.setFillColor(GRAY_DARK)
    c.setFont("Helvetica-Oblique", 22)
    text = '"До внедрения бота мы теряли каждого третьего клиента'
    c.drawString(90, 200, text)
    text2 = 'из-за долгого ответа. Теперь расчёт приходит за 90 секунд,'
    c.drawString(90, 170, text2)
    text3 = 'и конверсия выросла почти в 2 раза."'
    c.drawString(90, 140, text3)

    c.setFont("Helvetica-Bold", 20)
    c.setFillColor(BLUE_PRIMARY)
    c.drawString(90, 100, "— Алексей К., коммерческий директор")

def draw_objections(c):
    """Слайд 8: Возражения"""
    c.setFillColor(white)
    c.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, fill=1, stroke=0)

    # Заголовок
    c.setFillColor(BLUE_PRIMARY)
    c.setFont("Helvetica-Bold", 56)
    c.drawString(60, PAGE_HEIGHT - 100, "ВОЗРАЖЕНИЯ")

    # 3 возражения
    y = PAGE_HEIGHT - 190
    objections = [
        ("❓ Это дорого", "Окупается за 5-6 месяцев. Дальше — чистая экономия", GREEN),
        ("❓ У нас есть калькулятор", "Наш работает в мессенджерах. Конверсия на 40% выше", BLUE_PRIMARY),
        ("❓ Слишком сложно", "Если менеджер может посчитать — мы можем автоматизировать", YELLOW)
    ]

    for question, answer, color in objections:
        # Вопрос
        c.setFillColor(HexColor('#fef2f2'))
        c.rect(60, y-80, PAGE_WIDTH-120, 35, fill=1, stroke=0)
        c.setFillColor(RED)
        c.setFont("Helvetica-Bold", 24)
        c.drawString(80, y-70, question)

        # Ответ
        c.setFillColor(HexColor('#f0fdf4'))
        c.rect(60, y-140, PAGE_WIDTH-120, 55, fill=1, stroke=0)
        c.setFillColor(color)
        c.setFont("Helvetica-Bold", 20)
        c.drawString(80, y-110, "✓ " + answer)

        y -= 160

def draw_steps(c):
    """Слайд 9: Этапы"""
    c.setFillColor(white)
    c.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, fill=1, stroke=0)

    # Заголовок
    c.setFillColor(BLUE_PRIMARY)
    c.setFont("Helvetica-Bold", 56)
    c.drawString(60, PAGE_HEIGHT - 100, "ЭТАПЫ РАБОТЫ")

    # 5 этапов
    steps = [
        ("1", "АНАЛИЗ", "1-2 дня", "ТЗ и смета"),
        ("2", "ПРОТОТИП", "3-5 дней", "Тестовая версия"),
        ("3", "РАЗРАБОТКА", "7-14 дней", "Готовый бот"),
        ("4", "ТЕСТИРОВАНИЕ", "2-3 дня", "Проверка"),
        ("5", "ЗАПУСК", "1 день", "Production")
    ]

    y = PAGE_HEIGHT - 200
    box_width = (PAGE_WIDTH - 160) / 5 - 15
    x = 60

    for num, title, time, result in steps:
        # Номер
        c.setFillColor(BLUE_PRIMARY)
        c.circle(x + box_width/2, y, 25, fill=1, stroke=0)
        c.setFillColor(white)
        c.setFont("Helvetica-Bold", 28)
        c.drawCentredString(x + box_width/2, y-10, num)

        # Заголовок
        c.setFillColor(GRAY_DARK)
        c.setFont("Helvetica-Bold", 20)
        c.drawCentredString(x + box_width/2, y-50, title)

        # Время
        c.setFillColor(GRAY_LIGHT)
        c.setFont("Helvetica", 16)
        c.drawCentredString(x + box_width/2, y-75, time)

        # Блок результата
        c.setFillColor(BLUE_LIGHTER)
        c.rect(x, y-130, box_width, 40, fill=1, stroke=0)
        c.setFillColor(BLUE_PRIMARY)
        c.setFont("Helvetica", 14)
        c.drawCentredString(x + box_width/2, y-115, result)

        # Стрелка
        if num != "5":
            c.setStrokeColor(GRAY_LIGHT)
            c.setLineWidth(2)
            c.line(x + box_width + 5, y, x + box_width + 10, y)

        x += box_width + 15

    # Гарантия внизу
    c.setFillColor(GREEN)
    c.rect(60, 60, PAGE_WIDTH-120, 80, fill=1, stroke=0)
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 36)
    c.drawCentredString(PAGE_WIDTH/2, 105, "✓ ГАРАНТИЯ 3-6 МЕСЯЦЕВ")

def draw_cold_call(c):
    """Слайд 10: Скрипт холодного звонка"""
    c.setFillColor(white)
    c.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, fill=1, stroke=0)

    # Заголовок
    c.setFillColor(BLUE_PRIMARY)
    c.setFont("Helvetica-Bold", 56)
    c.drawString(60, PAGE_HEIGHT - 100, "СКРИПТ ЗВОНКА")

    # 3 шага
    y = PAGE_HEIGHT - 190

    # Шаг 1
    c.setFillColor(BLUE_LIGHTER)
    c.rect(60, y-110, PAGE_WIDTH-120, 110, fill=1, stroke=0)
    c.setFillColor(BLUE_PRIMARY)
    c.setFont("Helvetica-Bold", 28)
    c.drawString(80, y-30, "1. ПРЕДСТАВЛЕНИЕ (15 сек)")
    c.setFillColor(GRAY_DARK)
    c.setFont("Helvetica", 20)
    c.drawString(80, y-65, '"Добрый день! Bereznyak AI. Мы автоматизируем расчёты для клиентов.')
    c.drawString(80, y-92, 'Вместо 30 минут — 2 минуты. У вас 2 минуты?"')

    y -= 140

    # Шаг 2
    c.setFillColor(BLUE_LIGHTER)
    c.rect(60, y-110, PAGE_WIDTH-120, 110, fill=1, stroke=0)
    c.setFillColor(BLUE_PRIMARY)
    c.setFont("Helvetica-Bold", 28)
    c.drawString(80, y-30, "2. КВАЛИФИКАЦИЯ (1 мин)")
    c.setFillColor(GRAY_DARK)
    c.setFont("Helvetica", 20)
    c.drawString(80, y-65, '"Клиенты часто запрашивают расчёт стоимости? Сколько заявок в месяц?')
    c.drawString(80, y-92, 'Сколько времени уходит на 1 расчёт?"')

    y -= 140

    # Шаг 3
    c.setFillColor(BLUE_LIGHTER)
    c.rect(60, y-110, PAGE_WIDTH-120, 110, fill=1, stroke=0)
    c.setFillColor(BLUE_PRIMARY)
    c.setFont("Helvetica-Bold", 28)
    c.drawString(80, y-30, "3. ЗАКРЫТИЕ (30 сек)")
    c.setFillColor(GRAY_DARK)
    c.setFont("Helvetica", 20)
    c.drawString(80, y-65, '"Пришлю ссылку на демо-бота. Попробуете, и обсудим')
    c.drawString(80, y-92, 'как внедрить у вас. Договорились на завтра?"')

def draw_contacts(c):
    """Слайд 11: Контакты"""
    c.setFillColor(BLUE_PRIMARY)
    c.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, fill=1, stroke=0)

    # Заголовок
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 72)
    c.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT*0.7, "КОНТАКТЫ")

    # Контакты
    c.setFont("Helvetica-Bold", 32)
    y = PAGE_HEIGHT*0.55
    contacts = [
        "📧  hello@bezk.pro",
        "📞  +7 (931) 287-79-10",
        "💬  @ann_bezk",
        "🌐  bereznyak-ai.ru"
    ]

    for contact in contacts:
        c.drawCentredString(PAGE_WIDTH/2, y, contact)
        y -= 55

    # Демо-бот
    c.setFillColor(HexColor('#ffffff'))
    c.setFillAlpha(0.2)
    c.rect(150, PAGE_HEIGHT*0.18, PAGE_WIDTH-300, 100, fill=1, stroke=0)
    c.setFillAlpha(1)
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 28)
    c.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT*0.23, "ДЕМО-БОТ (ЛОГИСТИКА)")
    c.setFont("Helvetica", 24)
    c.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT*0.19, "t.me/prime_shift_bot")

    # Призыв
    c.setFont("Helvetica-Bold", 48)
    c.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT*0.08, "УДАЧИ В ПРОДАЖАХ!")

def generate_presentation():
    """Генерация PDF презентации"""
    filename = "/Users/annabereznyak/Desktop/Все проекты/Bereznyak_ai/bereznyak_ai/Bereznyak_AI_Presentation.pdf"

    c = canvas.Canvas(filename, pagesize=landscape(A4))

    # Метаданные
    c.setTitle("Bereznyak AI - Презентация для продажников")
    c.setAuthor("Bereznyak AI")
    c.setSubject("Боты-калькуляторы для автоматизации продаж")

    # Генерация слайдов
    print("Генерация слайда 1: Обложка...")
    draw_cover(c)
    c.showPage()

    print("Генерация слайда 2: Проблема...")
    draw_problem(c)
    c.showPage()

    print("Генерация слайда 3: Решение...")
    draw_solution(c)
    c.showPage()

    print("Генерация слайда 4: Тариф LITE...")
    draw_pricing_lite(c)
    c.showPage()

    print("Генерация слайда 5: Тариф PRO...")
    draw_pricing_pro(c)
    c.showPage()

    print("Генерация слайда 6: ROI...")
    draw_roi(c)
    c.showPage()

    print("Генерация слайда 7: Кейс...")
    draw_case_study(c)
    c.showPage()

    print("Генерация слайда 8: Возражения...")
    draw_objections(c)
    c.showPage()

    print("Генерация слайда 9: Этапы...")
    draw_steps(c)
    c.showPage()

    print("Генерация слайда 10: Скрипт звонка...")
    draw_cold_call(c)
    c.showPage()

    print("Генерация слайда 11: Контакты...")
    draw_contacts(c)

    # Сохранение
    c.save()
    print(f"\n✅ Презентация сохранена: {filename}")
    print(f"📄 Количество слайдов: 11")
    print(f"📐 Формат: A4 Landscape")

if __name__ == "__main__":
    generate_presentation()
