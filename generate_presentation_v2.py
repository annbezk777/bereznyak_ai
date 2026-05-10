#!/usr/bin/env python3
"""
Генератор профессиональной PDF презентации для Bereznyak AI
Дизайн в стиле сайта с поддержкой кириллицы
"""

from reportlab.lib.pagesizes import landscape, A4
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, white, black
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# Регистрация шрифтов с поддержкой кириллицы
pdfmetrics.registerFont(TTFont('Arial', '/System/Library/Fonts/Supplemental/Arial.ttf'))
pdfmetrics.registerFont(TTFont('Arial-Bold', '/System/Library/Fonts/Supplemental/Arial Bold.ttf'))
pdfmetrics.registerFont(TTFont('Arial-Italic', '/System/Library/Fonts/Supplemental/Arial Italic.ttf'))
pdfmetrics.registerFont(TTFont('Arial-BoldItalic', '/System/Library/Fonts/Supplemental/Arial Bold Italic.ttf'))

# Размеры страницы
PAGE_WIDTH, PAGE_HEIGHT = landscape(A4)

# Цветовая схема в стиле сайта
DARK_BG = HexColor('#0f172a')  # slate-950
INDIGO_DARK = HexColor('#1e1b4b')  # indigo-950
BLUE_PRIMARY = HexColor('#3b82f6')  # blue-500
INDIGO_PRIMARY = HexColor('#6366f1')  # indigo-500
BLUE_LIGHT = HexColor('#60a5fa')  # blue-400
PURPLE = HexColor('#a855f7')  # purple-500
GRAY_DARK = HexColor('#1e293b')
GRAY_LIGHT = HexColor('#64748b')
GREEN = HexColor('#10b981')  # emerald-500
RED = HexColor('#ef4444')  # red-500
YELLOW = HexColor('#f59e0b')  # amber-500

def draw_gradient_bg(c, color1, color2):
    """Симуляция градиента через полосы"""
    steps = 50
    for i in range(steps):
        r = color1.red + (color2.red - color1.red) * i / steps
        g = color1.green + (color2.green - color1.green) * i / steps
        b = color1.blue + (color2.blue - color1.blue) * i / steps
        c.setFillColorRGB(r, g, b)
        c.rect(0, i * PAGE_HEIGHT / steps, PAGE_WIDTH, PAGE_HEIGHT / steps + 1, fill=1, stroke=0)

def draw_cover(c):
    """Слайд 1: Обложка в стиле сайта"""
    # Градиентный фон
    draw_gradient_bg(c, DARK_BG, INDIGO_DARK)

    # Светящиеся круги (как на сайте)
    c.setFillColorRGB(0.23, 0.51, 0.96, alpha=0.1)  # blue с прозрачностью
    c.circle(PAGE_WIDTH * 0.3, PAGE_HEIGHT * 0.7, 200, fill=1, stroke=0)

    c.setFillColorRGB(0.63, 0.39, 0.97, alpha=0.1)  # purple с прозрачностью
    c.circle(PAGE_WIDTH * 0.7, PAGE_HEIGHT * 0.3, 200, fill=1, stroke=0)

    # Заголовок
    c.setFillColor(white)
    c.setFont("Arial-Bold", 80)
    c.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT*0.65, "BEREZNYAK AI")

    c.setFont("Arial-Bold", 40)
    c.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT*0.55, "Боты-калькуляторы")
    c.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT*0.48, "для автоматизации продаж")

    # Тэглайн
    c.setFont("Arial", 30)
    c.setFillColorRGB(0.6, 0.7, 1, alpha=0.9)
    c.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT*0.35, "Превращаем сложные расчёты")
    c.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT*0.29, "в 2 минуты диалога")

    # Контакты в стеклянном блоке
    c.setFillColorRGB(1, 1, 1, alpha=0.1)
    c.roundRect(PAGE_WIDTH/2 - 250, PAGE_HEIGHT*0.08, 500, 120, 20, fill=1, stroke=0)

    c.setFillColor(white)
    c.setFont("Arial", 22)
    y = PAGE_HEIGHT*0.17
    c.drawCentredString(PAGE_WIDTH/2, y, "hello@bezk.pro  •  +7 (931) 287-79-10")
    c.drawCentredString(PAGE_WIDTH/2, y-35, "bereznyak-ai.ru  •  @ann_bezk")

