"""Tests for the rule-based chatbot and its JSON endpoint.

Run with: python -m unittest test_chatbot_web -v
"""
import unittest

import chatbot_web
from chatbot_web import MAX_MESSAGE_LENGTH, SimpleChatbot


class RuleMatchingTests(unittest.TestCase):
    def setUp(self):
        self.bot = SimpleChatbot()

    def test_a_word_that_merely_contains_hi_is_not_a_greeting(self):
        self.assertEqual(
            self.bot.ask("which course should I take"),
            self.bot.fallback_response,
        )

    def test_a_word_that_merely_contains_time_does_not_report_the_time(self):
        self.assertEqual(
            self.bot.ask("sometimes I feel low"),
            self.bot.fallback_response,
        )

    def test_a_plain_greeting_matches(self):
        self.assertEqual(self.bot.ask("hi"), "Hello! How can I help you today?")

    def test_a_greeting_inside_a_sentence_matches(self):
        self.assertEqual(
            self.bot.ask("hi there"),
            "Hello! How can I help you today?",
        )

    def test_the_longest_rule_wins_over_a_shorter_one(self):
        self.assertEqual(
            self.bot.ask("tell me a joke"),
            "Why don't scientists trust atoms? Because they make up everything!",
        )
        self.assertEqual(
            self.bot.ask("joke"),
            "Why did the computer show up at work late? It had a hard drive!",
        )

    def test_a_specific_farewell_beats_the_shorter_one(self):
        self.assertEqual(self.bot.ask("goodbye"), "See you later! Take care!")
        self.assertEqual(self.bot.ask("bye"), "Goodbye! Have a great day!")

    def test_apostrophes_do_not_change_the_match(self):
        expected = self.bot.rules["what\u2019s up"]
        self.assertEqual(self.bot.ask("what's up"), expected)
        self.assertEqual(self.bot.ask("whats up"), expected)

    def test_time_is_answered_when_asked_for(self):
        self.assertTrue(self.bot.ask("what time is it").startswith("The current time is"))

    def test_blank_and_missing_messages_fall_back(self):
        for value in ("", "   ", "!!!", None):
            with self.subTest(value=value):
                self.assertEqual(self.bot.ask(value), self.bot.fallback_response)


class EndpointTests(unittest.TestCase):
    def setUp(self):
        chatbot_web.app.config["TESTING"] = True
        self.client = chatbot_web.app.test_client()

    def test_index_serves_the_chat_ui(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"chat-icon", response.data)

    def test_ask_returns_a_reply(self):
        response = self.client.post("/ask", json={"message": "hi"})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.get_json(),
            {"response": "Hello! How can I help you today?"},
        )

    def test_ask_rejects_a_non_json_body(self):
        response = self.client.post("/ask", data="not json", content_type="text/plain")

        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.get_json())

    def test_ask_rejects_a_non_string_message(self):
        response = self.client.post("/ask", json={"message": 42})

        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.get_json())

    def test_ask_rejects_an_overlong_message(self):
        response = self.client.post(
            "/ask", json={"message": "a" * (MAX_MESSAGE_LENGTH + 1)}
        )

        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.get_json())

    def test_reset_still_answers(self):
        response = self.client.post("/reset")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {"response": "Chat reset."})


if __name__ == "__main__":
    unittest.main()
