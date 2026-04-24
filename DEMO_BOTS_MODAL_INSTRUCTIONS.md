# 🤖 Инструкция: Добавление модального окна с демо-ботами

## ШАГ 1: Изменить кнопку (строка 1927)

**Найти:**
```html
<button class="btn-primary text-white px-10 py-5 rounded-xl font-semibold text-xl flex items-center gap-3 group" onclick="ym(108506107,'reachGoal','demo_bot_click')">
```

**Заменить на:**
```html
<button class="btn-primary text-white px-10 py-5 rounded-xl font-semibold text-xl flex items-center gap-3 group" onclick="openDemoBotsModal()">
```

---

## ШАГ 2: Добавить модальное окно

**Где:** Перед строкой 2126 (перед `</body>`)

**Вставить этот код:**

```html
<!-- ================================================================
     MODAL: Demo Bots Selector
     ================================================================ -->
<div id="demoBotsModal" class="fixed inset-0 bg-slate-950/90 backdrop-blur-sm z-50 hidden flex items-center justify-center p-6" onclick="closeDemoBotsModal(event)">
    <div class="relative max-w-5xl w-full glassmorphism rounded-3xl p-8 md:p-12 border-2 border-blue-500/30 shadow-2xl shadow-blue-500/20 animate-modal-fade-in" onclick="event.stopPropagation()">

        <!-- Close button -->
        <button onclick="closeDemoBotsModal()" class="absolute top-6 right-6 w-10 h-10 rounded-full bg-slate-800/50 hover:bg-slate-700/50 border border-slate-600 flex items-center justify-center transition-all group">
            <i data-lucide="x" class="w-5 h-5 text-gray-400 group-hover:text-white"></i>
        </button>

        <!-- Header -->
        <div class="text-center mb-10">
            <div class="inline-block bg-gradient-to-r from-blue-600/20 via-indigo-600/20 to-purple-600/20 border border-blue-500/30 rounded-full px-6 py-2 mb-4">
                <span class="text-blue-400 text-sm font-semibold">🚀 Попробуйте прямо сейчас</span>
            </div>
            <h2 class="text-3xl md:text-4xl font-black mb-4 text-white">
                Выберите демо-бот для тестирования
            </h2>
            <p class="text-lg text-gray-300">
                Откроется в Telegram. Ответьте на 5-7 вопросов и получите готовую смету
            </p>
        </div>

        <!-- Bots Grid -->
        <div class="grid md:grid-cols-3 gap-6">

            <!-- BOT 1: Международная логистика (ACTIVE) -->
            <a href="ВСТАВЬТЕ_ССЫЛКУ_НА_БОТА_ЗДЕСЬ" target="_blank" onclick="ym(108506107,'reachGoal','demo_logistics_click')" class="group relative block">
                <div class="relative h-full glassmorphism rounded-2xl p-6 border-2 border-blue-500/40 hover:border-blue-400/60 transition-all duration-300 hover:scale-105 hover:shadow-2xl hover:shadow-blue-500/30">

                    <!-- Active badge -->
                    <div class="absolute -top-3 -right-3 bg-gradient-to-r from-green-500 to-emerald-600 text-white text-xs font-bold px-3 py-1 rounded-full shadow-lg">
                        ✓ Доступен
                    </div>

                    <!-- Icon -->
                    <div class="w-16 h-16 bg-gradient-to-br from-blue-500 to-indigo-600 rounded-2xl flex items-center justify-center mb-4 shadow-lg shadow-blue-500/50 group-hover:scale-110 transition-transform">
                        <i data-lucide="plane" class="w-8 h-8 text-white"></i>
                    </div>

                    <!-- Title -->
                    <h3 class="text-xl font-bold text-white mb-2">
                        Международная логистика
                    </h3>

                    <!-- Description -->
                    <p class="text-sm text-gray-400 mb-4 leading-relaxed">
                        Расчёт стоимости доставки груза с учётом веса, маршрута и таможенных платежей
                    </p>

                    <!-- Features -->
                    <ul class="space-y-2 mb-6">
                        <li class="flex items-center gap-2 text-xs text-gray-300">
                            <i data-lucide="check" class="w-4 h-4 text-green-400"></i>
                            <span>7 вопросов</span>
                        </li>
                        <li class="flex items-center gap-2 text-xs text-gray-300">
                            <i data-lucide="check" class="w-4 h-4 text-green-400"></i>
                            <span>PDF-смета на почту</span>
                        </li>
                        <li class="flex items-center gap-2 text-xs text-gray-300">
                            <i data-lucide="check" class="w-4 h-4 text-green-400"></i>
                            <span>Актуальные курсы валют</span>
                        </li>
                    </ul>

                    <!-- CTA -->
                    <div class="flex items-center justify-between text-blue-400 font-semibold text-sm group-hover:text-blue-300">
                        <span>Запустить в Telegram</span>
                        <i data-lucide="arrow-right" class="w-4 h-4 group-hover:translate-x-1 transition-transform"></i>
                    </div>
                </div>
            </a>

            <!-- BOT 2: Детейлинг-центр (COMING SOON) -->
            <div class="group relative opacity-60 cursor-not-allowed">
                <div class="relative h-full glassmorphism rounded-2xl p-6 border-2 border-slate-700">

                    <!-- Coming soon badge -->
                    <div class="absolute -top-3 -right-3 bg-gradient-to-r from-orange-500 to-amber-600 text-white text-xs font-bold px-3 py-1 rounded-full shadow-lg">
                        Скоро
                    </div>

                    <!-- Icon (grayscale) -->
                    <div class="w-16 h-16 bg-gradient-to-br from-slate-700 to-slate-800 rounded-2xl flex items-center justify-center mb-4 shadow-lg">
                        <i data-lucide="car" class="w-8 h-8 text-gray-500"></i>
                    </div>

                    <!-- Title -->
                    <h3 class="text-xl font-bold text-gray-400 mb-2">
                        Детейлинг-центр
                    </h3>

                    <!-- Description -->
                    <p class="text-sm text-gray-500 mb-4 leading-relaxed">
                        Подбор услуг по марке авто и состоянию кузова с автоматическим расчётом
                    </p>

                    <!-- Features -->
                    <ul class="space-y-2 mb-6">
                        <li class="flex items-center gap-2 text-xs text-gray-500">
                            <i data-lucide="clock" class="w-4 h-4 text-gray-600"></i>
                            <span>В разработке</span>
                        </li>
                        <li class="flex items-center gap-2 text-xs text-gray-500">
                            <i data-lucide="clock" class="w-4 h-4 text-gray-600"></i>
                            <span>Запуск в мае 2026</span>
                        </li>
                    </ul>

                    <!-- Disabled CTA -->
                    <div class="flex items-center justify-between text-gray-600 font-semibold text-sm">
                        <span>Недоступно</span>
                        <i data-lucide="lock" class="w-4 h-4"></i>
                    </div>
                </div>
            </div>

            <!-- BOT 3: Кондиционеры под ключ (COMING SOON) -->
            <div class="group relative opacity-60 cursor-not-allowed">
                <div class="relative h-full glassmorphism rounded-2xl p-6 border-2 border-slate-700">

                    <!-- Coming soon badge -->
                    <div class="absolute -top-3 -right-3 bg-gradient-to-r from-orange-500 to-amber-600 text-white text-xs font-bold px-3 py-1 rounded-full shadow-lg">
                        Скоро
                    </div>

                    <!-- Icon (grayscale) -->
                    <div class="w-16 h-16 bg-gradient-to-br from-slate-700 to-slate-800 rounded-2xl flex items-center justify-center mb-4 shadow-lg">
                        <i data-lucide="wind" class="w-8 h-8 text-gray-500"></i>
                    </div>

                    <!-- Title -->
                    <h3 class="text-xl font-bold text-gray-400 mb-2">
                        Кондиционеры под ключ
                    </h3>

                    <!-- Description -->
                    <p class="text-sm text-gray-500 mb-4 leading-relaxed">
                        Расчёт мощности, подбор оборудования и стоимости монтажа
                    </p>

                    <!-- Features -->
                    <ul class="space-y-2 mb-6">
                        <li class="flex items-center gap-2 text-xs text-gray-500">
                            <i data-lucide="clock" class="w-4 h-4 text-gray-600"></i>
                            <span>В разработке</span>
                        </li>
                        <li class="flex items-center gap-2 text-xs text-gray-500">
                            <i data-lucide="clock" class="w-4 h-4 text-gray-600"></i>
                            <span>Запуск в июне 2026</span>
                        </li>
                    </ul>

                    <!-- Disabled CTA -->
                    <div class="flex items-center justify-between text-gray-600 font-semibold text-sm">
                        <span>Недоступно</span>
                        <i data-lucide="lock" class="w-4 h-4"></i>
                    </div>
                </div>
            </div>

        </div>

        <!-- Footer note -->
        <div class="mt-8 text-center">
            <p class="text-sm text-gray-400">
                💡 <span class="text-white font-semibold">Совет:</span> Укажите реальные данные, чтобы увидеть точность расчётов
            </p>
        </div>

    </div>
</div>
```