def draw_problem(c):
    """Слайд 2: Проблема"""
    c.setFillColor(white)
    c.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, fill=1, stroke=0)

    # Заголовок
    c.setFillColor(RED)
    c.setFont("Arial-Bold", 60)
    c.drawString(60, PAGE_HEIGHT - 100, "ПРОБЛЕМА")

    # Большая цифра
    c.setFont("Arial-Bold", 140)
    c.setFillColor(RED)
    c.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT - 280, "30-40%")

    c.setFont("Arial-Bold", 40)
    c.setFillColor(GRAY_DARK)
    c.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT - 340, "лидов теряется")
    c.setFont("Arial", 32)
    c.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT - 385, "из-за долгого ответа")

    # Блоки проблем
    y = PAGE_HEIGHT - 480
    problems = [
        "Расчёт занимает 20-40 минут",
        "Ошибки в расчётах",
        "Менеджеры перегружены рутиной"
    ]

    for problem in problems:
        c.setFillColor(HexColor('#fef2f2'))
        c.roundRect(80, y-10, PAGE_WIDTH-160, 55, 12, fill=1, stroke=0)
        c.setFillColor(RED)
        c.circle(120, y+18, 10, fill=1, stroke=0)
        c.setFillColor(GRAY_DARK)
        c.setFont("Arial", 24)
        c.drawString(150, y+5, problem)
        y -= 75

def draw_solution(c):
    """Слайд 3: Решение"""
    c.setFillColor(white)
    c.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, fill=1, stroke=0)

    # Заголовок с градиентом (симуляция)
    c.setFillColor(GREEN)
    c.setFont("Arial-Bold", 60)
    c.drawString(60, PAGE_HEIGHT - 100, "РЕШЕНИЕ")

    # Центральный блок с градиентом
    c.setFillColor(HexColor('#eff6ff'))
    c.roundRect(100, PAGE_HEIGHT - 400, PAGE_WIDTH-200, 230, 16, fill=1, stroke=0)

    c.setFillColor(BLUE_PRIMARY)
    c.setFont("Arial-Bold", 48)
    c.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT - 235, "БОТ-КАЛЬКУЛЯТОР")
    c.setFont("Arial", 30)
    c.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT - 280, "Автоматический расчёт за 90 секунд")

    # 4 блока преимуществ
    y = PAGE_HEIGHT - 470
    boxes = [
        ("5-7", "вопросов"),
        ("90 сек", "расчёт"),
        ("PDF", "смета"),
        ("CRM", "интеграция")
    ]

    box_width = (PAGE_WIDTH - 160) / 4 - 20
    x = 80

    for num, desc in boxes:
        c.setFillColor(HexColor('#f0fdf4'))
        c.roundRect(x, y, box_width, 100, 12, fill=1, stroke=0)
        c.setFillColor(GREEN)
        c.setFont("Arial-Bold", 36)
        c.drawCentredString(x + box_width/2, y+60, num)
        c.setFillColor(GRAY_DARK)
        c.setFont("Arial", 20)
        c.drawCentredString(x + box_width/2, y+28, desc)
        x += box_width + 20

def draw_pricing_lite(c):
    """Слайд 4: Тариф LITE"""
    c.setFillColor(white)
    c.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, fill=1, stroke=0)

    # Заголовок
    c.setFillColor(BLUE_PRIMARY)
    c.setFont("Arial-Bold", 52)
    c.drawString(60, PAGE_HEIGHT - 90, "ТАРИФ LITE")

    # Цена
    c.setFont("Arial-Bold", 90)
    c.setFillColor(BLUE_PRIMARY)
    c.drawString(60, PAGE_HEIGHT - 200, "45-60K ₽")
    c.setFont("Arial", 36)
    c.setFillColor(GRAY_LIGHT)
    c.drawString(430, PAGE_HEIGHT - 185, "7-10 дней")

    # Что входит
    y = PAGE_HEIGHT - 280
    c.setFont("Arial-Bold", 30)
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

    for feature in features:
        c.setFillColor(GREEN)
        c.setFont("Arial-Bold", 28)
        c.drawString(80, y, "✓")
        c.setFillColor(GRAY_DARK)
        c.setFont("Arial", 24)
        c.drawString(120, y, feature)
        y -= 42

    # Для кого
    c.setFillColor(HexColor('#eff6ff'))
    c.roundRect(60, 70, 360, 130, 16, fill=1, stroke=0)
    c.setFillColor(BLUE_PRIMARY)
    c.setFont("Arial-Bold", 26)
    c.drawString(80, 170, "Для кого:")
    c.setFillColor(GRAY_DARK)
    c.setFont("Arial", 22)
    c.drawString(80, 135, "• Небольшой бизнес")
    c.drawString(80, 100, "• До 50 заявок/месяц")

    # Пример
    c.setFillColor(HexColor('#fef3c7'))
    c.roundRect(PAGE_WIDTH-480, 70, 420, 130, 16, fill=1, stroke=0)
    c.setFillColor(YELLOW)
    c.setFont("Arial-Bold", 26)
    c.drawString(PAGE_WIDTH-460, 170, "Пример:")
    c.setFillColor(GRAY_DARK)
    c.setFont("Arial", 22)
    c.drawString(PAGE_WIDTH-460, 125, "Расчёт доставки по городу")
    c.drawString(PAGE_WIDTH-460, 92, "(вес + расстояние)")

