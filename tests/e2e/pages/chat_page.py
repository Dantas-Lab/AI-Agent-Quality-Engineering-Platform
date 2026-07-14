from playwright.sync_api import Page


class ChatPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.message_input = page.locator("#message-input")
        self.submit_button = page.locator("button[type='submit']")
        self.messages = page.locator("#messages")

    def open(self) -> None:
        self.page.goto("http://127.0.0.1:8000")

    def send_message(self, message: str) -> None:
        self.message_input.fill(message)
        self.submit_button.click()

    def get_messages(self) -> str:
        return str(self.messages.inner_text())
