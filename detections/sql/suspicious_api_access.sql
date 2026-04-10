SELECT user, ip, COUNT(*) AS suspicious_accesses
FROM api_logs
WHERE user != resource_owner
GROUP BY user, ip
HAVING COUNT(*) >= 5;