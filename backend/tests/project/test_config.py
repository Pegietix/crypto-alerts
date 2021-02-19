import os


class TestEnvironment:
    """Make sure that crucial environment variables are set."""

    def test_glassnode_api_key_set(self):
        self._assert_env_var_set('GLASSNODE_API_KEY')

    def test_mailgun_api_key_set(self):
        self._assert_env_var_set('MAILGUN_API_KEY')

    @staticmethod
    def _assert_env_var_set(env_var_name):
        val = os.getenv(env_var_name)
        assert val and val != 'None'