def draw_pricing_pro(c):
    """Слайд 5: Тариф PRO"""
    c.setFillColor(white)
    c.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, fill=1, stroke=0)

    # Заголовок с бейджем HIT
    c.setFillColor(BLUE_PRIMARY)
    c.setFont("Arial-Bold", 52)
    c.drawString(60, PAGE_HEIGHT - 90, "ТАРИФ PRO")

    c.setFillColor(YELLOW)
    c.circle(435, PAGE_HEIGHT - 65, 18, fill=1, stroke=0)
    c.setFillColor(white)
    c.setFont("Arial-Bold", 16)
    c.drawCentredString(435, PAGE_HEIGHT - 73, "HIT")

    # Цена
    c.setFont("Arial-Bold", 90)
    c.setFillColor(BLUE_PRIMARY)
    c.drawString(60, PAGE_HEIGHT - 200, "120-180K ₽")
    c.setFont("Arial", 36)
    c.setFillColor(GRAY_LIGHT)
    c.drawString(560, PAGE_HEIGHT - 185, "14-21 день")

    # Что входит
    y = PAGE_HEIGHT - 280
    c.setFont("Arial-Bold", 30)
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

    for feature in features:
        c.setFillColor(GREEN)
        c.setFont("Arial-Bold", 28)
        c.drawString(80, y, "✓")
        c.setFillColor(GRAY_DARK)
        c.setFont("Arial", 24)
        c.drawString(120, y, feature)
        y -= 38

    # Для кого
    c.setFillColor(HexColor('#eff6ff'))
    c.roundRect(60, 55, 360, 130, 16, fill=1, stroke=0)
    c.setFillColor(BLUE_PRIMARY)
    c.setFont("Arial-Bold", 26)
    c.drawString(80, 155, "Для кого:")
    c.setFillColor(GRAY_DARK)
    c.setFont("Arial", 22)
    c.drawString(80, 118, "• Средний бизнес")
    c.drawString(80, 83, "• 50-200 заявок/месяц")

    # Пример
    c.setFillColor(HexColor('#fef3c7'))
    c.roundRect(PAGE_WIDTH-530, 55, 470, 130, 16, fill=1, stroke=0)
    c.setFillColor(YELLOW)
    c.setFont("Arial-Bold", 26)
    c.drawString(PAGE_WIDTH-510, 155, "Пример:")
    c.setFillColor(GRAY_DARK)
    c.setFont("Arial", 21)
    c.drawString(PAGE_WIDTH-510, 115, "Международная логистика")
    c.drawString(PAGE_WIDTH-510, 80, "(вес + маршрут + таможня + НДС)")

