# Detection Writeups

This document outlines the detection logic, purpose, and investigation guidance for each detection implemented in the Detection Lab.

---

## 1. Brute Force Login Detection

### Objective
Detect repeated failed login attempts from the same IP and user that may indicate brute force or credential stuffing activity.

### Log Source
auth_logs.csv

### Detection Logic
Triggers when 5 or more failed login attempts occur for the same user from the same IP address.

### Why It Matters
Repeated failed login attempts are a common indicator of brute force attacks, password spraying, or credential stuffing. These attacks can lead to account compromise if successful.

### Example Scenario
An attacker attempts multiple passwords against a single user account from the same IP address.

### False Positives
- User entering incorrect password multiple times
- Misconfigured scripts or automation tools
- Internal testing activity

### Investigation Steps
1. Identify the source IP address and check reputation
2. Determine if login attempts eventually succeeded
3. Check if the targeted account has elevated privileges
4. Review login patterns (time, frequency, geolocation)

### Recommended Response
- Temporarily lock the account
- Block or rate-limit the source IP
- Force password reset if compromise is suspected

---

## 2. Suspicious API Access Detection

### Objective
Detect repeated access to resources not owned by the requesting user, indicating possible authorization bypass or IDOR-style attacks.

### Log Source
api_logs.csv

### Detection Logic
Triggers when a user accesses 5 or more resources that are not owned by them.

### Why It Matters
Accessing resources outside of a user's authorization scope may indicate broken access control vulnerabilities such as IDOR (Insecure Direct Object Reference).

### Example Scenario
A user iterates through resource IDs (e.g., account numbers) attempting to access other users’ data.

### False Positives
- Legitimate admin or support access
- Shared resources in certain systems
- Testing or QA activity

### Investigation Steps
1. Identify affected resources and owners
2. Determine if access was authorized or expected
3. Review user role and permissions
4. Check for patterns of enumeration or sequential access

### Recommended Response
- Validate authorization controls
- Restrict access where necessary
- Monitor user activity for further abuse
- Initiate incident response if data exposure is confirmed

---

## 3. Privilege Escalation / Defense Evasion Detection

### Objective
Detect high-risk administrative actions that may indicate privilege escalation or attempts to evade detection.

### Log Source
cloud_logs.csv

### Detection Logic
Triggers when actions such as `attach_admin_policy` or `disable_logging` are observed.

### Why It Matters
These actions are high-risk because they can grant elevated privileges or disable monitoring, allowing attackers to persist undetected.

### Example Scenario
A low-privileged user attaches an admin policy to themselves and disables logging to cover their tracks.

### False Positives
- Legitimate administrative actions
- Infrastructure automation scripts
- Planned maintenance activities

### Investigation Steps
1. Verify user identity and role
2. Confirm whether action was authorized
3. Review recent activity leading up to the event
4. Check for additional suspicious behavior

### Recommended Response
- Revoke unauthorized privileges
- Re-enable logging and monitoring
- Investigate for further compromise
- Escalate to incident response if necessary