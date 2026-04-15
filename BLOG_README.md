# 📝 Раздел блога для bezk.pro

## Что создано:

### 1. Главная страница блога
**Файл:** `/blog.html`
- Красивый лендинг в стиле основного сайта
- Карточки статей с тегами
- Фильтры по категориям (Все, Кейсы, Технологии, AI)
- Готовы плейсхолдеры для будущих статей

### 2. Первая статья
**Файл:** `/blog/blue-circle-bot-case-study.html`
- Полноценный кейс о Blue Circle Bot
- Архитектура, технологии, решения
- 3 забавных бага с подробным разбором
- Стильное оформление с подсветкой кода
- Статистика в карточках
- Время чтения: ~15 минут

### 3. Обновления на главной
**Файл:** `/index.html` (обновлен футер)
- Добавлена ссылка "Блог" в футере
- Навигация стала более функциональной

## 📁 Структура файлов:

```
bereznyak_ai/
├── index.html                     # Главная страница
├── blog.html                      # 🆕 Страница блога (каталог статей)
├── logistic-bot-case/             # 🆕 Папка первой статьи
│   ├── index.html                 # Статья
│   └── logistics-hero.png         # Изображение для статьи
└── BLOG_README.md                 # 🆕 Этот файл
```

## 🚀 Как использовать:

### Локальный просмотр:
1. Откройте в браузере:
   - Блог (каталог): `file:///Users/annabereznyak/Desktop/Все проекты/Bereznyak_ai/bereznyak_ai/blog.html`
   - Статья: `file:///Users/annabereznyak/Desktop/Все проекты/Bereznyak_ai/bereznyak_ai/logistic-bot-case/index.html`

### Деплой на сервер:
```bash
cd "/Users/annabereznyak/Desktop/Все проекты/Bereznyak_ai/bereznyak_ai"

# Проверить изменения
git status

# Добавить новые файлы
git add blog.html logistic-bot-case/ BLOG_README.md

# Закоммитить
git commit -m "Add blog section with logistic bot case study"

# Запушить на сервер
git push origin main
```

После пуша на сервере будут доступны:
- **Блог:** https://bezk.pro/blog.html
- **Статья:** https://bezk.pro/logistic-bot-case

## 📝 Как работает blog.html:

Страница **blog.html** — это каталог всех статей с:
- Фильтрами по категориям (Все статьи, Кейсы, Технологии, AI)
- Карточками статей в grid-сетке
- Красивым hover-эффектом на карточках

Когда пользователь:
1. Заходит на https://bezk.pro/blog.html
2. Видит все доступные статьи
3. Кликает на интересную карточку
4. Переходит на полную статью (например, /logistic-bot-case)

## ✍️ Как добавить новую статью:

### Шаг 1: Создать папку для статьи
Создайте папку с коротким URL-именем (например, `my-article-name`):
```bash
cd "/Users/annabereznyak/Desktop/Все проекты/Bereznyak_ai/bereznyak_ai"
mkdir my-article-name
```

### Шаг 2: Создать HTML файл
Скопируйте существующую статью как шаблон:
```bash
cp logistic-bot-case/index.html my-article-name/index.html
```

### Шаг 3: Отредактировать содержимое
- Замените `<title>`, `<meta>` теги
- Обновите заголовок H1, дату публикации
- Напишите контент статьи
- Добавьте изображения в ту же папку (если нужно)

### Шаг 4: Добавить карточку на blog.html
Найдите секцию "Articles Grid" в blog.html и добавьте новую карточку:

