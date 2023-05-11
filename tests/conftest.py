"""Fixtures for tests"""
import pytest
import asyncio
import pytest_asyncio

pytest_plugins = ("pytest_homeassistant_custom_component", "pytest_asyncio")


@pytest_asyncio.fixture(autouse=True)
def auto_enable_custom_integrations(enable_custom_integrations):
    yield
