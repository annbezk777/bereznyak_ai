<?php
/**
 * Backend endpoint для отправки заявок в Telegram
 * Обрабатывает CORS и пересылает сообщения через Telegram Bot API
 */

// Разрешаем CORS
header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Methods: POST, OPTIONS');
header('Access-Control-Allow-Headers: Content-Type');
header('Content-Type: application/json; charset=utf-8');

// Обработка preflight запроса
if ($_SERVER['REQUEST_METHOD'] === 'OPTIONS') {
    http_response_code(200);
    exit;
}

// Принимаем только POST
if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    http_response_code(405);
    echo json_encode(['error' => 'Method not allowed']);
    exit;
}

// Получаем данные из запроса
$input = file_get_contents('php://input');
$data = json_decode($input, true);

if (!$data || !isset($data['message'])) {
    http_response_code(400);
    echo json_encode(['error' => 'Invalid request data']);
    exit;
}

// Настройки Telegram Bot
$botToken = '8171742276:AAHOdnAPPql_8MEsS60bxBAa1PJoCcX7P-w';
$chatIds = [
    '1337987399',  // Основной админ
    '1336680373'   // Katrina (менеджер)
];

$message = $data['message'];
$results = [];

// Отправляем сообщение всем получателям
foreach ($chatIds as $chatId) {
    $telegramUrl = "https://api.telegram.org/bot{$botToken}/sendMessage";

    $postData = [
        'chat_id' => $chatId,
        'text' => $message
    ];

    $ch = curl_init($telegramUrl);
    curl_setopt($ch, CURLOPT_POST, 1);
    curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($postData));
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_HTTPHEADER, ['Content-Type: application/json']);

    $response = curl_exec($ch);
    $httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
    $error = curl_error($ch);
    curl_close($ch);

    $responseData = json_decode($response, true);

    $results[] = [
        'chatId' => $chatId,
        'success' => isset($responseData['ok']) && $responseData['ok'] === true,
        'httpCode' => $httpCode,
        'error' => $error ?: (isset($responseData['description']) ? $responseData['description'] : null)
    ];
}

// Проверяем, отправилось ли хотя бы одному получателю
$successCount = count(array_filter($results, function($r) {
    return $r['success'];
}));

if ($successCount > 0) {
    http_response_code(200);
    echo json_encode([
        'success' => true,
        'message' => 'Заявка успешно отправлена',
        'sent' => $successCount,
        'total' => count($chatIds),
        'details' => $results
    ]);
} else {
    http_response_code(500);
    echo json_encode([
        'success' => false,
        'error' => 'Не удалось отправить заявку ни одному получателю',
        'details' => $results
    ]);
}