---

## ШАГ 3: Добавить JavaScript для управления модалкой

**Где:** После кода модалки, но перед `</body>`

**Вставить:**

```html
<script>
    // ================================================================
    // Demo Bots Modal Management
    // ================================================================

    function openDemoBotsModal() {
        const modal = document.getElementById('demoBotsModal');
        modal.classList.remove('hidden');
        modal.classList.add('flex');
        document.body.style.overflow = 'hidden'; // Prevent scroll

        // Track in Yandex.Metrika
        if (typeof ym !== 'undefined') {
            ym(108506107, 'reachGoal', 'demo_bot_modal_opened');
        }

        // Re-initialize Lucide icons for modal content
        if (typeof lucide !== 'undefined') {
            lucide.createIcons();
        }
    }

    function closeDemoBotsModal(event) {
        // Close only if clicked on backdrop or close button
        if (!event || event.target.id === 'demoBotsModal' || event.currentTarget.tagName === 'BUTTON') {
            const modal = document.getElementById('demoBotsModal');
            modal.classList.add('hidden');
            modal.classList.remove('flex');
            document.body.style.overflow = ''; // Restore scroll
        }
    }

    // Close on ESC key
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape') {
            closeDemoBotsModal();
        }
    });
</script>
```

---

## ШАГ 4: Добавить CSS анимацию для модалки

