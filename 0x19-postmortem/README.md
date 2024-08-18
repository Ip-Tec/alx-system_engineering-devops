# Postmortem: The Case of the Missing Cookies

## Issue Summary

**Duration**: August 10, 2024, 10:00 AM - August 10, 2024, 12:30 PM (UTC)

**Impact**: During the outage, 75% of our users were unable to stay logged in, resulting in numerous complaints and a significant drop in active sessions. Users experienced frequent logouts, making it impossible for them to complete their shopping or browse the site without interruption.

**Root Cause**: The root cause of the issue was a misconfigured cache setting that led to session cookies being prematurely expired.

## Timeline

- **10:00 AM**: Issue detected by the engineering team through a sudden spike in login failures and user complaints.
- **10:05 AM**: Monitoring tools confirmed that the number of active sessions had dropped by 75%.
- **10:15 AM**: Initial investigation began focusing on the authentication service, suspecting an issue with the login API.
- **10:30 AM**: The team noticed an anomaly in the cache server logs, but dismissed it as unrelated.
- **10:45 AM**: Further investigation was escalated to the DevOps team to check for any recent changes in the infrastructure.
- **11:00 AM**: A misleading assumption was made that a recent deployment was the culprit, leading to a rollback, which did not resolve the issue.
- **11:30 AM**: A detailed review of the cache server configuration revealed that session cookies were being cached incorrectly, causing them to expire prematurely.
- **12:00 PM**: Cache settings were corrected, and the session service was restarted.
- **12:30 PM**: Full service was restored, and users were able to stay logged in without issues.

## Root Cause and Resolution

The issue was caused by a misconfiguration in our cache server settings. The cache was configured to store session cookies with a short TTL (Time To Live), which led to the cookies expiring before the user's session was truly over. This caused users to be logged out prematurely, leading to a frustrating experience.

To resolve the issue, we identified the incorrect cache setting and updated it to ensure that session cookies are no longer cached or are cached with the correct TTL. The session service was then restarted to apply the new configuration, and the issue was resolved.

## Corrective and Preventative Measures

To prevent this issue from recurring, the following actions will be taken:

1. **Patch Cache Configuration**: Update the cache server settings to prevent session cookies from being cached improperly.
2. **Add Monitoring on Session TTL**: Implement monitoring to track the TTL of session cookies and alert the team if cookies are expiring too soon.
3. **Improve Incident Response**: Conduct a training session for the team on how to better identify cache-related issues.
4. **Document Configuration Changes**: Maintain thorough documentation of all cache settings and their impacts on session management.
5. **Perform Regular Audits**: Schedule regular audits of the cache configuration to ensure it aligns with best practices.

By implementing these measures, we aim to enhance the reliability of our session management and prevent similar issues from affecting our users in the future.


