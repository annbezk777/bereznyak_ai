/**
 * Vercel Serverless Function - Proxy для отправки заявок в Telegram
 * Обходит блокировку api.telegram.org в РФ
 */

export default async function handler(req, res) {
    // Разрешаем CORS для вашего домена
    res.setHeader('Access-Control-Allow-Origin', '*');
    res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
    res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

    // Обработка preflight запроса
    if (req.method === 'OPTIONS') {
        return res.status(200).end();
    }

    // Принимаем только POST запросы
    if (req.method !== 'POST') {
        return res.status(405).json({ error: 'Method not allowed' });
    }

    try {
        const { name, contact, message } = req.body;

        // Валидация
        if (!name || !contact || !message) {
            return res.status(400).json({
                error: 'Missing required fields',
                required: ['name', 'contact', 'message']
            });
        }

        // Telegram Bot настройки
        const botToken = process.env.TELEGRAM_BOT_TOKEN || '8171742276:AAHOdnAPPql_8MEsS60bxBAa1PJoCcX7P-w';
        const chatIds = [
            '1337987399',  // Основной админ
            '1336680373'   // Katrina (менеджер)
        ];

        // Отправляем сообщение всем получателям
        const sendPromises = chatIds.map(async chatId => {
            try {
                const response = await fetch(`https://api.telegram.org/bot${botToken}/sendMessage`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({
                        chat_id: chatId,
                        text: message
                    })
                });

                const data = await response.json();
                return { chatId, success: data.ok, error: data.description };
            } catch (error) {
                return { chatId, success: false, error: error.message };
            }
        });

        const results = await Promise.all(sendPromises);
        const successCount = results.filter(r => r.success).length;

        if (successCount > 0) {
            return res.status(200).json({
                success: true,
                message: 'Заявка успешно отправлена',
                sent: successCount,
                total: chatIds.length,
                details: results
            });
        } else {
            return res.status(500).json({
                success: false,
                error: 'Не удалось отправить заявку ни одному получателю',
                details: results
            });
        }

    } catch (error) {
        console.error('Server error:', error);
        return res.status(500).json({
            success: false,
            error: 'Internal server error',
            message: error.message
        });
    }
}