**Где:** В секции `<style>` в `<head>` (в самом конце перед `</style>`)

**Вставить:**

```css
/* ================================================================
   Modal Animation
   ================================================================ */
@keyframes modalFadeIn {
    from {
        opacity: 0;
        transform: scale(0.95) translateY(20px);
    }
    to {
        opacity: 1;
        transform: scale(1) translateY(0);
    }
}

.animate-modal-fade-in {
    animation: modalFadeIn 0.3s ease-out forwards;
}

/* Prevent body scroll when modal is open */
body.modal-open {
    overflow: hidden;
}
```

---

## ШАГ 5: ВСТАВИТЬ ССЫЛКУ НА БОТА

**Найти строку в модальном окне:**
```html
<a href="ВСТАВЬТЕ_ССЫЛКУ_НА_БОТА_ЗДЕСЬ" target="_blank"
```

**Заменить на:**
```html
<a href="https://t.me/ВАШ_БОТ_USERNAME" target="_blank"
```

Например:
```html
<a href="https://t.me/bereznyak_logistics_bot" target="_blank"
```

---

## ✅ ФИНАЛЬНЫЙ ЧЕК-ЛИСТ

- [ ] Шаг 1: Изменена кнопка (добавлен onclick="openDemoBotsModal()")
- [ ] Шаг 2: Добавлено модальное окно перед `</body>`
- [ ] Шаг 3: Добавлен JavaScript для управления
- [ ] Шаг 4: Добавлена CSS анимация
- [ ] Шаг 5: Вставлена ссылка на Telegram-бота
- [ ] Проверено: Клик по кнопке открывает модалку
- [ ] Проверено: Клик вне модалки закрывает её
- [ ] Проверено: ESC закрывает модалку
- [ ] Проверено: Иконки отображаются корректно
- [ ] Проверено: Ссылка на бота работает

---

## 🎨 ПРЕВЬЮ РЕЗУЛЬТАТА

```
┌───────────────────────────────────────────────────────────┐
│                🚀 Попробуйте прямо сейчас                 │
│         Выберите демо-бот для тестирования                │
│                                                           │
├─────────────┬─────────────┬─────────────────────────────┤
│ ✈️ ЛОГИСТИКА │ 🚗 ДЕТЕЙЛИНГ │ ❄️ КОНДИЦИОНЕРЫ           │
│ ✓ Доступен   │ ⏳ Скоро     │ ⏳ Скоро                  │
│              │              │                            │
│ 7 вопросов   │ В разработке │ В разработке              │
│ PDF-смета    │ Запуск: май  │ Запуск: июнь             │
│ Курсы валют  │              │                            │
│              │              │                            │
│ [Запустить→] │ [🔒Недоступ] │ [🔒Недоступ]              │
└─────────────┴─────────────┴─────────────────────────────┘
```

---

**Готово!** После этих изменений при клике на "Запустить демо-бот в мессенджере" откроется красивое модальное окно с выбором ботов.
