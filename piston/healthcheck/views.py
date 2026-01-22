import requests
from azure.storage.blob import BlobServiceClient
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


class AzureBlobHealthCheck(BaseHealthCheckBackend):
    critical_service = True

    def check_status(self):
        try:
            service_client = BlobServiceClient.from_connection_string("DefaultEndpointsProtocol=https;AccountName=XXXX;AccountKey=XXXXX;EndpointSuffix=core.windows.net")

            service_client.get_container_client("$logs")  # testlcmih

        except Exception as e:
            self.add_error(HealthCheckException(f"Azure Blob Storage unreachable: {str(e)}"), e)

    def identifier(self):
        return "Azure Blob Storage"


class AzureFrontDoorHealthCheck(BaseHealthCheckBackend):
    critical_service = False

    def check_status(self):
        cdn_url = "https://suhas-test-cdn-efehfubqdxcjbja4.z03.azurefd.net/"

        try:
            requests.get(cdn_url, timeout=5)

        except Exception as e:
            self.add_error(HealthCheckException("Azure Front Door endpoint unreachable"), e)

    def identifier(self):
        return "Azure Front Door CDN"
