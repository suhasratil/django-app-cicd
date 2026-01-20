from health_check.backends import BaseHealthCheckBackend
from health_check.exceptions import HealthCheckException

# Create your views here.
# class healthcheckview(View):
#     def get(self, request):
#         url = f"https://bugs-legacy.mojang.com/"
#         try:
#             response = requests.get(url)
#             if response.status_code != 200:
#                 raise HealthCheckException (f"Jira returned {response.status_code}")
#         except requests.RequestException as e:
#             raise HealthCheckException
# myapp/backends.py
from jira import JIRA


class healthcheckview(BaseHealthCheckBackend):
    critical_service = False

    def check_status(self):
        try:
            JIRA("https://bugs-legacy.mojang.com")
        except Exception as e:
            raise HealthCheckException(f"Jira Connectivity Error: {str(e)}")

    def identifier(self):
        return "Jira Status"  # This name shows up in your /health/ UI
