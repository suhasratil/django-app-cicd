from unittest.mock import MagicMock, patch

from django.test import TestCase

from .views import JiraFilterHealthCheckView


class TestJiraHealthCheck(TestCase):
    def setUp(self):
        self.backend = JiraFilterHealthCheckView()

    @patch("healthcheck.views.JIRA")
    def test_check_status_success(self, mock_jira_class):
        # Mock the JIRA instance and search_issues return value
        mock_jira_instance = mock_jira_class.return_value
        mock_results = MagicMock()
        mock_results.total = 188
        mock_jira_instance.search_issues.return_value = mock_results

        self.backend.check_status()

        # Verify result
        self.assertEqual(self.backend.issue_count, 188)
        self.assertEqual(self.backend.identifier(), "Jira Filter Status (188 issues)")
        self.assertFalse(self.backend.errors)

    @patch("healthcheck.views.JIRA")
    def test_check_status_failure(self, mock_jira_class):
        # Simulate a connection error
        mock_jira_class.side_effect = Exception("Connection Refused")

        self.backend.check_status()

        # Verify the error was caught and recorded
        self.assertTrue(self.backend.errors)
        self.assertIn("Jira Connection failed", str(self.backend.errors[0]))  # codespell:ignore