def draw_roi(c):
    """Слайд 6: ROI"""
    c.setFillColor(white)
    c.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, fill=1, stroke=0)

    # Заголовок
    c.setFillColor(BLUE_PRIMARY)
    c.setFont("Arial-Bold", 60)
    c.drawString(60, PAGE_HEIGHT - 100, "ЭКОНОМИКА")

    # Большая цифра ROI
    c.setFont("Arial-Bold", 160)
    c.setFillColor(GREEN)
    c.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT - 270, "5 МЕС")
    c.setFont("Arial", 40)
    c.setFillColor(GRAY_DARK)
    c.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT - 320, "срок окупаемости")

    # ДО и ПОСЛЕ
    y = PAGE_HEIGHT - 430
    box_width = (PAGE_WIDTH - 180) / 2

    # ДО
    c.setFillColor(HexColor('#fef2f2'))
    c.roundRect(60, y-150, box_width, 150, 16, fill=1, stroke=0)
    c.setFillColor(RED)
    c.setFont("Arial-Bold", 36)
    c.drawString(90, y-25, "❌ ДО")
    c.setFillColor(GRAY_DARK)
    c.setFont("Arial", 24)
    c.drawString(90, y-65, "Менеджер: 30 мин на расчёт")
    c.drawString(90, y-98, "Затраты: 36 000₽/мес")
    c.setFont("Arial-Bold", 30)
    c.setFillColor(RED)
    c.drawString(90, y-135, "= 432 000₽/год")

    # ПОСЛЕ
    c.setFillColor(HexColor('#f0fdf4'))
    c.roundRect(60 + box_width + 20, y-150, box_width, 150, 16, fill=1, stroke=0)
    c.setFillColor(GREEN)
    c.setFont("Arial-Bold", 36)
    c.drawString(90 + box_width + 20, y-25, "✓ ПОСЛЕ")
    c.setFillColor(GRAY_DARK)
    c.setFont("Arial", 24)
    c.drawString(90 + box_width + 20, y-65, "Бот: 2 минуты автоматически")
    c.drawString(90 + box_width + 20, y-98, "Затраты: 0₽/расчёт")
    c.setFont("Arial-Bold", 30)
    c.setFillColor(GREEN)
    c.drawString(90 + box_width + 20, y-135, "= 432 000₽ экономия")

    # Бонусы
    c.setFillColor(HexColor('#eff6ff'))
    c.roundRect(60, 55, PAGE_WIDTH-120, 90, 16, fill=1, stroke=0)
    c.setFillColor(BLUE_PRIMARY)
    c.setFont("Arial-Bold", 26)
    c.drawCentredString(PAGE_WIDTH/2, 110, "+ Рост конверсии на 40%  •  Работа 24/7  •  Репутация")

def draw_case_study(c):
    """Слайд 7: Кейс"""
    c.setFillColor(white)
    c.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, fill=1, stroke=0)

    # Заголовок
    c.setFillColor(BLUE_PRIMARY)
    c.setFont("Arial-Bold", 60)
    c.drawString(60, PAGE_HEIGHT - 100, "КЕЙС: PRIME SHIFT")
    c.setFont("Arial", 30)
    c.setFillColor(GRAY_LIGHT)
    c.drawString(60, PAGE_HEIGHT - 145, "Международная логистика")

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
        c.setFillColor(HexColor('#eff6ff'))
        c.roundRect(x, y-190, box_width-10, 190, 16, fill=1, stroke=0)

        c.setFillColor(BLUE_PRIMARY)
        c.setFont("Arial-Bold", 64)
        c.drawCentredString(x + (box_width-10)/2, y-50, big_num)

        c.setFillColor(GRAY_DARK)
        c.setFont("Arial-Bold", 24)
        c.drawCentredString(x + (box_width-10)/2, y-90, label)

        c.setFont("Arial", 18)
        c.setFillColor(GRAY_LIGHT)
        c.drawCentredString(x + (box_width-10)/2, y-120, desc)

        x += box_width + 10

    # Отзыв
    c.setFillColor(HexColor('#f8fafc'))
    c.roundRect(60, 55, PAGE_WIDTH-120, 190, 16, fill=1, stroke=0)

    c.setFillColor(GRAY_DARK)
    c.setFont("Arial-Italic", 24)
    text = '"До внедрения бота мы теряли каждого третьего клиента'
    c.drawString(90, 210, text)
    text2 = 'из-за долгого ответа. Теперь расчёт приходит за 90 секунд,'
    c.drawString(90, 177, text2)
    text3 = 'и конверсия выросла почти в 2 раза."'
    c.drawString(90, 144, text3)

    c.setFont("Arial-Bold", 22)
    c.setFillColor(BLUE_PRIMARY)
    c.drawString(90, 100, "— Алексей К., коммерческий директор")

