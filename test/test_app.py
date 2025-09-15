import pytest
from streamlit.testing.v1 import AppTest

@pytest.fixture(scope='module')
def app_test():
  from main import main
  return AppTest.from_function(main, default_timeout=30).run()

def test_app(app_test):
  assert not app_test.exception
