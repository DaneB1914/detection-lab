SELECT ip, user, COUNT(*) AS failed_attempts
FROM auth_logs
WHERE status = 'failed'
GROUP BY ip, user
HAVING COUNT(*) >= 5;