def draw_objections(c):
    """Слайд 8: Возражения"""
    c.setFillColor(white)
    c.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, fill=1, stroke=0)

    # Заголовок
    c.setFillColor(BLUE_PRIMARY)
    c.setFont("Arial-Bold", 60)
    c.drawString(60, PAGE_HEIGHT - 100, "ВОЗРАЖЕНИЯ")

    # 3 возражения
    y = PAGE_HEIGHT - 190
    objections = [
        ("❓ Это дорого", "Окупается за 5-6 месяцев. Дальше — чистая экономия", GREEN),
        ("❓ У нас есть калькулятор", "Наш работает в мессенджерах. Конверсия на 40% выше", BLUE_PRIMARY),
        ("❓ Слишком сложно", "Если менеджер может посчитать — мы можем автоматизировать", PURPLE)
    ]

    for question, answer, color in objections:
        # Вопрос
        c.setFillColor(HexColor('#fef2f2'))
        c.roundRect(60, y-85, PAGE_WIDTH-120, 40, 10, fill=1, stroke=0)
        c.setFillColor(RED)
        c.setFont("Arial-Bold", 26)
        c.drawString(80, y-70, question)

        # Ответ
        c.setFillColor(HexColor('#f0fdf4'))
        c.roundRect(60, y-145, PAGE_WIDTH-120, 55, 10, fill=1, stroke=0)
        c.setFillColor(color)
        c.setFont("Arial-Bold", 22)
        c.drawString(80, y-113, "✓ " + answer)

        y -= 165

def draw_steps(c):
    """Слайд 9: Этапы"""
    c.setFillColor(white)
    c.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, fill=1, stroke=0)

    # Заголовок
    c.setFillColor(BLUE_PRIMARY)
    c.setFont("Arial-Bold", 60)
    c.drawString(60, PAGE_HEIGHT - 100, "ЭТАПЫ РАБОТЫ")

    # 5 этапов
    steps = [
        ("1", "АНАЛИЗ", "1-2 дня", "ТЗ и смета"),
        ("2", "ПРОТОТИП", "3-5 дней", "Тест версия"),
        ("3", "РАЗРАБОТКА", "7-14 дней", "Готовый бот"),
        ("4", "ТЕСТ", "2-3 дня", "Проверка"),
        ("5", "ЗАПУСК", "1 день", "Production")
    ]

    y = PAGE_HEIGHT - 200
    box_width = (PAGE_WIDTH - 160) / 5 - 15
    x = 60

    for num, title, time, result in steps:
        # Номер
        c.setFillColor(BLUE_PRIMARY)
        c.circle(x + box_width/2, y, 28, fill=1, stroke=0)
        c.setFillColor(white)
        c.setFont("Arial-Bold", 32)
        c.drawCentredString(x + box_width/2, y-12, num)

        # Заголовок
        c.setFillColor(GRAY_DARK)
        c.setFont("Arial-Bold", 22)
        c.drawCentredString(x + box_width/2, y-55, title)

        # Время
        c.setFillColor(GRAY_LIGHT)
        c.setFont("Arial", 18)
        c.drawCentredString(x + box_width/2, y-82, time)

        # Блок результата
        c.setFillColor(HexColor('#eff6ff'))
        c.roundRect(x, y-140, box_width, 45, 10, fill=1, stroke=0)
        c.setFillColor(BLUE_PRIMARY)
        c.setFont("Arial", 16)
        c.drawCentredString(x + box_width/2, y-123, result)

        # Стрелка
        if num != "5":
            c.setStrokeColor(GRAY_LIGHT)
            c.setLineWidth(3)
            c.line(x + box_width + 5, y, x + box_width + 10, y)

        x += box_width + 15

    # Гарантия внизу
    c.setFillColor(GREEN)
    c.roundRect(60, 55, PAGE_WIDTH-120, 90, 16, fill=1, stroke=0)
    c.setFillColor(white)
    c.setFont("Arial-Bold", 40)
    c.drawCentredString(PAGE_WIDTH/2, 105, "✓ ГАРАНТИЯ 3-6 МЕСЯЦЕВ")

