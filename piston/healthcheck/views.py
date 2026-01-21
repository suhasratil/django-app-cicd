from health_check.backends import BaseHealthCheckBackend
from health_check.exceptions import HealthCheckException
from jira import JIRA


class JiraFilterHealthCheckView(BaseHealthCheckBackend):
    critical_service = False
    issue_count = 0

    def check_status(self):
        try:
            jira = JIRA(server="https://bugs-legacy.mojang.com/", timeout=(3.0, 5.0), max_retries=0)
            results = jira.search_issues(jira.filter("14500").jql, maxResults=0)
            self.issue_count = results.total
        except Exception as e:
            # raise HealthCheckException("Something is wrong, Jira Connection failed.")
            self.add_error(HealthCheckException(f"Jira Connection failed: {str(e)}"), e)
        pass

    def identifier(self):
        return f"Jira Filter Status ({self.issue_count} issues)"
