SELECT timestamp, user, action, target, ip
FROM cloud_logs
WHERE action IN ('attach_admin_policy', 'disable_logging');