def draw_cold_call(c):
    """Слайд 10: Скрипт холодного звонка"""
    c.setFillColor(white)
    c.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, fill=1, stroke=0)

    # Заголовок
    c.setFillColor(BLUE_PRIMARY)
    c.setFont("Arial-Bold", 60)
    c.drawString(60, PAGE_HEIGHT - 100, "СКРИПТ ЗВОНКА")

    # 3 шага
    y = PAGE_HEIGHT - 195

    # Шаг 1
    c.setFillColor(HexColor('#eff6ff'))
    c.roundRect(60, y-115, PAGE_WIDTH-120, 115, 16, fill=1, stroke=0)
    c.setFillColor(BLUE_PRIMARY)
    c.setFont("Arial-Bold", 30)
    c.drawString(80, y-30, "1. ПРЕДСТАВЛЕНИЕ (15 сек)")
    c.setFillColor(GRAY_DARK)
    c.setFont("Arial", 22)
    c.drawString(80, y-67, '"Добрый день! Bereznyak AI. Мы автоматизируем расчёты.')
    c.drawString(80, y-97, 'Вместо 30 минут — 2 минуты. У вас 2 минуты?"')

    y -= 145

    # Шаг 2
    c.setFillColor(HexColor('#eff6ff'))
    c.roundRect(60, y-115, PAGE_WIDTH-120, 115, 16, fill=1, stroke=0)
    c.setFillColor(BLUE_PRIMARY)
    c.setFont("Arial-Bold", 30)
    c.drawString(80, y-30, "2. КВАЛИФИКАЦИЯ (1 мин)")
    c.setFillColor(GRAY_DARK)
    c.setFont("Arial", 22)
    c.drawString(80, y-67, '"Клиенты часто запрашивают расчёт? Сколько заявок?')
    c.drawString(80, y-97, 'Сколько времени уходит на 1 расчёт?"')

    y -= 145

    # Шаг 3
    c.setFillColor(HexColor('#eff6ff'))
    c.roundRect(60, y-115, PAGE_WIDTH-120, 115, 16, fill=1, stroke=0)
    c.setFillColor(BLUE_PRIMARY)
    c.setFont("Arial-Bold", 30)
    c.drawString(80, y-30, "3. ЗАКРЫТИЕ (30 сек)")
    c.setFillColor(GRAY_DARK)
    c.setFont("Arial", 22)
    c.drawString(80, y-67, '"Пришлю демо-бота. Попробуете, и обсудим')
    c.drawString(80, y-97, 'как внедрить у вас. Договорились?"')

def draw_contacts(c):
    """Слайд 11: Контакты в стиле сайта"""
    # Градиентный фон
    draw_gradient_bg(c, DARK_BG, INDIGO_DARK)

    # Светящиеся круги
    c.setFillColorRGB(0.23, 0.51, 0.96, alpha=0.15)
    c.circle(PAGE_WIDTH * 0.25, PAGE_HEIGHT * 0.7, 180, fill=1, stroke=0)

    c.setFillColorRGB(0.63, 0.39, 0.97, alpha=0.15)
    c.circle(PAGE_WIDTH * 0.75, PAGE_HEIGHT * 0.3, 180, fill=1, stroke=0)

    # Заголовок
    c.setFillColor(white)
    c.setFont("Arial-Bold", 80)
    c.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT*0.7, "КОНТАКТЫ")

    # Контакты
    c.setFont("Arial-Bold", 36)
    y = PAGE_HEIGHT*0.55
    contacts = [
        "📧  hello@bezk.pro",
        "📞  +7 (931) 287-79-10",
        "💬  @ann_bezk",
        "🌐  bereznyak-ai.ru"
    ]

    for contact in contacts:
        c.drawCentredString(PAGE_WIDTH/2, y, contact)
        y -= 60

    # Демо-бот в стеклянном блоке
    c.setFillColorRGB(1, 1, 1, alpha=0.1)
    c.roundRect(150, PAGE_HEIGHT*0.17, PAGE_WIDTH-300, 110, 20, fill=1, stroke=0)

    c.setFillColor(white)
    c.setFont("Arial-Bold", 30)
    c.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT*0.23, "ДЕМО-БОТ (ЛОГИСТИКА)")
    c.setFont("Arial", 26)
    c.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT*0.19, "t.me/prime_shift_bot")

    # Призыв
    c.setFont("Arial-Bold", 52)
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
    print(f"🎨 Дизайн: в стиле сайта bereznyak-ai.ru")
    print(f"✓ Кириллица поддерживается")

if __name__ == "__main__":
    generate_presentation()