```html
<article class="glassmorphism rounded-2xl overflow-hidden article-card">
    <div class="h-48 bg-gradient-to-br from-blue-600 to-indigo-600 flex items-center justify-center">
        <i data-lucide="название-иконки" class="w-20 h-20 text-white opacity-80"></i>
    </div>
    <div class="p-6">
        <div class="flex items-center gap-2 mb-3">
            <span class="text-xs text-blue-400 font-semibold">КЕЙС</span>
            <span class="text-xs text-gray-500">•</span>
            <span class="text-xs text-gray-500">15 апреля 2026</span>
        </div>
        <h3 class="text-xl font-bold mb-3 text-white hover:text-blue-400 transition-colors">
            <a href="my-article-name">
                Заголовок статьи
            </a>
        </h3>
        <p class="text-gray-400 mb-4 line-clamp-3">
            Краткое описание статьи...
        </p>
        <div class="flex items-center justify-between">
            <div class="flex gap-2">
                <span class="px-2 py-1 bg-blue-500/20 text-blue-400 text-xs rounded">AI</span>
                <span class="px-2 py-1 bg-purple-500/20 text-purple-400 text-xs rounded">Python</span>
            </div>
            <a href="my-article-name" class="text-blue-400 hover:text-blue-300 flex items-center gap-1 text-sm font-medium">
                Читать
                <i data-lucide="arrow-right" class="w-4 h-4"></i>
            </a>
        </div>
    </div>
</article>
```

### Шаг 5: Закоммитить
```bash
git add my-article-name/ blog.html
git commit -m "Add new blog article: My Article Name"
git push
```

## 🎯 Быстрый старт (добавить статью за 5 минут):

```bash
# 1. Создать папку
mkdir my-new-article

# 2. Скопировать шаблон
cp logistic-bot-case/index.html my-new-article/index.html

# 3. Отредактировать my-new-article/index.html
# - Заменить <title>, <h1>, дату
# - Написать контент

# 4. Добавить карточку в blog.html
# - Найти "ОПУБЛИКОВАННЫЕ СТАТЬИ"
# - Скопировать последнюю карточку
# - Изменить ссылки на "my-new-article"

# 5. Закоммитить
git add my-new-article/ blog.html
git commit -m "Add new article"
git push
```

Готово! Статья доступна по адресу: **https://bezk.pro/my-new-article**

## 🎨 Элементы дизайна в статье:

### Highlight Box (важная информация):
```html
<div class="highlight-box">
    <p><strong>Важно:</strong> Ваш текст здесь</p>
</div>
```

### Bug Story Box (история бага):
```html
<div class="bug-story">
    <h3 style="color: #fca5a5; margin-top: 0;">Заголовок бага</h3>
    <p>Описание проблемы...</p>
</div>
```

### Stat Card (статистика):
```html
<div class="stat-card">
    <div class="text-3xl font-bold text-blue-400 mb-1">99.7%</div>
    <div class="text-sm text-gray-400">точность</div>
</div>
```

### Code Block:
```html
<pre><code>const example = "код здесь";</code></pre>
```

### Inline Code:
```html
<code>переменная</code>
```

## 📊 Доступные иконки (Lucide):
- `bot` - робот
- `cpu` - процессор
- `trending-up` - график вверх
- `code` - код
- `database` - база данных
- `zap` - молния
- `shield-check` - галочка в щите

Полный список: https://lucide.dev/icons/

## 🎯 SEO оптимизация:

Для каждой статьи не забудьте:
1. Уникальный `<title>`
2. `<meta name="description">` (до 160 символов)
3. `<meta name="keywords">` (5-10 ключевых слов)
4. Хорошая структура заголовков (H2, H3)
5. Alt-теги для изображений (если добавляете)

## ✅ Чеклист перед публикацией:

- [ ] Статья написана и отформатирована
- [ ] Проверена орфография
- [ ] Добавлена карточка на blog.html
- [ ] Обновлены meta-теги
- [ ] Проверены все ссылки
- [ ] Протестировано локально в браузере
- [ ] Закоммичено в git
- [ ] Запушено на сервер

## 🔗 Полезные ссылки:

- Tailwind CSS: https://tailwindcss.com/docs
- Lucide Icons: https://lucide.dev/
- Yandex Metrika: уже подключена (ID: 108506107)

---

**Автор:** Claude AI
**Дата создания:** 15 апреля 2026
**Статус:** ✅ Готово к использованию
