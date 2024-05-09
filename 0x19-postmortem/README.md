```markdown
Issue Summary:

- Duration: May 5, 2024, 08:00 UTC to May 6, 2024, 04:00 UTC
- Impact: The website's database server experienced intermittent outages, causing service disruptions for 30% of users. Users reported slow loading times and occasional errors.

Timeline:
- May 5, 08:00 UTC: Issue detected through monitoring alerts indicating database connectivity failures.
- May 5, 08:15 UTC: Engineering team notified about the outage.
- May 5, 08:30 UTC: Investigated network connectivity and server logs, assuming network misconfiguration.
- May 5, 10:00 UTC: No conclusive evidence found, issue escalated to database specialists.
- May 5, 12:00 UTC: Database specialists identified abnormal spikes in CPU usage during peak hours.
- May 5, 14:00 UTC: Implemented temporary mitigation measures to redistribute database load.
- May 5, 16:00 UTC: Issue persisted despite mitigation efforts, escalated to senior engineers.
- May 5, 18:00 UTC: Senior engineers discovered a misconfigured database query causing inefficient resource usage.
- May 5, 20:00 UTC: Implemented a fix by optimizing the database query.
- May 5, 22:00 UTC: Verified fix effectiveness and monitored system stability.
- May 6, 04:00 UTC: Service fully restored and stabilized.

Root Cause and Resolution:

- Root Cause: The issue stemmed from a poorly optimized database query, causing excessive CPU usage during peak traffic hours.
- Resolution: The database query was optimized to reduce resource consumption and improve efficiency. Additionally, monitoring thresholds were adjusted to promptly detect similar issues in the future.

Corrective and Preventative Measures:

- Improvements/Fixes:
  - Implement regular code reviews to catch inefficient queries early.
  - Enhance monitoring capabilities to detect abnormal resource usage more accurately.
  - Conduct performance testing under simulated peak loads to identify potential bottlenecks.
- Tasks:
  1. Conduct code review for all database queries to identify and optimize inefficient ones.
  2. Update monitoring thresholds to trigger alerts for abnormal CPU usage.
  3. Schedule regular performance tests to simulate peak traffic scenarios.
  4. Document best practices for database query optimization and share with the team for future reference.
  
By implementing these measures and addressing the root cause, we aim to minimize the likelihood of similar outages and ensure optimal performance of our services going forward.

[GitHub Repository](https://github.com/Ip-Tec/alx-system_engineering-devops/0x19-postmortem)
```
