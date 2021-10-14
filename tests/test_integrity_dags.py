import pytest 
import logging
from airflow.models import DagBag

LOGGER = logging.getLogger(__name__)

@pytest.fixture
def dagbag():
    return DagBag()

def test_import_dags(dagbag):
    """
    Test that check if dags has import failures
    """
    import_errors = dagbag.import_errors
    msg = f"DAG import failures {import_errors}"
    assert len(import_errors)==0, msg
