from health_check.backends import BaseHealthCheckBackend
from health_check.exceptions import HealthCheckException
from jira import JIRA


class healthcheckview(BaseHealthCheckBackend):
    critical_service = False

    def check_status(self):
        try:
            jira = JIRA(server="https://127.0.0.1:8080", timeout=(3.0, 5.0), max_retries=0)
            results = jira.search_issues(jira.filter("14500").jql, maxResults=0)
            results.total
        except Exception as e:
            # raise HealthCheckException("Something is wrong, Jira Connection failed.")
            self.add_error(HealthCheckException("Jira Connection failed"), e)
        pass

    def identifier(self):
        return "Jira Status"
