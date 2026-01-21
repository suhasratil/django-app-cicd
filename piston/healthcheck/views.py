from health_check.backends import BaseHealthCheckBackend
from health_check.exceptions import HealthCheckException
from jira import JIRA


class healthcheckview(BaseHealthCheckBackend):
    critical_service = False

    def check_status(self):
        try:
            jira = JIRA(server="https://bugs-legacy.mojang.com/", timeout=(3.0, 5.0), max_retries=0)
            jira_filter = jira.filter("14500")
            jql = jira_filter.jql
            issues = jira.search_issues(jql, maxResults=100)
            issues.total
        except Exception:
            raise HealthCheckException("Something is wrong, Jira Connection failed.")
        pass

    def identifier(self):
        return "Jira Status"
