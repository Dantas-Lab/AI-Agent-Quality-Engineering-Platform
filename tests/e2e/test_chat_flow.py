import pytest
from playwright.sync_api import Page, expect

from tests.e2e.pages.chat_page import ChatPage


@pytest.mark.e2e
def test_user_can_send_message_and_receive_response(
    page: Page,
) -> None:
    chat_page = ChatPage(page)

    chat_page.open()
    chat_page.send_message("How can I update my registration?")

    expect(chat_page.messages).to_contain_text("Assistant:")
    expect(chat_page.messages).to_contain_text("Sources:")
