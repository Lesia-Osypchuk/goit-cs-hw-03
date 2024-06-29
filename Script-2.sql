SELECT * FROM status;
SELECT * From users;
SELECT * FROM tasks;

--Отримати всі завдання певного користувача за його user_id
SELECT * FROM tasks WHERE user_id = 2;
--Вибрати завдання за певним статусом (наприклад, 'new') з використанням підзапиту
SELECT * FROM tasks WHERE status_id = (SELECT id FROM status WHERE name = 'new');
-- Оновити статус конкретного завдання на 'in progress' (або інший статус)
UPDATE tasks SET status_id = (SELECT id FROM status WHERE name = 'in progress') WHERE id = 3;
-- Отримати список користувачів, які не мають жодного завдання
SELECT * FROM users WHERE id NOT IN (SELECT DISTINCT user_id FROM tasks);

SELECT * FROM tasks;
--Додати нове завдання для конкретного користувача
INSERT INTO tasks (title, description, status_id, user_id) VALUES ('Назва завдання', 'Опис завдання', 3, 5);
-- Отримати всі завдання, які ще не завершено
SELECT * FROM tasks WHERE status_id <> (SELECT id FROM status WHERE name = 'completed');
-- Видалити конкретне завдання за його id
DELETE FROM tasks WHERE id = 21;


-- Знайти користувачів з певною електронною поштою (за паттерном, наприклад, '%@example.com')
SELECT * FROM users WHERE email LIKE '%@example.com';
--Оновити ім'я користувача
UPDATE users SET fullname = 'Нове' WHERE id = 2;
--Отримати кількість завдань для кожного статусу
SELECT s.name, COUNT(t.id) AS tasks_count
FROM status s
LEFT JOIN tasks t ON s.id = t.status_id
GROUP BY s.name;
-- Отримати завдання, які призначені користувачам з певною доменною частиною електронної пошти (наприклад, '%@example.com')
SELECT t.*
FROM tasks t
INNER JOIN users u ON t.user_id = u.id
WHERE u.email LIKE '%@example.com';
-- Отримати список завдань, що не мають опису
SELECT * FROM tasks WHERE description IS NULL OR description = '';
-- Вибрати користувачів та їхні завдання, які є у статусі 'in progress' (використовуючи INNER JOIN)
SELECT u.*, t.*
FROM users u
INNER JOIN tasks t ON u.id = t.user_id
WHERE t.status_id = (SELECT id FROM status WHERE name = 'in progress');
-- Отримати користувачів та кількість їхніх завдань (використовуючи LEFT JOIN та GROUP BY)
SELECT u.fullname, COUNT(t.id) AS tasks_count
FROM users u
LEFT JOIN tasks t ON u.id = t.user_id
GROUP BY u.fullname;








