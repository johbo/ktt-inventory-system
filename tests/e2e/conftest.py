import os
import subprocess

import pytest

from pages import HomePage, ItemPage, SearchResultsPage


PROJECT_ROOT = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)


@pytest.fixture(scope="session", autouse=True)
def _ensure_e2e_data():
    subprocess.run(
        ["uv", "run", "python", "manage.py", "ensure_e2e_data"],
        cwd=PROJECT_ROOT,
        check=True,
    )


@pytest.fixture
def home_page(page) -> HomePage:
    return HomePage(page)


@pytest.fixture
def item_page(page) -> ItemPage:
    return ItemPage(page)


@pytest.fixture
def search_results_page(page) -> SearchResultsPage:
    return SearchResultsPage(page)
